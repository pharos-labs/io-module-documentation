# Repeat - Version 2.2.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Fires another Trigger, waits a specified delay time before firing the Trigger a specified number of times.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Release Notes

#### Version 2.2

* &nbsp;Added *Repeat Ended* Trigger.
* &nbsp;Added *Occurrence as Trigger Variable* instance option.
* &nbsp;Added *Log Trigger Fire* instance option.
* &nbsp;Bug fixes.

#### Version 2.1

* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;General updates and improvements.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

#### Instance Properties

The *Trigger Number* specifies which Trigger to fire.

The *Delay* is the time in seconds between occurrences of the Trigger being fired.

*Occurrences* specifies how many times to fire the Trigger. Setting this to 0 will cause the repeat to continue indefinitely or until the *Stop Repeat* action is called. Setting this to 1 will immediately fire the Trigger *Start Repeat* but will not repeat.

*Count Direction* determines how the number of Triggers already fired will be displayed in the status variables eg. count *Up* from 1 to 10 or count *Down* from 10 to 1. The status variables will also show the last system time a Trigger was fired.

If *Occurrence as Trigger Variable* is enabled, the occurrence number will be passed as a Trigger variable to the fired Trigger.

If *Log Trigger Fire* is enabled, the Trigger number and occurrence number will be printed to the log (alongside the usual Trigger log messages).

#### Triggers

##### Repeat Ended

Fires when all occurrences of the repeating Trigger have fired.

#### Actions

##### Start Repeat

Fires the Trigger immediately and then starts the repeating from the count specified in the *Occurrences* instance property. If the repeating has already started, it will be restarted at the count specified in the *Occurrences*.

##### Stop Repeat

Stops and cancels the repeating and can be called at any time in the repeating process. The *Start Repeat* action can be called to restart repeating.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
