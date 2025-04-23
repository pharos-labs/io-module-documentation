# Wait - Version 2.5.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Enables a trigger to fire after a specified time delay, on a per-instance basis.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.5
* &nbsp;Improved timer management

#### Version 2.4.1
* &nbsp;Add time remaining triggers option.
* &nbsp;Improved handling of floating point wait times passed as variables.

#### Version 2.3

* &nbsp;Added option to display Actions in the log.
* &nbsp;Fixed potential memory leak bug.
* &nbsp;Fixed display of decimal wait times in status variables and log messages.

#### Version 2.2

* &nbsp;Removed previously fired waits from *Current Waits* status variable, and added *Last Fired* status variable.

#### Version 2.1

* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;Added *Cancel Waits* action to cancel all Waits within a given instance.
* &nbsp;Added *Current Waits* status variable to view the status of enqueued Waits.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

Use the *Wait* action to enqueue a trigger. The *Trigger* will fire independently of others, after the specified delay in *Seconds*, once a *Wait* action has been called. Any number of Waits can exist in one instance so if individual control of a Wait stack is required, create a new instance. The *Cancel Waits* action will cancel all Waits within a given instance.

The variables present when the *Wait* action is fired, are copied to the resultant trigger.

### Instance Properties

If *Log Actions* is checked, log messages will be displayed for new *Wait* Actions, completed waits and *Cancel Waits* Actions.

[//]: # (### Triggers)

[//]: # (### Conditions)

### Actions

#### Wait

Fires the *Trigger* after the specified wait time in *Seconds* time. Multiple Waits can be used within one instance and will all fire independently of each other. The IO Module tab in the web interface will show the enqueued Waits with a countdown for each. To cancel all Waits within an instance, use the *Cancel Waits* action.

An optional *Countdown Trigger Number* can be set to, this trigger will be called frequently with the last variable set to the remaining wait time.

#### Cancel Waits

Stop and cancels all Waits enqueued by *Wait* actions, on a per-instance basis.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
