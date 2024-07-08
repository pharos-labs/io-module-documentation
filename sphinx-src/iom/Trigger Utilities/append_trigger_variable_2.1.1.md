# Append Trigger Variable - Version 2.1.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Adds a Variable to the end of the variables captured by a trigger.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1.1

* &nbsp;Updated documentation.
* &nbsp;Adds action "Append Group Master Intensity"

#### Version 2.0

* &nbsp;General updates and improvements.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

This module uses a condition to allow variables to be added to the end of the trigger variables.

The variable is added after any captured variables, so care should be taken with variable numbering in the action/s.

If this is used with the Web Interface or enqueuing the trigger, then care should be taken to test the conditions on the trigger.

### Conditions

#### Append String

Adds a string to the end of the trigger variables.

### Append Integer

Add an integer the end of the trigger variables.

#### Append Float

Adds a float to the end of the trigger variables.

#### Append Boolean

Adds a boolean to the end of the trigger variables; *1* for true and *0* for false.

#### Append Group Master Intensity

Adds the master intensity level of group number *Group*.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
