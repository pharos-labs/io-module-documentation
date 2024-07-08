# Xicato - Version 2.6.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Integrates the Controller with the Xicato Intelligent Gateways and interact with Xicato Devices.

## Module Status

This IO Module was developed and tested over a Bluetooth mesh network using a *Xicato XIG Gateway* connected to *XIM* fixtures.

Please note that because this IO Module has only been tested with a single gateway, we cannot guarantee operation with a large scale network using multiple Xicato Gateways. Testing is recommended before being used on a live project.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)
This IO Module is stable and has been tested internally.

This IO Module uses both polling, AMQP updates, as well as Actions to retrieve information from the Xicato network, and then fire the relevant Triggers to feed information back to either the Controller or Xicato systems.

Currently the *Get Devices* Action retrieves a list of devices connected to the Xicato Intelligent Gateway(s), but **doesn't** fire any triggers off of the information it has pulled. The information is posted to controller log.
This Action will be reworked in the future.

**Note: This module is intended for use with 20 or less devices. Whilst this may work on larger installations,**
**we can not guarantee that a Controller will be able to successfully discover all devices and this may also impact on Controller performance.**

### Release Notes

### Version 2.6
* &nbsp;Allow use of *Network Name* with spaces.
* &nbsp;Improved validation of Device and Group IDs, allowing for unassigned dotted decimal device ID.
* &nbsp;Added AMQP connection for device updates.
* &nbsp;Removed user polling options and actions.

#### Version 2.5

* &nbsp;Added *Sensor Motion* Trigger.
* &nbsp;Added *Sensor Humidity* Trigger.
* &nbsp;Added *Display Full Response* instance option.

#### Version 2.4

* &nbsp;Added extra error handling for invalid or empty response values.
* &nbsp;Added *Comms Logging* option to view HTTP requests and success status.

#### Version 2.3

* &nbsp;Updated documentation.

#### Version 2.2

* &nbsp;Added *Set HSI-CCT* Action.
* &nbsp;Added *Set Multi-Channel Intensity* Action.
* &nbsp;Added small delay between polling intervals (each instance has its own poll) to prevent clashing.
* &nbsp;Extra error checking when receiving device statistics to prevent invalid values being processed.
* &nbsp;Updated documentation.

#### Version 2.1

* &nbsp;Minor fixes.

#### Version 2.0

* &nbsp;Added Status Variables.
* &nbsp;Added extra authentication Actions.
* &nbsp;Added automatic re-authentication upon polling between the Controller and Xicato Gateway.
* &nbsp;Also added an *Automatic Re-Authentication* Trigger that fires when the Controller detects that the uptime of the gateway is less than the time since it was last authenticated to the Controller.
* &nbsp;Bug fixes and performance enhancements.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

## Configuration

Via either the Xicato Web Interface, or the Xicato Control Panel, retrieve the Xicato network settings. The *Gateway Address* and *Port* which will need to be set to match within the IO Module's Instance Properties.

If you are planning on sending information to any connected Xicato devices, please ensure you also note their Device IDs or Group IDs in the same manner, as this information will be needed by the Actions used to send the information. These are also visible in the Status Variables after each full update poll.

## Operation

Polling is the method used to gather information such as: Gateway statistics, authentication status as well as full information about the connected devices, sensors, and switches. Polling will occur every 60 seconds.
Device updates will be automatically pushed to the Controller via AMQP updates, this allows for instantaneous response to device events (e.g. Motion sensor updates).

Information received through polling and the AMQP updates is then used to fire Triggers.

Polling will also update the Status Variables (viewable in the IO Modules tab of the web interface) that offer useful information on the Xicato system.

For the Controller to be able to communicate with your Xicato Intelligent Gateway it will need to have been authenticated.
Authentication (and re-authentication) will automatically occur during any polling event.
Alternatively, it is possible to authenticate using the *Authenticate Gateway* Action.

### Instance Properties

The Instance Properties cover all the network details for connecting to the Xicato Intelligent Gateway.

Set the *Gateway Address* and *Port* to match the IP and Port for the Xicato Intelligent Gateway network address.
You must also provide the *Network Name* you wish to connect to via the gateway with its *Username* and *Password* login credentials.

*RabbitMQ Username* and *RabbitMQ Password* should contain the AMQP credentials.

Checking the *Extended Logging* checkbox will provide more detailed log messages for fired Triggers and Actions as well as for some higher level communication.
This is intended for diagnostics and problem solving and should be ideally be disabled during normal operation.

Checking the *Comms Logging* checkbox will provide more detailed log messages for the sending of HTTP commands and success responses.
This is intended for diagnostics and problem solving and should be ideally be disabled during normal operation.

Checking the *Display Full Response* checkbox will display the raw JSON response in both the log and in the *Last Response* status variable.
This is intended for diagnostics and problem solving and should be ideally be disabled during normal operation.

### Triggers

#### Gateway Status Changed

This Trigger detects whether there is a change in the connection status with the Xicato Intelligent Gateway.

Use *Status* to define which gateway status change you wish the Trigger to activate off of; *Online* will activate the Trigger when the Xicato Intelligent Gateway comes online, *Offline* when connection is lost to the gateway, and *Any* when it simply changes from either state to the other.

[//]: # (Gateway status: true/false bool as integer: 1 or 0)

#### Device Temperature

Fires in response to either the *Get Device Temperature* Action, or from any device event. If the *ID* field is left empty, then the Trigger will pass the temperature value for any temperature device.

* &nbsp;*Variable 1*: Sensor ID (*string*).
* &nbsp;*Variable 2*: Temperature (*real*)

#### Device Intensity

Fires in response to either the *Get Device Intensity* Action, or from any device event. If the *ID* field is left empty, then the Trigger will pass the intensity value for any lighting device.

* &nbsp;*Variable 1*: Sensor ID (*string*).
* &nbsp;*Variable 2*: Intensity value (*integer*)

#### Sensor Temperature

Fires in response to a sensor event. If the *ID* field is left empty, then the Trigger will pass the lux level value for any sensor device.

Trigger variables:

* &nbsp;*Variable 1*: Sensor ID (*string*).
* &nbsp;*Variable 2*: Lux value (*integer*)

#### Sensor Lux Level

Fires in response to a sensor event. If the *ID* field is left empty, then the Trigger will pass the lux level value for any sensor device.

Trigger variables:

* &nbsp;*Variable 1*: Sensor ID (*string*).
* &nbsp;*Variable 2*: Lux value (*integer*)

#### Sensor Motion

Fires in response to a sensor event. The current *Occupancy* state is derived from the last motion time, using the *Timeout* as an offset from the current time. If the If the *ID* field is left empty, then the Trigger will pass the lux level value for any sensor device.

Trigger variables:

* &nbsp;*Variable 1*: Sensor ID (*string*).
* &nbsp;*Variable 2*: Occupancy value (*integer: 0 = vacant, 1 = occupied*)
* &nbsp;*Variable 2*: Occupancy description (*string*)

#### Gateway Statistics Response

Fires in response to the *Get Gateway Statistics* Action. It will take the Xicato Intelligent Gateway statistics (listed below) and pass them onto a chosen Action.

In the *IO module instance* select the instance of this IO Module that specifies the Xicato Intelligent Gateway you desire. Make sure that the *Get Gateway Statistics* has the matching instance selected, otherwise this Trigger will not fire.

Below is the list of variables this Trigger passes on together with their type in parentheses:

* &nbsp;*Variable 1*: Module instance name (*string*).
* &nbsp;*Variable 2*: Gateway ID (*string*).
* &nbsp;*Variable 3*: Gateway IP address (*string*).
* &nbsp;*Variable 4*: Network name (*string*).
* &nbsp;*Variable 5*: Gateway status: true/false (*bool*: 1 = Online, 0 = Offline).
* &nbsp;*Variable 6*: Last system time (*string*).
* &nbsp;*Variable 7*: Last system uptime (*string*).
* &nbsp;*Variable 8*: Last uptime (*string*).
* &nbsp;*Variable 9*: Temperature (*real* in &deg;C).
* &nbsp;*Variable 10*: Number of networks (*integer*).
* &nbsp;*Variable 11*: Number of devices (*integer*).
* &nbsp;*Variable 12*: Number of sensors (*integer*).
* &nbsp;*Variable 13*: Number of switches (*integer*).

#### Automatic Re-Authentication

Fires if the Controller detects that the gateway's uptime is less than time since the last Controller-gateway authentication time. The Controller will automatically re-authenticate and fire this Trigger passing on the below-listed variables.

* &nbsp;*Variable 1*: System time (Gateway).
* &nbsp;*Variable 2*: System uptime (Gateway) time.
* &nbsp;*Variable 3*: Hardware uptime (Gateway) time.

The *Authenticate Gateway* Action will not cause this Trigger to fire.

This is a useful Trigger for diagnostic purposes of your Xicato network.

### Conditions

#### Gateway Online

This Condition checks whether a given Xicato Intelligent Gateway is Online or Offline. Specify the desired gateway using the *IO module instance* drop-down and selecting the instance related to that gateway.

If the *Negate* checkbox is unchecked, this Condition will check whether the gateway is Online. If it is checked it will check whether it is Offline.

### Actions

#### Set Intensity

Sets the *Intensity* (as %) and *Fade time* (in s) for a given *Target*.

The *Target* can be either a *Device*, or *Group* of devices specified by a given *ID* value. Or alternatively it can be *Broadcast* to all available devices within that Xicato network.

#### Set Multi-Channel Intensity

Sets the *Master Intensity* (as %), * and *Fade time* (in s) for a given *Target*. *Channel Intensities* is a comma separated list of individual channel intensities for a given device.

The *Target* can be either a *Device*, or *Group* of devices specified by a given *ID* value.

#### Set HSI-CTT

Sets the *Hue* (as degrees out of 360), *Saturation* (as %), *Intensity* (as %), *CCT* (as Kelvin) and *Fade time* (in s) for a given *Target*.

The *Target* can be either a *Device*, or *Group* of devices specified by a given *ID* value. Or alternatively it can be *Broadcast* to all available devices within that Xicato network.

##### Recall Scene

Recalls a *Scene* (*integer*) and sets the *Fade time* (in s) for a given *Target*.

The *Target* can be either a *Device*, or *Group* of devices specified by a given *ID* value. Or alternatively it can be *Broadcast* to all available devices within that Xicato network.

#### Sensor Response

Set **all** sensors within the Xicato network (specified by the *IO module instance*) to the *Status* setting of either *Enabled* or *Disabled*. This effectively allows you to enable or disable all sensors within a Xicato network in a single Action.

#### Get Gateway Status

Issues a get status command to the Xicato Intelligent Gateway specified by the *IO module instance*. This will fire the *Get Gateway Status* Trigger that will capture, and pass onto the chosen Action, that gateways status as variables. See the *Get Gateway Status* Trigger section for details on the variables passed.

#### Get Gateway Statistics

Issues a get statistics command to the Xicato Intelligent Gateway specified by the *IO module instance*. This will fire the *Get Gateway Statistics* Trigger that will capture, and pass onto the chosen Action, that gateways statistics as variables. See the *Get Gateway Statistics* Trigger section for details on the variables passed.

#### Get Devices

Issues a command to get information for all the devices connected to the Xicato Intelligent Gateway specified by the *IO module instance*.

**Note** at present this Action does not yet have a counter-part Trigger, this will be added in future.

At the moment this Action can be used for diagnostic purposes to receive information of devices within Controller log.

#### Get Device Temperature

Issues a get temperature command to a temperature sensor of given *ID* value connected to the Xicato Intelligent Gateway specified by the *IO module instance*. This will fire any *Device Temperature* Triggers that will capture, and pass onto the chosen Action, the sensor's temperature reading (in &deg;C).

#### Get Device Intensity

Issues a get intensity command to a Xicato light fixture of given *ID* value connected to the Xicato Intelligent Gateway specified by the *IO module instance*. This will fire any *Device Intensity* Triggers that will capture, and pass onto the chosen Action, the fixture's intensity value (*integer*).

#### Set Scene

Creates (or overwrites) the scene for a specified device with given *ID* in the Xicato network specified by the *IO module instance*. The Action allows the *Scene Number*, *Intensity*, *Delay*, and *Fade time* of the scene to be set for that device.

#### Authenticate Gateway

Forces a re-authentication between the Controller and gateway. This Action will not fire the “Automatic Re-authentication” Trigger.

[//]: # (### Status Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in Actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
