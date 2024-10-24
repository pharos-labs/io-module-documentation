# Stopwatch - Version 2.1.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Runs a Stopwatch and allows for firing of triggers on elapsed times.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1

* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;General updates and improvements.
* &nbsp;Updated module documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

*Time Format* specifies the unit of time to be used for triggering, the trigger variable after calling a *Stop* action, and how the time is displayed in the web interface.

### Triggers

#### Time Elapsed

Fires when the current Stopwatch elapsed time is equal to the *Time Elapsed* trigger property, passing the *Time Elapsed* as trigger variable 1 (*real number*) (units as set in the *Time Format* instance property.)

#### Started

Fires when the Stopwatch is started by the *Start* or *Restart* action, but not *Resume*. There are no trigger variables associated with the *Started* trigger.

#### Stopped

Fires when the Stopwatch is stopped by the *Stop* or *Reset* action, but not *Pause*, capturing the time at which is was stopped as trigger variable 1 (*real number*) (units as set in the *Time Format* instance property.)

### Conditions

#### Is Running

Will return true if the Stopwatch is in a running state (not stopped or paused).

### Actions

#### Start

Begins the Stopwatch running and will fire the *Started* trigger.

#### Pause

Stops the Stopwatch but the *Stopped* trigger is **not** fired.

#### Resume

Restarts the Stopwatch if it is currently stopped, but will **not** fire the *Started* trigger. If the Stopwatch has not begun, *Resume* will act the same as the *Start* (but will still **not** fire the *Started* trigger).

#### Stop

Stops the Stopwatch and fires the *Stopped* trigger. The elapsed time is not reset.

#### Restart

Resets the elapsed time, begins the Stopwatch running and will fire the *Started* trigger. If any *Time Elapsed* triggers have already been fired, they will fire again.

#### Reset

Stops the Stopwatch, resets the elapsed time, and fires the *Stopped* trigger.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
