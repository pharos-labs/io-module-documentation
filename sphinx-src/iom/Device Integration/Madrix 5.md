# Madrix 5 - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Remote control of Madrix 5 using HTTP.

[//]: # (Brief description of the module; usually the same as the description in the package)

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)
This IO Module is stable and has been tested internally.

[//]: # (Always required)
If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* Initial release.

[//]: # (Always required)
*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

## Configuration
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

"HTTP Remote Control" should be enabled on the target network interface.\
Remote control options can be found under "Preferences" in Madrix 5 toolbar.

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

[//]: # (### List instance properties and their function)

Set the *IP Address* to that configured on the device.

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.


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
        <td>Connection</td>
        <td>Result of last connection attempt</td>
        <ul style="margin-top:0px;">
            <li><code>Unknown</code></li>
            <li><code>Offline</code></li>
            <li><code>Online</code></li>
        </ul>
    </tr>
    <tr>
        <td>Host name</td>
        <td>Reported hostname of the remote peer</td>
    </tr>
    <tr>
        <td>Host label</td>
        <td>Madrix instance identification label</td>
    </tr>
    <tr>
        <td>Version</td>
        <td>Madrix software version</td>
    </tr>
    <tr>
        <td>Fade type</td>
        <td>Current fade type</td>
        <ul style="margin-top:0px;">
            <li><code>Unknown</code></li>
            <li><code>Cross fade</code></li>
            <li><code>White fade</code></li>
            <li><code>Black fade</code></li>
            <li><code>Wipe X</code></li>
            <li><code>Wipe Y</code></li>
            <li><code>Wipe XC</code></li>
            <li><code>Wipe YC</code></li>
            <li><code>Slide X</code></li>
            <li><code>Slide Y</code></li>
            <li><code>Slide XC</code></li>
            <li><code>Slide YC</code></li>
            <li><code>Wipe Z</code></li>
            <li><code>Wipe ZC</code></li>
            <li><code>Slide Z</code></li>
            <li><code>Slide ZC</code></li>
        </ul>
    </tr>
    <tr>
        <td>Fade time</td>
        <td>Current fade time</td>
    </tr>
    <tr>
        <td>Fade value</td>
        <td>Current fade value between deck A and deck B</td>
    </tr>
    <tr>
        <td>Active storage</td>
        <td>Currently active storage bin and storage place</td>
    </tr>
    <tr>
        <td>Bank A storage</td>
        <td>Bank A storage bin and storage place</td>
    </tr>
    <tr>
        <td>Bank B storage</td>
        <td>Bank B storage bin and storage place</td>
    </tr>
    <tr>
        <td>Cuelist</td>
        <td>Selected cuelist and playback status</td>
    </tr>
    <tr>
        <td>Timeline</td>
        <td>Selected, and if active, it's playback state; else selected and active timelines</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

[//]: # (Start with a verb such as "Fires when..." or "Receives...")

### Updated connection

Fires when the connection status to the remote Madrix peer changes, matching *Status*.

Trigger variables:

* *Variable 1*: <code>Online</code> or <code>Offline</code> (*string*).

#### Updated fade type

Fires when the Madrix fade type changes, matching *Type*.

Trigger variables:

* *Variable 1*: Fade type name (*string*).

#### Updated fade time

Fires when the Madrix fade time changes, matching *Time*.

Trigger variables:

* *Variable 1*: Fade time in seconds (*integer*).

#### Updated fade value

Fires when the Madrix fade between deck A and deck B changes, matching the *Value is* and *Value* properties.

Trigger variables:

* *Variable 1*: Fade value (*byte*).

#### Updated master fader

Fires when the Madrix master fader value changes, matching the *Value is* and *Value* properties.

Trigger variables:

* *Variable 1*: Master fader value (*byte*).

#### Updated storage

Fires when the Madrix storage changes, matching the *Bank*, *Storage*, and *Place* properties.

Trigger variables:

* *Variable 1*: Active storage (*integer*).
* *Variable 2*: Bank A storage (*integer*).
* *Variable 3*: Bank B storage (*integer*).
* *Variable 4*: Active storage place (*integer*).
* *Variable 5*: Bank A storage place (*integer*).
* *Variable 6*: Bank B storage place (*integer*).

#### Updated cuelist

Fires when the Madrix selected cuelist changes, matching the *Cuelist* and *Playing* properties.\
<i>n.b. Cuelist <code>0</code> represents no selected cuelist</i>

Trigger variables:

* *Variable 1*: Selected cuelist (*integer*).

#### Updated timeline

Fires when the Madrix selected timeline changes, matching the *Timeline* and *State* properties.\
<i>n.b. Timeline <code>0</code> represents no selected timeline</i>

Trigger variables:

* *Variable 1*: Selected cuelist (*integer*).

### Conditions

[//]: # (Start with a verb such as "Matches if...")

#### Fade type

Matches if the Madrix fade type matches *Type*.

Condition variables:

* *Variable 1*: Fade type name (*string*).

#### Fade time

Matches if the Madrix fade time matches *Time*.

Condition variables:

* *Variable 1*: Fade time in seconds (*integer*).

#### Fade value

Matches if the Madrix fade between deck A and deck B matches *Value is* and *Value*.

Condition variables:

* *Variable 1*: Fade value (*byte*).

#### Master fader

Matches if the Madrix master fader matches *Value is* and *Value*.

Condition variables:

* *Variable 1*: Master fader (*byte*).

#### Storage

Matches if the Madrix bank *Bank* storage matches *Storage* and *Place*.

Condition variables:

* *Variable 1*: Active storage (*integer*).
* *Variable 2*: Bank A storage (*integer*).
* *Variable 3*: Bank B storage (*integer*).
* *Variable 4*: Active storage place (*integer*).
* *Variable 5*: Bank A storage place (*integer*).
* *Variable 6*: Bank B storage place (*integer*).

#### Cuelist

Matches if the Madrix selected cuelist matches *Cuelist* and *State*.

Condition variables:

* *Variable 1*: Selected cuelist (*integer*).

### Actions

[//]: # (Start with a verb such as "Requests..." or "Starts...")

#### Set fade type

Sends a request to Madrix to set the fade type to *Type*.

#### Set fade time

Sends a request to Madrix to set the fade time to *Time*.

#### Set fade value

Sends a request to Madrix to set the fade between deck A and deck B to *Value*.

#### Set master fader

Sends a request to Madrix to set the master fader to *Value*.

#### Set storage

Sends a request to Madrix to set the bank *Bank* to storage place *Place* from storage bank *Storage*, with or without a *Fade*.

#### Set selected cuelist

Sends a request to Madrix to set the selected cuelist to *Value*.

#### Set cuelist state

Sends a request to Madrix to set the selected cuelist play state to *State*.

#### Set selected timeline

Sends a request to Madrix to set the selected timeline to *Value*.

#### Set timeline state

Sends a request to Madrix to set the selected timeline play state to *State*.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
