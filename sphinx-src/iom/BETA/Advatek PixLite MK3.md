# Advatek PixLite MK3 - Version 2.1.0.BETA1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Queries an Advatek PixLite MK3 Controller.

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (This IO Module is stable and has been tested internally and externally.)
**Note:** Please be aware that this is an beta version of this IO Module for evaluation purposes only and has not yet been fully tested.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1
* &nbsp;Adds Trigger match types "Is NOT In Range" and "Exits Range".

#### Version 2.0

* &nbsp;Added *Version/Name Response* Trigger.
* &nbsp;Added *Temperature Statistics Response* Trigger.
* &nbsp;Added *Port Power Response* Trigger.
* &nbsp;Added *Bank Voltage Response* Trigger.
* &nbsp;Added *Port Fuse Good Response* Trigger.
* &nbsp;Added *Request Version/Name* Action.
* &nbsp;Added *Request Device Statistics* Action.
* &nbsp;Added *Identify* Action.
* &nbsp;Added *Stop Identify* Action.
* &nbsp;Added Status variables.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

Version and name data is requested at startup as well as using the *Request Version/Name* Action. The status variables will be updated in both cases.

The Triggers *Temperature Statistics Response*, *Port Power Response*, *Bank Voltage Response* and *Port Fuse Good Response*
will all be fired in response to a *Request Device Statistics* Action.

### Instance Properties

Set the *Host IP Address* to the address of the Advatek PixLite MK3 Controller.

If enabled, *Log Requests and Responses* will show all outbound and inbound HTTP message in the log.
This is intended for diagnostic purposes and should ideally be disabled during normal operation to maintain a clean log
and to maintain Controller performance.

If enabled, *Log Triggers and Action* will show information on Actions and Triggers, including errors, in the log.
This is intended for diagnostic purposes but may be useful in normal operation.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Nickname&nbsp;&nbsp;&nbsp;</td>
        <td>Name of the PixLite MK3 Controller as set by the user.</td>
    </tr>
    <tr>
        <td>Product Name&nbsp;&nbsp;&nbsp;</td>
        <td>Specific product type name.</td>
    </tr>
    <tr>
        <td>Product Family&nbsp;&nbsp;&nbsp;</td>
        <td>The product family code.</td>
    </tr>
    <tr>
        <td>Product Family Name&nbsp;&nbsp;&nbsp;</td>
        <td>The name of the product range.</td>
    </tr>
    <tr>
        <td>Firmware Version&nbsp;&nbsp;&nbsp;</td>
        <td>Current firmware version.</td>
    </tr>
    <tr>
        <td>API Version&nbsp;&nbsp;&nbsp;</td>
        <td>The API version which is used by this module to communicate.</td>
    </tr>
    <tr>
        <td>Bank Voltage&nbsp;&nbsp;&nbsp;</td>
        <td>The current supply voltage.</td>
    </tr>
    <tr>
        <td>Current Power (Milliamps)&nbsp;&nbsp;&nbsp;</td>
        <td>The current draw of each port in Milliamps.</td>
    </tr>
    <tr>
        <td>Fuse Good&nbsp;&nbsp;&nbsp;</td>
        <td>The current state of each port's fuse.</td>
    </tr>
    <tr>
        <td>Current Temperature&nbsp;&nbsp;&nbsp;</td>
        <td>The current temperature of the PixLite MK3 Controller in °C.</td>
    </tr>
    <tr>
        <td>Minimum Temperature&nbsp;&nbsp;&nbsp;</td>
        <td>The lowest temperature the PixLite MK3 Controller has reached during operation in °C.</td>
    </tr>
    <tr>
        <td>Maximum Temperature&nbsp;&nbsp;&nbsp;</td>
        <td>The highest temperature the PixLite MK3 Controller has reached during operation in °C.</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Version/Name Response

Fires in response to a *Request Version/Name* Action.

The response will set the status variables and pass the below Trigger variables.
If *Include Key In Trigger Variables* is checked, the Trigger variables will be in the format "Key: Value", otherwise the variable will just be the values.

Trigger variables:

* &nbsp;*Variable 1*: Nickname Address (*string*).
* &nbsp;*Variable 2*: Product Name (*string*)
* &nbsp;*Variable 3*: Product Family (*string*)
* &nbsp;*Variable 4*: Product Family Name (*string*)
* &nbsp;*Variable 5*: Firmware Version (*string*)
* &nbsp;*Variable 6*: API Version (*string*)

#### Temperature Statistics Response

Fires in response to a *Request Device Statistics* Action with current, minimum and maximum temperatures.

If the *Parameter*, *Match Type*, *Minimum* temperature and *Maximum* temperature properties all match the received data, the Trigger will match and the below Trigger variable will be passed. If <code>Any</code> *Parameter* is selected and the Trigger matches for _any_ of the current, minimum or maximum temperatures, all three values will be passed as Trigger variables.

* &nbsp;*Variable 1*: Current temperature (*real in °C*).
* &nbsp;*Variable 2* (or *1* for specified parameter: Minimum Temperature Name (*real in °C*)
* &nbsp;*Variable 3* (or *1* for specified parameter: Maximum Temperature (*real in °C*)

#### Port Power Response

Fires in response to a *Request Device Statistics* Action with port power of individual ports.

The properties will be checked against the value of a specific  *Port* or <code>Any</code> to check all ports.

If the *Port*, *Match Type*, *Minimum* Milliamps and *Maximum* Milliamps properties all match the received data, the Trigger will match and the below Trigger variable will be passed.

* &nbsp;*Variable 1*: Port number (*integer*).
* &nbsp;*Variable 2*: Current power (*Milliamps as integer*)
* &nbsp;*Variable 3*: Description of Trigger match (*string*)

#### Bank Voltage

Fires in response to a *Request Device Statistics* Action with the current supply voltage.

If the *Port*, *Match Type*, *Minimum* Millivoltage and *Maximum* Millivoltage properties all match the received data, the Trigger will match and the below Trigger variable will be passed.

* &nbsp;*Variable 1*: Current voltage (*Millivolts as integer*).
* &nbsp;*Variable 2*: Current voltage (*Volts as real*)
* &nbsp;*Variable 3*: Description of Trigger match (*string*)

#### Port Fuse Good Response

Fires in response to a *Request Device Statistics* Action with the current state of each port's fuse.

The properties will be checked against the value of a specific  *Port* or <code>Any</code> to check all ports.

If the *Port* and *Fuse Status*, the Trigger will match and the below Trigger variable will be passed.
If </code>Any</code> *Port* is selected, the Trigger will fire is any of the ports match the *Fuse Status*, passing all statues as Trigger Variables.

* &nbsp;*Variable 1*: Port status 1 (or specific port) (*integer - 0 = Bad, 1 = Good*).
* &nbsp;*Variable 2*: Port status 2 (*integer - 0 = Bad, 1 = Good*).
* &nbsp;*Variable 3*: Port status 3 (*integer - 0 = Bad, 1 = Good*).
* &nbsp;*Variable 4*: Port status 4 (*integer - 0 = Bad, 1 = Good*).


[//]: # (### Conditions)

[//]: # (#### Conditions Name)
[//]: # (#### Start with a verb such as "Is met when..." or "Returns true if...")

### Actions

#### Request Version Name

Sends a request to the PixLite MK3 Controller to report version and name information.
The response will fire a *Version/Name Response* Trigger if one exists in the project.

The Action will also update the status variables.

#### Request Device Statistics

Sends a request to the PixLite MK3 Controller to report information on temperature, power and port status.

The response will fire *Temperature Statistics Response*, *Port Power Response*, *Bank Voltage Response* and *Port Fuse Good Response* Triggers if any exists in the project.

The Action will also update the status variables.

#### Identify

Sends a request to the PixLite MK3 Controller to identify itself by way of flashing the LED orange on the front of the Controller.

The *Duration* determines how long to display the identify LED or <code>0</code> for continuous identification,
until the Controller is rebooted or a *Stop Identify* Action is called.

#### Stop Identify

Sends a request to the PixLite MK3 Controller to stop identifying itself if it is already in the identify mode.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
