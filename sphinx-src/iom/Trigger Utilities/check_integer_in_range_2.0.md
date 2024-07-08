# Check Integer in Range - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Checks whether a captured variable is within a specified range.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Extra error handling.
* &nbsp;Parses integer-format strings as integers.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

[//]: # (### Instance Properties)

[//]: # (### Triggers)

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

### Conditions

#### Integer in Range

Returns true if the value of the Trigger *Variable* matchs the values wittin the *Range*.
The *Range* is defined in comma-dash format, either using ranges of number or discrete values for example: <code>1-5,11,13,21-25</code>.

Example:

<code>Trigger 1</code>: Digital Input - Any - Low, </code>Condition</code>: *Integer in Range* - *Variable* <code>1</code>, *Range* <code>1-4</code>, <code>Action</code>: Start Timeline from Variable 1

The above trigger would start any timeline between 1 and 4 using the matching Digital Input, but the not Timelines 5-8.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
