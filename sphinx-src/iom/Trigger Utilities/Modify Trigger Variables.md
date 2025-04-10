# Modify Trigger Variables - Version 2.1.2


[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Using Conditions, modifies the value of variables captured by a Trigger before being passed to Actions.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1.2

* &nbsp;Added *Convert Value* Condition.
* &nbsp;Added *Change Range* Condition.
* &nbsp;Fixed to allow division of 0, but disallow division by 0.

#### Version 2.0

* &nbsp;Added *Round* Condition.
* &nbsp;Added *To Integer* Condition.
* &nbsp;Added *To Real* Condition.
* &nbsp;Added *Negate Binary* Condition.
* &nbsp;Added *To String* Condition.
* &nbsp;Added *Prepend/Append To String* Condition.
* &nbsp;Added option to *not* convert to range type.
* &nbsp;Fixed bug to allow script variables to be correctly handled.
* &nbsp;Added logging and error handling.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

All functions are implemented as Conditions, allowing the variables captured by the Trigger to be adjusted before being passed to the Action. As such, if the Condition is set to negate, the Trigger will not fire.

In all modification Conditions, the modified value does not replace the existing variable; it will be added to the end of the Trigger table. In order to confirm the captured and modified variables, check Controllers logs. Multiple Conditions can be used to perform multiple modifications, but a new variable is created each time, so care must be taken with the variable numbers being used.

In all Actions, if the *Range* is set to *Don't Use* (0), the value will be passed to the Action without being converted to a Pharos Range value. Certain Actions such as *Master Intensity* and *Set RGB* will require a *Range* value to convert a Trigger variable to a range value. This can be achieved by setting the *Range* property to greater than 0 (above *Don't Use*).
For information on variant and ranges see help documentation.

**Note:** If you are using multiple Controllers in a project, you will need to ensure that the Trigger has been set to *Test Conditions* on the Controllers that has been set to be the Network Primary in your project.

### Conditions

#### Additions

Adds the *Add* value to the Trigger *Variable* and appends the new value to the end of the Trigger variables.

#### Subtraction

Subtracts the *Subtract* value from the Trigger *Variable* and appends the new value to the end of the Trigger variables.

#### Multiplication

Multiplies the Trigger *Variable* by the *Multiply* value and appends the new value to the end of the Trigger variables.

#### Division

Divides the Trigger *Variable* by the *Divisor* value, and appends the remainder value to end of the Trigger variables table.

#### Remainders

Divides the Trigger *Variable* by the *Divide* value and appends the new value to the end of the Trigger variables.

#### Round

Rounds the Trigger *Variable* number up or down (*Direction*) by the *Decimal Places* value and appends the new value to the end of the Trigger variables.

#### Change Sign

Changes the *Sign* of the Trigger *Variable* and appends the new value to the end of the Trigger variables. If the sign of the Trigger variable matches the *Sign* property, the sign will not be changed.

#### To Integer

Converts Trigger *Variable* from a string or real (float) number to an integer and appends the new value to the end of the Trigger variables. If the Trigger variable is a real (float) or a string containing a real number, the number will be rounded down to the closest whole number.

#### To Real

Converts Trigger *Variable* from a string or integer to a real (float) number and appends the new value to the end of the Trigger variables. If the Trigger variable is an integer or a string containing an integer number, type of the new Trigger variable will be in real number format.

#### Negate Binary

Converts Trigger *Variable* from a 0 to a 1 or a 1 to a 0 appends the new value to the end of the Trigger variables. If the variable is not a 0 or 1, an error will be logged.

#### To String

Converts Trigger *Variable* from any type to a string and appends the new value to the end of the Trigger variables.

#### Prepend/Append To String

Adds the *String* to before (*Prepend*) or after (*Append*) Trigger *Variable* and appends the new value to the end of the Trigger variables.

#### Convert Value

Converts the Trigger *Variable* number to a percentage, 8-bit number or a float between 0-1 and appends the new value to the end of the Trigger variables.

#### Change Range

Changes the Trigger variable range of the Trigger *Variable* number and appends the new value to the end of the Trigger variables. This applies to integers only.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
