# Ramp Timeline Rate - Version 2.1.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Ramps up or down the timeline rate over a given time

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

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

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

[//]: # (### Instance Properties)

[//]: # (Describe relevant instance properties if there are any beyond the name)

[//]: # (### Triggers)
[//]: # (An event received by the controller that can be acted upon to create a reaction)

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

### Actions
#### Ramp Timeline Rate

Changes the rate of a specified *Timeline* from the *Start Rate* to the *End Rate* over the specified *Time*. The *Start Rate* must be specified and does not take in to consideration the current timeline rate. If *End Rate* is set to 0, once reached, the timeline will seemingly stop; it will not be released but will instead be running but with a rate of 0.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
