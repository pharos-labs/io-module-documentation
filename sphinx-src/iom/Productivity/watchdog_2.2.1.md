# Watchdog - Version 2.2.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Fires a trigger if no tickle action happens within a defined length of time.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1

* &nbsp;Added options to log Triggers and Actions.

#### Version 2.1

* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;Extended *Timeout* to two days.
* &nbsp;Added status variable.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

**Note** This is a user-defined Watchdog and does not relate to a hardware Watchdog. The Watchdog must be "tickled" using the *Tickle* action to remain active.

### Instance Properties

*Timeout* defines how long to wait without being "tickled" before firing the *Timeout* trigger, in seconds. The maximum is two days.

### Triggers

#### Timeout

Fires when the Watchdog *Timeout* reaches zero. When a *Tickle* action is called, the Watchdog timer will be reset to the *Timeout* instance property. The countdown/current status can be viewed in the IO Module tab of the web interface.

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

### Actions

#### Start

Begins the Watchdog timer. If the Watchdog timer has already begun, the *Start* action will reset the Watchdog timer will be reset to the *Timeout* instance property value. The countdown/current status can be viewed in the IO Module tab of the web interface.

#### Stops

Cancels the Watchdog timer. The Watchdog can be restarted using the *Start* action.

#### Stops

Resets the Watchdog timer to the *Timeout* instance property value. If the Watchdog timer has already begun, the *Tickle* action will start the Watchdog timer.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
