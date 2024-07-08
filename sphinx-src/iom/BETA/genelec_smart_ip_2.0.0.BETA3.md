# Genelec Smart IP - Version 2.0.0.BETA3

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Interact with Genelec Smart IP Speakers.

[//]: # (Brief description of the module; usually the same as the description in the package)

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (This IO Module is stable and has been tested internally.)
**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.

[//]: # (Always required)
If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0 Beta 3

* Adds support for Multicast API.

[//]: # (Always required)
*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

## Requirements
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)
Compilable with models: 4410A, 4420A, 4430A, 4435A, and 4436A

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

**Note:** For correct operation of device discovery, please ensure the default gateway is correctly set on the Controller's network interface.

The module can operate in two main control modes, <code>Multiple device</code> and <code>Single device</code>.
When operating in <code>Multiple device</code>, commands are multicast to a number of devices.
There is no feedback from these devices, and certain actions and trigger functions are invalid in this mode.\
Genelec firmware v1.3.25 or later is required for <code>Multiple device</code> control.

To obtain individual feedback from devices, while retaining multicast control, it's fine to create multiple instances to obtain both <code>Multiple device</code> and <code>Single device</code> operation.

### Module Properties

Checking the *Extended Logging* checkbox will provide detailed log messages about discovery operations.\
This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

### Instance Properties

[//]: # (### List instance properties and their function)

*Control mode* sets the operating mode, different properties are then available dependent on mode.

*Volume scaling* can be set to either <code>Logarithmic</code> or <code>Linear</code> and affects the scaling used between decibels and percent.

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

#### Control mode - Single device
Set the *Receiver* to either that of the host name (e.g. <code>4420-010203</code>) or the IP address (e.g. <code>192.168.0.1</code>) of the receiver.\
If the host name is set, then the device is automatically discovered on the network.\
If set to IP address, optionally a port can be used by appending :{port number} e.g. <code>192.168.0.1:9000</code>

Authentication credentials should be entered into *Username* and *Password*.

Setting the *Update interval* will dictate how often the receiver is polled for updates.

#### Control mode - Multiple device
The multicast *Group address* and *Group port* should be set to match that of the receiver group.

#### Status Variables

**Note:** Feedback is not available in <code>Multiple device</code> mode

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

Some of these variables will unavailable unless receiver's power status is <code>Active</code>.

<table>
    <style type="text/css">
    td {
        padding: 3 10px;
    }
    </style>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Connection</td>
        <td>Result of last connection attempt</td>
            <ul style="margin-top:0px;">
                <li><code>Access denied</code></li>
                <li><code>Offline</code></li>
                <li><code>Online</code></li>
                <li><code>Unknown</code></li>
                <li><code>Multicast mode</code></li>
            </ul>
    </tr>
    <tr>
        <td>Power status</td>
        <td>Current power status</td>
            <ul style="margin-top:0px;">
                <li><code>Standby</code></li>
                <li><code>Active</code></li>
                <li><code>Sleep</code></li>
                <li><code>PoE Fail</code></li>
            </ul>
    </tr>
    <tr>
        <td>Receiver name</td>
        <td>Receiver display name</td>
        <tr>
            <i><small>Not available if instance property <code>Receiver</code> was set to an IP Address</small></i>
        </tr>
    </tr>
    <tr>
        <td>Receiver IP</td>
        <td>Resolved IP Address of the receiver</td>
    </tr>
    <tr>
        <td>Zone number</td>
        <td>Current zone number of the receiver</td>
    </tr>
    <tr>
        <td>Zone name</td>
        <td>Current zone name of the receiver</td>
    </tr>
    <tr>
        <td>Volume</td>
        <td>Current audio volume in Decibels (-130.0 dB to 0.0 dB) and percent</td>
    </tr>
    <tr>
        <td>Mute</td>
        <td>Is the audio output muted?</td>
    </tr>
    <tr>
        <td>Inputs</td>
        <td>List of enabled audio inputs</td>
    </tr>
    <tr>
        <td>Profile number</td>
        <td>Active profile number</td>
    </tr>
    <tr>
        <td>Profile name</td>
        <td>Active profile name</td>
    </tr>
    <tr>
        <td>Firmware version</td>
        <td>Reported firmware version</td>
    </tr>
    <tr>
        <td>PoE</td>
        <td>Current power drawn from PoE (power over ethernet)</td>
    </tr>
    <tr>
        <td>LED brightness</td>
        <td>Brightness of the front panel LEDs</td>
    </tr>
    <tr>
        <td>RJ45 LED</td>
        <td>RJ45 Ethernet connector status LED</td>
            <ul style="margin-top:0px;">
                <li><code>Enabled</code></li>
                <li><code>Disabled</code></li>
            </ul>
    </tr>
    <tr>
        <td>Clip LED</td>
        <td>Clip LED (Subwoofer only) status</td>
            <ul style="margin-top:0px;">
                <li><code>Enabled</code></li>
                <li><code>Disabled</code></li>
            </ul>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

[//]: # (Start with a verb such as "Fires when..." or "Receives...")

### Updated connection
**Note:** Not available in <code>Multiple device</code> mode

Fires when the connection status to the receiver changes, matching *Status*.

Trigger variables:

* &nbsp;*Variable 1*: <code>Online</code> or <code>Offline</code> (*string*).

### Updated power
**Note:** Not available in <code>Multiple device</code> mode

Fires when the controller receives an updated power level, matching *Mode*.

Trigger variables:
* &nbsp;*Variable 1*: <code>Standby</code>, <code>Active</code>, <code>Sleep</code>, <code>PoE Fail</code> (*string*).

#### Updated volume
**Note:** Not available in <code>Multiple device</code> mode

Fires when the controller receives an updated volume level.

Trigger variables:

* &nbsp;*Variable 1*: Decibel level (*number*).
* &nbsp;*Variable 2*: Percentage (*number*).

#### Updated mute
**Note:** Not available in <code>Multiple device</code> mode

Fires when the controller receives an updated audio mute, matching *Set*.

Trigger variables:

* &nbsp;*Variable 1*: Mute set (*boolean*).

#### Updated profile
**Note:** Not available in <code>Multiple device</code> mode

Fires when the controller receives an updated profile, matching *Number*.

Trigger variables:

* &nbsp;*Variable 1*: Profile number (*integer*).
* &nbsp;*Variable 2*: Profile name (*string*).

### Actions

[//]: # (Start with a verb such as "Requests..." or "Starts...")

#### Set power

Requests the receiver to set power *Mode*.
n.b. Some actions maybe unavailable when not in <code>Active</code>.

#### Set volume (dB)

Requests the receiver to set audio volume *Level* dB.

#### Set volume (Percent)

Requests the receiver to set audio volume *Level* %.

#### Set mute

Requests the receiver to *Set* or unset audio mute.

#### Set inputs
**Note:** Not available in <code>Multiple device</code> mode

Requests the receiver to set audio inputs to a combination of *Analogue*, *Dante 1*, *Dante 2*.

#### Set profile

Requests the receiver to current profile to *Number*.
Optionally the default startup will be set to *Number* if *Default* is set.

#### Set LED
**Note:** Not available in <code>Multiple device</code> mode

Requests the receiver to set the front panel LED *Intensity*\.
The RJ45 connector LEDs, and Clip LED (subwoofers only); can be enabled/disabled.

#### Log details

For information only.\
Log in full the results from *ID*, *Info*, *Power*, *Events*, *Profiles*.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
