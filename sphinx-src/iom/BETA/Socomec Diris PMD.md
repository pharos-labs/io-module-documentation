# Socomec Diris PMD - Version 2.0.0.BETA1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

[//]: # (Brief description of the module; usually the same as the description in the package)
Interact with Socomec Diris Power Monitoring Device (PMD) via Modbus/TCP

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (This IO Module is stable and has been tested internally.)
[//]: # (**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)

[//]: # (Always required)
If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Initial release.

[//]: # (Always required)
*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

## Requirements
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)
The Socomec device may require an optional ethernet hardware module.

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

[//]: # (### List instance properties and their function)

Select the appropriate *Model*. n.b. The A40 and A-40 are different models.

Set the *IP Address*, *Port*, and *Modbus ID*; to that configured on the device.

The *Poll Interval* and *Start Poll on Init* can be altered as required to fine tune polling requirements.

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
        <td>Connected</td>
        <td>Connected to device, true/false</td>
    </tr>
    <tr>
        <td>Frequency</td>
        <td>Last polled line frequency</td>
    </tr>
    <tr>
        <td>Phase 1 to Neutral Voltage</td>
        <td>Last polled voltage between Live 1 and Neutral</td>
    </tr>
    <tr>
        <td>Phase 2 to Neutral Voltage</td>
        <td>Last polled voltage between Live 2 and Neutral</td>
    </tr>
    <tr>
        <td>Phase 3 to Neutral Voltage</td>
        <td>Last polled voltage between Live 3 and Neutral</td>
    </tr>
    <tr>
        <td>Phase 1 to Phase 2</td>
        <td>Last polled voltage between Line 1 and Line 2</td>
    </tr>
    <tr>
        <td>Phase 2 to Phase 3</td>
        <td>Last polled voltage between Line 2 and Line 3</td>
    </tr>
    <tr>
        <td>Phase 3 to Phase 1</td>
        <td>Last polled voltage between Line 3 and Line 1</td>
    </tr>
    <tr>
        <td>Phase 1 Current</td>
        <td>Last polled current on Line 1</td>
    </tr>
    <tr>
        <td>Phase 2 Current</td>
        <td>Last polled current on Line 2</td>
    </tr>
    <tr>
        <td>Phase 3 Current</td>
        <td>Last polled current on Line 3</td>
    </tr>
    <tr>
        <td>Neutral Current</td>
        <td>Last polled current on Neutral</td>
    </tr>
    <tr>
        <td>Total Active Power</td>
        <td>Last polled active (aka real/true) power</td>
    </tr>
    <tr>
        <td>Total Reactive Power</td>
        <td>Last polled reactive power</td>
    </tr>
    <tr>
        <td>Software Version</td>
        <td>Reported software version</td>
    </tr>
    <tr>
        <td>Serial Number</td>
        <td>Reported serial number</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

[//]: # (Start with a verb such as "Fires when..." or "Receives...")

#### Data Received


Fires when the Controller receives response from a poll.

Trigger variables:

* &nbsp;*Variable 1*: Frequency (Hz) (*number*).
* &nbsp;*Variable 2*: Phase 1 to Neutral Voltage (V) (*number*).
* &nbsp;*Variable 3*: Phase 2 to Neutral Voltage (V) (*number*).
* &nbsp;*Variable 4*: Phase 3 to Neutral Voltage (V) (*number*).
* &nbsp;*Variable 5*: Phase 1 to Phase 2 Voltage (V) (*number*).
* &nbsp;*Variable 6*: Phase 1 to Phase 2 Voltage (V) (*number*).
* &nbsp;*Variable 7*: Phase 3 to Phase 1 Voltage (V) (*number*).
* &nbsp;*Variable 8*: Phase 1 Current (A) (*number*).
* &nbsp;*Variable 9*: Phase 2 Current (A) (*number*).
* &nbsp;*Variable 10*: Phase 3 Current (A) (*number*).
* &nbsp;*Variable 11*: Neutral Current (A) (*number*).
* &nbsp;*Variable 12*: Total active power (W) (*number*).
* &nbsp;*Variable 13*: Total reactive power (VAR) (*number*).

### Actions

[//]: # (Start with a verb such as "Requests..." or "Starts...")

#### Start Poll

Starts background polling of the device.

#### Stop Poll

Stops background polling of the device.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
