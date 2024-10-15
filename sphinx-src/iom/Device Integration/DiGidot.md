# DiGidot - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Sends queries and commands to DiGidot C4 devices and parses the responses.

## Module Status

**Note:** This module has been tested internally but has limited field testing. Testing is recommended before being used on a live project.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Initial release.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

## Configuration

This module uses the DiGidot HTTP API. By default, the DiGidot devices does not allow HTTP calls so this must first be enabled.

From a web browser:

1. Go to the device’s web interface, either by entering the IP address of the device directly or using the IP address 10.254.254.254
2. On the device's home page, select "Triggers"
3. Click the menu in the top-right corner, "...", and select "HTTP, UDP and OSC trigger"
4. Select "Enable' HTTP Get' Triggers"

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Set the *IP Address* to the DiGidot C4 controller.

The actual *MAC Address* of the DiGidot C4 is not required,
however the *MAC Address* type can be specified to communicate with *Device Only* (using the *IP Address*)
or *All Devices* on the network.

If enabled, *Log Requests and Responses* will show all outbound and inbound HTTP message in the log.
This is intended for diagnostic purposes and should ideally be disabled during normal operation to maintain a clean log
and to maintain Controller performance.

If enabled, *Log Triggers and Action* will show information on Actions and Triggers, including errors, in the log.
This is intended for diagnostic purposes but may be useful in normal operation.

*Scenes Response Triggers* determines how the response for a *Request Scenes* is used.

If <code>Individual Triggers</code> is selected, then a Trigger will fire for each scene received,
<code>Individual Lines</code> will fire one Trigger with a description of each scene as a variable,
and <code>Individual Variables</code> will fire on Trigger with all scene data with many variables for each scene.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Device Name</td>
        <td>Name of DiGidot C4 received from device settings.</td>
    </tr>
    <tr>
        <td>MAC Address</td>
        <td>MAC address of DiGidot C4 received from device settings.</td>
    </tr>
    <tr>
        <td>Ethernet (i)</td>
        <td>IP Address of Ethernet 1 (0) interface</td>
    </tr>
    <tr>
        <td>Ethernet (ii)</td>
        <td>IP Address of Ethernet 2 (1) interface</td>
    </tr>
    <tr>
        <td>Wifi</td>
        <td>IP Address of Wifi interface</td>
    </tr>
    <tr>
        <td>Version</td>
        <td>DiGidot C4 firmware version.</td>
    </tr>
    <tr>
        <td>Master Brightness</td>
        <td>In percent along with the internal 16 bit value.</td>
    </tr>
    <tr>
        <td>Last Message Sent</td>
        <td>Last message sent from Actions or startup, if delivered.</td>
    </tr>
    <tr>
        <td>Last Response Received&nbsp;&nbsp;&nbsp;</td>
        <td>Last response, usually an OK or error.</td>
    </tr>
    <tr>
        <td>Last Scene Called</td>
        <td>Last Scene Recall Action send, if delivered, with result.</td>
    </tr>
    <tr>
        <td>Last Scene Called</td>
        <td>Last Scene Recall Action send, if delivered, with result.</td>
    </tr>
    <tr>
        <td>Scene n</td>
        <td>The first 38 scenes: Scene ID, scene name and fade time retrieved from the DiGidot C4 (Not necessarily the definitive list).</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Any Response Received

Fires when any response is received from the DiGidot C4 whether a valid response or an error. This is for information purposes.

Trigger variables:

* &nbsp;*Variable 1*: MAC Address (*string*).
* &nbsp;*Variable 2*: Result (*string*)
* &nbsp;*Variable 3-n*: Extra relevant data (*any type*)

#### Scenes Response

Fires in response to a *Recall Scene* Action.

If <code>Individual Triggers</code> is selected in the instance properties, then a Trigger will fire for each scene received,
with the following Trigger variables:

* &nbsp;*Variable 1*: Scene Index (as seen in status variables) (*integer*).
* &nbsp;*Variable 2*: DiGidot scene ID (*integer*).
* &nbsp;*Variable 3*: Scene Name (*string*).
* &nbsp;*Variable 4*: Scene Fade Time (*integer in ms*).
* &nbsp;*Variable 5*: MAC Address (*string*).

If <code>Individual Lines</code> is selected, one Trigger with file with a description of each scene as a separate Trigger variables:

* &nbsp;*Variable 1-n*: Scene description (ID, name, fade time) (*string*).
* &nbsp;*Last Trigger Variable*: MAC Address (*string*).

If <code>Individual Variables</code> is selected, one Trigger will fire with all values for all scenes as their own Trigger variables, for example

* &nbsp;*Variable 1*: Scene 1 Index (as seen in status variables) (*integer*).
* &nbsp;*Variable 2*: Scene 1 ID (*integer*).
* &nbsp;*Variable 3*: Scene 1 Name (*string*).
* &nbsp;*Variable 4*: Scene 1 Fade Time (*integer in ms*).
* &nbsp;*Variable 5*: Scene 2 Index (as seen in status variables) (*integer*).
* &nbsp;*Variable 6*: Scene 2 ID (*integer*).
* &nbsp;*Variable 7*: Scene 2 Name (*string*).
* &nbsp;*Variable 8*: Scene 2 Fade Time (*integer in ms*).
* &nbsp;*Variables ...*
* &nbsp;*Last Trigger Variable*: MAC Address (*string*).

#### Brightness Response

Fires in response to a *Request Brightness* Action.

Trigger variables:

* &nbsp;*Variable 1*: MAC Address (*string*).
* &nbsp;*Variable 2*: Result (*string*)
* &nbsp;*Variable 3-n*: Extra relevant data (*any type*)

#### Device Settings Response

Fires in response to a *Request Device Settings* Action.

Trigger variables:

* &nbsp;*Variable 1*: MAC Address (*string*).
* &nbsp;*Variable 2*: Name (*string*).
* &nbsp;*Variable 3*: Version (*integer*).

#### Network Settings Response

Fires in response to a *Request Network Settings* Action. If *Log Triggers and Actions* is enabled, a description of the network will be logged before the Trigger is fired.

Trigger variables:

* &nbsp;*Variable 1*: MAC Address (*string*).
* &nbsp;*Variable 2*: Ethernet 1 (0) IP Address (*string*).
* &nbsp;*Variable 3*: Ethernet 2 (1) IP Address (*string*).
* &nbsp;*Variable 4*: Ethernet Subnet Mask (*string*).
* &nbsp;*Variable 5*: WiFi IP Address (*string*).
* &nbsp;*Variable 6*: WiFi Subnet Mask (*string*).
* &nbsp;*Variable 7*: Gateway IP Address (*string*).

[//]: # (### Conditions)

[//]: # (#### Conditions Name)
[//]: # (#### Start with a verb such as "Is met when..." or "Returns true if...")

### Actions

#### Request Device Settings

Sends a request to the DiGidot device to get device settings data. The reply will fire a *Device Settings Response* Trigger.

#### Request Network Settings

Sends a request to the DiGidot device to get device settings data. The reply will fire a *Network Settings Response* Trigger.

#### Recall Scene

Sends a command to the DiGidot device to recall a scene. The *Scene ID* can be either the scene index, as shown in the status variables and Trigger variables, or the DiGidot scene ID, also showing in in the status variables and Trigger variables.

If the *Scene ID*, index or DiGidot ID, can not be found or is not displayed, a command will still be sent and the response displayed.

#### Stop Playback

Sends a request to the DiGidot device to stop all playback.

#### Set Intensity Channels

Sends a request to set the master intensity/brightness as a 16 bit number, specified by the *Course* (high byte) and *Fine* (low byte) values.

If either *Course* or *Fine* is set to <code>Ignore</code>, then the new intensity will be calculated using the respective non-ignored byte and current master brightness (if known). If the current brightness is not known, then an error message will be logged.

#### Set Intensity

Sends the same request as the *Set Intensity Channels* Action, but the 16-bit intensity is calculated differently.

If <code>16 bit</code> *Format* is selected, there will no conversion of the *Intensity* value.

If <code>8 bit</code> *Format* is selected, the 8 bit *Intensity* will be converted to a 16-bit value.

If </code>%</code> *Format* is selected, then the percentage *Intensity* will be converted to a 16-bit value.

The *Intensity* is always relative to the *Format*. If the *Intensity* is out of range of the *Format*,
the *Intensity* value will be rounded up to maximum value before being sent and a log message show this has happened.

#### Request Current Brightness

Sends a request to the DiGidot device to get the current master brightness/intensity. The reply will fire a *Brightness Response* Trigger.

#### Request Current Brightness

Sends a request to the DiGidot device to get data on all scenes, up to the maximum of  38. The reply will fire *Scenes Response* Triggers according to the *Scenes Response Triggers* instance property. The Triggers: *Scenes Response* section of this readme explains this in more detail.

[//]: # (#### Action Name)
[//]: # (#### Start with a verb such as "Sends..." or "Sets...")

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
