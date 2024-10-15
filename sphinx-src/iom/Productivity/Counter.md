# Counter - Version 2.1.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Fires a trigger once a given number of triggers have been received.

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

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

Use actions to *Incriment* the Counter and fire the *Target* trigger once the target *Count* has been reached.

### Instance Properties

*Count* defines the target Counter value. Once this target is hit, the *Target* trigger will fire.

### Triggers

#### Target

Fires when the *Count* target is reached (from using *Incriemnt* actions). Once the trigger has been fired, the the counter will be reset to 0.

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

### Actions

#### Start

Activates the Counter. Without a *Start* action being called, an *Increment* action will have no effect on the Counter.


#### Stop

Deactivates the Counter. If the *Stop* action has been called, an *Increment* action will have no effect on the Counter.

#### Increment

Adds one to the Counter, if it is active.

#### Reset

Resets the counter back to 0.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
