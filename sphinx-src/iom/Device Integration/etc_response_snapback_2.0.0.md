# ETC Response SnapBack - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Interact with an ETC Response SnapBack.

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

* &nbsp;Initial release.

[//]: # (Always required)
*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Module Properties

Set the *Local UDP Port* (default 4703) to that configured on the device for Subscription Devices.\
If Subscription Devices are not used, then this can be ignored.

*Allow Reports From* sets the allowed trigger sources:
<table>
    <style type="text/css">
    td {
        padding: 3 10px;
    }
    </style>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Any source</td>
        <td>Any source reporting with matching <i>Device number</i> will be accepted</td>
    </tr>
    <tr>
        <td>Instances only</td>
        <td>Only sources reporting with with matching <i>IP Address</i> and <i>Device number</i> matching an instance will be accepted</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

### Instance Properties

[//]: # (### List instance properties and their function)

Set the *IP Address*, *UDP Port* (default 4703), and *Device number* to that configured on the device.

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
        <td>Device</td>
        <td>Assigned device number</td>
    </tr>
    <tr>
        <td>Active preset</td>
        <td>Currently active preset number</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

[//]: # (Start with a verb such as "Fires when..." or "Receives...")

#### Preset active

Fires when the device reports an active preset for the instance *Device number*.

Trigger variables:

* *Variable 1*: Device number (*integer*).
* *Variable 2*: Preset (*integer*).
* *Variable 3 (Optional)*: Fade time (seconds) (*number*)

#### Preset recorded

Fires when the device reports an preset has been recorded for the instance *Device number*.

Trigger variables:

* *Variable 1*: Device number (*integer*).
* *Variable 2*: Preset (*integer*).

### Actions

[//]: # (Start with a verb such as "Requests..." or "Starts...")

#### Activate preset

Sends a request to the device to activate *Preset*, with *Fade time*.

#### Record preset

Sends a request to the device to record *Preset*.

#### All off

Sends a request to the device to set all off, with *Fade time*.

#### Contact resync

Sends a request to the device to resync the devices analog inputs.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
