# Pulse Digital Output - Version 2.1.0



[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Pulses a RIO's digital output a specified number of times.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1

* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;Added *Pulse State* property to *Start Pulse* action, to define whether the pulse sets the output to *High* or *Low*.
* &nbsp;Added *End State* property to *Start Pulse* action, to define whether the output is *High*, *Low*, or *Restored* on completion of the pulse cycle.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Select the *Device* and the digital *Output* number to be pulsed. If multiple outputs are to be controlled, create a new module instance for each.

[//]: # (### Triggers)
[//]: # (An event received by the controller that can be acted upon to create a reaction)

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)
### Actions
#### Enable Pulse

Starts the pulsing cycle. Set *Duration* to the time in which the *Output* is held at the *Pulse State* (default *High*) and the *Period* to the total cycle time (including the *Duration* time) between pulses. *End State* defines whether the *Output* at the end of the total pulse cycle should be *High* or *Low* (default *Low*), or whether to *Restore Previous State* (the state in which is the *Output* was in before the *Enable Pulse* action was called).

Set *Count* to the number of times to repeat a single pulse cycle. If set to *Infinite* (0), the pulsing will continue until the *Disable Pulse* action is called.

#### Disable Pulse

Stops the pulsing cycle immediately, leaving the *Output* in it's current state.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
