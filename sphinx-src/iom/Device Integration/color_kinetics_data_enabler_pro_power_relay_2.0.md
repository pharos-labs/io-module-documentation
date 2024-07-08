# Color Kinetics Data Enabler Pro Power Relay - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Control the Power relay within a PCK Data Enabler Pro.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Added status variables.
* &nbsp;Improved logging.
* &nbsp;Added *Log Actions* and *Extended Logging* options.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

One instance is required for each Data Enabler Pro to be controller, defined by its *IP Address*.

The *Retries* property is number of times to send a status query to check that the setting has been correctly applied.

Checking *Log Actions* will provide log messages when module Actions are called and whether the action was verified successful.

Checking *Extended Logging* will provide more detailed logs on communication between the Controller and the Data Enabler.
This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>IP Address&nbsp;&nbsp;&nbsp;</td>
        <td>The IP address of the Data Enabler Pro set in the instance properties.</td>
    </tr>
    <tr>
        <td>Last Action&nbsp;&nbsp;&nbsp;</td>
        <td>The last Action called.</td>
    </tr>
    <tr>
        <td>Last Command Sent&nbsp;&nbsp;&nbsp;</td>
        <td>The last command sent to the Data Enabler pro. This may be different from the last action for example in the case of sending a query following a request to change state.</td>
    </tr>
    <tr>
        <td>Last Status&nbsp;&nbsp;&nbsp;</td>
        <td>A description of how the success of the request based on the response received.</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Actions

#### Set Power

Sends a command to the Data Enabler Pro to set its power setting to the *Action* specified.

#### Turn Off After No Data

Sends a command to the Data Enabler Pro to turn off the power relay when no data has been received after the *Timeout* period.

#### Turn Off After Black Data

Sends a command to the Data Enabler Pro to turn off the power relay when all channels are set to 0, after the *Timeout* period.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
