# Pad Trigger Variables - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Pads a variable passed from the Trigger with a specified character to a specified length of string.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

[//]: # (### List instance properties and their function)

[//]: # (### Triggers)

[//]: # (#### Trigger Name)
[//]: # (#### Start with a verb such as "Fires when..." or "Receives...")

### Condition

#### Pad Variable

Pads the captured Trigger *Variable* with the *Character* to a given *Total Length*.
The length is the sum of the initial variable and the padded characters.
Set *Pad Position* to either <code>Left</code> (before) or <code>Right</code> (after) of the Trigger variable.

The new, padded variable is added to the end of the variables table and does not replace the initial value.
If the variable can not be found, the Condition will return false.

Only one character is allowed as the padding character, per Condition.

If this is used with the Web Interface, or enqueuing the Trigger, care should be taken to test the Conditions on the Trigger.

[//]: # (### Actions)

[//]: # (#### Action Name)
[//]: # (#### Start with a verb such as "Sends..." or "Sets...")

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
