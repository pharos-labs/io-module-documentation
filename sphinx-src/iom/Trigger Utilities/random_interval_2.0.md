# Random Interval - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Fires a trigger at random intervals.

## Module Status

[//]: # (If still desired provide a status of the module)

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (#### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Updated documentation.
* &nbsp;General updates.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (### Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (### Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

This IO Module works by specifying a time frame (in the Instance Properties) within which the *Random Interval* Trigger can randomly fire.
Once enabled from an *Enable Random Interval* action, the *Random Interval* trigger will begin to fire.

### Instance Properties

The *Minimum Interval* and *Interval Range* specify the minimum and maximum time within which the *Random Interval* Trigger will fire.
A numeric *Seed* value can be specified for the random generator to use; this can be any value between 1 and 999999 but can be left as default *1*.

Check the *Repeating* checkbox to allow the *Random Interval* Trigger to continue firing indefinitely once it has been enabled by the *Enable Random Interval* action, otherwise it will fire once when the *Enable Random Interval* action is run.

### Triggers

#### Random Interval

Fires after the random interval time expires.

If the *Repeating* checkbox is ticked in the Instance Properties this Trigger will continue firing at random. If not, then this Trigger will only fire once.

[//]: # (#### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

### Actions

#### Enable Random Interval

Enables the *Random Interval* trigger to begin firing.

#### Disable Random Interval

Disables (cancels) the *Random Interval* Trigger from firing.

If *Repeating* is checked in the instance properties, the trigger will continue being fired until this action is run.

[//]: # (#### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (#### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (#### Further Notes)
[//]: # (Possible location for further notes, may not be used)
