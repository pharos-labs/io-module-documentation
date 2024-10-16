# Start Random Timeline or Scene - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Starts a random scene or timeline

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (#### Module Scope)
[//]: # (TODO)

### Release Notes

#### Version 2.0

* &nbsp;Added *Last Timelines Started* status variable.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

### Instance Properties

Define the *Timelines and Scenes* set in comma-dash format, eg. <code>t1-4,8,10</code>, using <code>t</code> for timelines and <code>s</code> before the respective numbers.
The set can be entered as a continuous range <code>t1-5</code>, discrete entries <code>t1,t2,s10,23</code>, or a combination <code>t1-4,s8,t10</code>.

If *Force All to Play Once* is enabled, this will ensure that all Timelines and Scenes in the set will played at least once (in a random order) before any Timeline or Scene is repeated.

If *Release Previous* is checked, all previously running Scenes and Timelines will be released.

Checking the *Extended Logging* checkbox will provide more detailed log messages for actions.
This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

### Actions

#### Start Random Timeline or Scene

Starts a random Timeline or Scene from the specified instance *Timelines and Scenes* set.

[//]: # (#### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

### Support

If you encounter any issues with this module, please contact our support team.

[//]: # (#### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (#### Further Notes)
[//]: # (Possible location for further notes, may not be used)
