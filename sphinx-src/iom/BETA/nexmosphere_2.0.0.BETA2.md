# Nexmosphere - Version 2.0.0.BETA2

## Module Summary

Interact with Nexmosphere elements via a Nexmosphere Xperience controller.

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (This IO Module is stable and has been tested internally.)
**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.

[//]: # (Always required)
If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope

This module is able to communicate with a subset of Nexmosphere elements.\
Currently supported:
* XN-135M3
* XN-165
* XT-B4N6
* XT-EF30
* XT-EF630
* XT-EF650
* XT-EF680
* XV-H40
* XY-116
* XY-146
* XY-176
* XY-240
* XY-241
* XY-251B
* XY-251G

### Release Notes

#### Version 2.0

* Initial release.

[//]: # (Always required)
*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

## Requirements

A Nexmosphere Xperience controller is required to communicated with Nexmosphere elements.\
This module supports Serially connected, and ethernet connected; Nexmosphere controllers.

## Configuration

The Nexmosphere controller must be fully configured prior to use with this module.\
Nexmosphere elements are automatically configured with suitable settings for operation with this module.

#### <code>Transport: Serial</code>

When using a serially connected Nexmosphere controller, the local controllers serial settings must match.\
Typically a Nexmosphere controller will use:

* Mode: *RS232*
* Baud: *115200*
* Data bits: *8*
* Parity: *None*
* Stop bits: *1*

#### <code>Transport: UDP/IP</code>

When using a UDP/IP connected Nexmosphere controller, it will be required to note the *Controller ID*.\
Typically a Nexmosphere controller will use it's MAC address in colon notation (i.e. 01:23:45:67:89:AB).

## Operation

Not all Nexmosphere elements will support all Triggers and Actions, or exposed values.\
e.g. a XY-116 does not include AirButton support, so will not accept the action *Configure: AirButton* or emit the trigger *Button*.

The logs, during runtime, will detail if the element was unable to accept the action.

During startup, the module will try to discover Nexmosphere elements, this is a slow process that may take over 5 minutes.\
If Nexmosphere elements are added/removed then the Controller will need to be restarted to allow for discovery to run again.

### Instance Properties

Set *Transport* to the connection method the Nexmosphere controller.

*Status LED behavior* Configures the status LED behaviour of all connected Nexmosphere elements.

*Element address limit* should be set to the maximum expected Nexmosphere element address.\
This number will be used as the upper discovery element address limit.\
Setting this value too high will needlessly slow down discovery, setting this number too low will result in missing Nexmosphere elements.

Checking the *Extended Logging* and/or *Log Comms* checkboxes will provide more detailed log messages. These are intended for diagnostics and problem solving and should ideally be disabled during normal operation.

#### <code>Transport: Serial</code>

*Interface* selects the local or remote serial interface.\
*Serial Terminator* selects the message termination character used, this should match your Nexmosphere controller.

#### <code>Transport: UDP/IP</code>

*Datagram Terminator* selects the message termination character used, this should match your Nexmosphere controller.\
*Controller ID*, *Local Port*, and *Remote Port* should match settings configured on your ethernet connected Nexmosphere controller.

*Local Port* and *Remote Port* default to <code>5000</code>.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <style type="text/css">
    td {
        padding: 3 10px;
    }
    </style>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>System</td>
        <td>Is the system online or offline?</td>
    </tr>
    <tr>
        <td>State</td>
        <td>The current module state</td>
            <ul style="margin-top:0px;">
                <li><code>Disconnected</code><br>No communication received from Nexmosphere controller or communication timeout</li>
                <li><code>Connected</code><br>Communication established with Nexmosphere controller, but discovery not performed</li>
                <li><code>Discovering</code><br>Discovering Nexmosphere elements connected to Nexmosphere controller</li>
                <li><code>Discovery complete</code><br>Finished discovering Nexmosphere elements connected to Nexmosphere controller</li>
                <li><code>Auto configuring</code><br>Auto configuring sensible defaults on Nexmosphere elements connected to Nexmosphere controller</li>
                <li><code>Auto configure complete</code><br>Auto configuring complete, Nexmosphere controller and elements are ready to use</li>
            </ul>
    </tr>
    <tr>
        <td>Element count</td>
        <td>Number of discovered Nexmosphere elements</td>
    </tr>
    </tbody>
</table>

### Triggers

#### State

Fires when the module state changes, matching *State*.\
Details of states can be found in Status Variables.

#### Button

Fires when button (or AirButton) *Number* on the element at address *Address* is activated.

Trigger variables:

* *Variable 1*: Element address (*integer*).
* *Variable 2*: Button number (*integer*).

#### Distance

Fires when the proximity sensor on the element at address *Address* changes between the range of *Minimum* and *Maximum*, inclusive.

*Type* specifies if the element support <code>Raw</code> or <code>Absolute</code> or <code>Zone</code> values.\
The trigger will only fire if the element supported the selected type. e.g. XY-116 only supports <code>Raw</code>.

<code>Absolute</code> values are returned as centimeter (cm), <code>Raw</code> values are unitless.

Trigger variables:

* *Variable 1*: Element address (*integer*).
* *Variable 2*: Distance value (*integer*).

#### Swipe

Fires when the element at address *Address* swipe activation matches *Action*.

Trigger variables:

* *Variable 1*: Element address (*integer*).
* *Variable 2*: Swipe direction (*string*).

#### Gestures

Fires when the element at address *Address* gesture report matches *Hand Id*, *Gesture*, and *Direction*.

Trigger variables:

* *Variable 1*: Element address (*integer*).
* *Variable 2*: Hand Id (*integer*).
* *Variable 2*: Gesture (*string*).
* *Variable 2*: Gesture direction (*string*).

### Conditions

#### Connected

Matches if Nexmosphere is discovered, auto configured, connected and ready to go.

### Actions

#### Configure: AirButton

Sends a request to the element at address *Address*, to set the AirButton range(s) to *Range 1*, *Range 2*.

This enables the AirButton if disabled, and may (depending on element type) alter the proximity sensor type to zone.\
Not all elements have multiple AirButtons, elements with a single AirButton will ignore *Range 2*.

#### Control: Output

Sends a request to the element at address *Address*, to set output number *Output* to *State*.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
