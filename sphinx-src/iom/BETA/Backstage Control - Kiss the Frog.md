# Backstage Control - Kiss the Frog - Version 2.0.0.BETA2

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Integrate with Kiss the Frog MQTT servers.

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

Set the *Controller ID* as required to uniquely identify the controller on the MQTT broker. If omitted then the controller's type and serial number will be used.

Set the *MQTT Broker Hostname* and *MQTT Broker Port* to that configured on the MQTT broker.\
Tick *Use SSL* if the broker requires a SSL/TLS encrypted connection.\
Tick *Verify SSL Certificate* to verify, when using an encrypted connection, that the broker's certificate is valid.

Set the *Username* and *Password* as required.

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

### Instance Properties

[//]: # (### List instance properties and their function)

Set the *Instance ID* as to uniquely identify this instance on the MQTT broker.

*Mode 1* to *Mode 16* are used to assign names to the settable modes, these are use for logging and returned with trigger variables.

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
        <td>Current Mode</td>
        <td>The currently set mode name and mode number</td>
    </tr>
    <tr>
        <td>Current Intensity</td>
        <td>The currently set intensity</td>
    </tr>
    <tr>
        <td>Last Mode Change</td>
        <td>Date and time of the last mode change</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

[//]: # (Start with a verb such as "Fires when..." or "Receives...")

#### Mode changed

Fires when the mode has changed, matching *Mode* or "Any".

Trigger variables:

* &nbsp;*Variable 1*: Mode number /16 (*integer*).
* &nbsp;*Variable 2*: Mode name (*string*).
* &nbsp;*Variable 3*: Source of change ("mqtt" or "internal").

#### Current mode

Fires in response to the action *Get current mode*.

Trigger variables:

* &nbsp;*Variable 1*: Mode number /16 (*integer*).
* &nbsp;*Variable 2*: Mode name (*string*).

#### Intensity changed

Fires when the intensity has changed, matching *Value* or "Any".

Trigger variables:

* &nbsp;*Variable 1*: Intensity value /255 (*integer*).

### Conditions

[//]: # (Start with a verb such as "Matches if...")

#### Mode is

Returns true if *Mode* matches the current mode.

### Actions

[//]: # (Start with a verb such as "Requests..." or "Starts...")

#### Set mode

Changes the current mode to *Mode*.

#### Get current mode

Requests the current mode via the trigger *Current mode*.

#### Set intensity

Changes the current intensity to *Value*.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
