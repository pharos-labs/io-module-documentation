# Network Connection Status - Version 2.0.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Monitor and report on the network connection status of the primary controller.

[//]: # (Brief description of the module; usually the same as the description in the package)

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)
This IO Module is stable and has been tested internally.

[//]: # (Always required)
If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope
[//]: # (If important to mention explain the limitations and things this module cannot perform)
The module is limited to triggering from events of the management interface on the primary network controller.

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
        <td>First network up event</td>
        <td>Date and time of the first network up event for the management interface on the primary network controller</td>
    </tr>
    <tr>
        <td>Last network up event</td>
        <td>Date and time of the latest network up event for the management interface on the primary network controller</td>
    </tr>
    <tr>
        <td>Last network down event</td>
        <td>Date and time of the latest network down event for the management interface on the primary network controller</td>
    </tr>
    <tr>
        <td>Cycle count</td>
        <td>Number of network up events for the management interface on the primary network controller since boot</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Network Up

[//]: # (Start with a verb such as "Fires when..." or "Receives...")
Fires when the management interface on the primary controller is Up.

If *Only first* is enabled then only the first event after a controller boot with trigger.

Trigger variables:

* &nbsp;*Variable 1*: Is first up event since boot (*boolean*).

#### Network Down

[//]: # (Start with a verb such as "Fires when..." or "Receives...")
Fires when the management interface on the primary controller is Down.

If *Only first* is enabled then only the first event after a controller boot with trigger.

Trigger variables:

* &nbsp;*Variable 1*: Is first down event since boot (*boolean*).

### Conditions

#### Is network up

[//]: # (Start with a verb such as "Matches if...")
Returns true if selected *Interface* on the primary controller is up.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
