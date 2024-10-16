# Nth Weekday - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Fires a Trigger on the Nth weekday of a month e.g. "First Thursday", "Third Wednesday", "Last Sunday" etc.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Added status variable to show the current day's monthly occurrence.
* &nbsp;Checks Trigger on Controller time change.
* &nbsp;Added "Log Today's Occurrence" Instance property.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

See the IO Modules tab of the web interface for the current date's Nth day format ie. <code>Today is the fourth (last) Monday of the month</code>.

### Instance Properties

The *Daily Trigger Time* is the time at which the trigger, if matched, will fire.

If *Log Today's Occurrence* is checked, the current Nth day format ie. <code>Today is the fourth (last) Monday of the month</code>
will be logged at the *Daily Trigger Time*, if the Controller's time is changed or if a *Is Nth Weekday* Condition is _not_ met.

[//]: # (### Triggers)

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

### Trigger

#### Nth Weekday

Fires at midnight if *Occurrence* of the *Weekday* matches today's date. The trigger will also fire if the Controller's time is changed.

### Condition

#### Is Nth Weekday

Is met if the *Occurrence* of the *Weekday* matches today's date.

If *Log Today's Occurrence* is checked, the current Nth day format ie. <code>Today is the fourth (last) Monday of the month</code>
if a *Is Nth Weekday* Condition is _not_ met.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
