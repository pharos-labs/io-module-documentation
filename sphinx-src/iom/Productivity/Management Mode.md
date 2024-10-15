# Management Mode - Version 2.2.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Creates up to 16 custom Modes per instance and control which mode your Controller is in.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.2

* &nbsp;Added support for using variable in Set Mode action, in the format "Mode x", the mode number as a string or the mode name (exact match).
* &nbsp;Updated documentation.

#### Version 2.1

* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;Initial release.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

This IO Module allows up to 16 possible different Modes for the Controller per instance of this IO Module. Only one Mode can be set at any one time per instance.

### Instance Properties

Specify a *Name* for the set of Modes contained within the created instance of this IO Module. **Note: Mode names _must_ be valid (not blank) to be used in the module and _can not_ be updated dynamically using Triggers or Actions.**

In Triggers, Actions and Condition, the modes are defined in the format <code>Mode XX</code> but are mapped to the Modes names during operation.

Checking the *Extended Logging* checkbox will provide more detailed log messages for fired Triggers, Conditions and Actions.

### Triggers

#### Mode Changed

Fires when the Mode has been changed from a *Change Mode* Action, to that specified within the *Mode Changed* Trigger for a given selected *IO module instance*.

#### Current Mode Received

Fires in response to the *Get Current Mode* Action, passing the name (as a *string*) and number (as an *integer*) of the current *Mode* as variables.

This Trigger will only receive the current Mode information if the Trigger's *IO module instance* matches that set for the executed *Get Current Mode* Action.

### Conditions

#### Mode Is

Returns true if the current mode matched the Condition *Mode* for a given Instance.

Checking the *Negate* checkbox will reverse the Condition allowing it to pass for all Modes _except_ the selected *Mode* for a given instance.

### Actions

#### Change Mode

Changes the Controller's Mode to that specified by the *Mode*. Ensure the *IO module instance* with the desired Mode specifications has been also selected.

A Trigger variable string identifying a Mode name can be used to change the mode. The variable can be in the format <code>Mode X</code>, the Mode index (as a string) or the Mode name (exact match).

#### Get Current Mode

Fires the *Current Mode Received* Trigger, passing the Mode name (as a *string*) and number (as an *integer*) as Trigger.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
