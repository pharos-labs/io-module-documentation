# Trigger Lockout - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Sets a trigger lockout state based on momentary events.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Updated Action and state names.
* &nbsp;Added *Lockout State* status variable.
* &nbsp;Added *Unlocked* Condition.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

Set the lockout state using a *Lock Out/Unlock* Action. This state is then used by the *Locked Out* Condition to either fire or prevent a Trigger from firing.

The current state can be seen in the IO Module tab of the web interface.

Triggers without this Condition will not be affected.

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

[//]: # (### Triggers)

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

### Condition

#### Unlocked

Fires the associated Trigger if the lockout state is *Unlocked*. This can also be used in the negated state to allow Triggers to only fire when in the *Locked Out* state.

Triggers without this Condition will not be affected.

#### Locked Out

Fires the associated Trigger if the lockout state is *Locked Out*. This can also be used in the negated state to allow Triggers to only fire when in the *Unlocked* state.

Triggers without this Condition will not be affected.

### Action

#### Lock Out/Unlock

Sets the lockout *State* to *Lockout* or *Unlock*. This status is then used by the *Locked Out* Condition to either fire or prevent a Trigger from firing.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
