# Random Trigger - Version 2.3.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Enqueues a random trigger from a selection.

## Module Status

[//]: # (If still desired provide a status of the module)

This IO Module is stable and has been tested internally.

[//]: # (#### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

#### Release Notes
##### Version 2.3

* &nbsp;Added default *Triggers* instance property.
* &nbsp;Added *Last Trigger Fired* instance property.

##### Version 2.2

* &nbsp;Updated documentation.

[//]: # (Provide a history of the release updates to the module for the end user)

[//]: # (### Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (### Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

When the *Enqueue Random Trigger* Action is called, a random Trigger will be played from the user-specified selection defined within the Action.

### Instance Properties

Define the *Triggers* to enqueue from the *Enqueue Random Trigger* action in comma-dash format, eg <code>1-4,8,10</code>.
If *Triggers* are specified in the action, the action's *Triggers* will be used (instance defaults will be overridden), otherwise the instance *'Triggers* will be used.

[//]: # (#### Triggers)
[//]: # (An event received by the controller that can be acted upon to create a reaction)

[//]: # (#### Conditions)
[//]: # (Conditions are other criteria that need to be met after a Trigger to activate an Action)

### Actions
#### Enqueue Random Trigger

Enqueues (fires) a trigger at random from the *Triggers* selection, defined in comma-dash format, eg. <code>1-4,8,10</code> .
If *Triggers* are specified in the action, the action's *Triggers* will be used (instance defaults will be overridden),
otherwise the instance *Triggers* will be used.


[//]: # (#### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (#### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (#### Further Notes)
[//]: # (Possible location for further notes, may not be used)
