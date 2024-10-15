# Controller HTTP API Client Commands - Version 2.1.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Controls a Project from another Project using the Controller HTTP API.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1

* Support for Controllers with security enabled.

#### Version 2.0

* Updated documentation.
* General updates and improvements.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Set the *Destination Controller IP Address* and *Destination Port* to the Controller with the Project to control.

If the destination Controller has security enabled, then the *Username* and *Password* should be set, if the *Username* is omitted then the *Password* is ignored.

Ticking *Use SSL* will attempt to use encrypted HTTPS with the Controller. n.b. You may need to set the matching *Destination Port*, normally <code>443</code>.

[//]: # (### Triggers)

[//]: # (### Conditions)

[//]: # (#### Conditions Name)
[//]: # (#### Start with a verb such as "Is met when..." or "Returns true if...")

### Actions

#### Release Timeline

Sends a request to the remote Controller to release the *Timeline Number* over the *Fade Time* in seconds.

#### Release Scene

Sends a request to the remote Controller to release the *Scene Number* over the *Fade Time* in seconds.

#### Release All Timeline

Sends a request to the remote Controller to release all Timelines over the *Fade Time* in seconds.

#### Release All Scenes

Sends a request to the remote Controller to release all Scenes over the *Fade Time* in seconds.

#### Toggle Timeline

Sends a request to the remote Controller to toggle the state of the *Timeline Number* over the *Fade Time* in seconds.

#### Toggle Scene

Sends a request to the remote Controller to toggle the state of the *Scene Number* over the *Fade Time* in seconds.

#### Pause Timeline

Sends a request to the remote Controller to pause the *Timeline Number*.

#### Resume Timeline

Sends a request to the remote Controller to resume the paused *Timeline Number*.

#### Pause All

Sends a request to the remote Controller to pause all Timelines.

#### Resume All

Sends a request to the remote Controller to resume all paused Timelines.

#### Set Timeline Rate

Sends a request to the remote Controller to set the *Rate* (as a percentage) of the *Timeline Number*.

#### Enqueue Trigger

Sends a request to the remote Controller to enqueue *Trigger Number* with the option to *Test Conditions*.

#### Run Script

Sends a request to the remote Controller to run the *Script* text as lua code.

#### Hardware Reset

Sends a request to the remote Controller to execute a hardware reset.

#### Master Intensity (Non VLC)

Sends a request to the remote Controller to set the master intensity of the *Group Number* to the *Level* as a percentage,
with a *Fade* and *Delay* in seconds.

#### Master Intensity (VLC)

Sends a request to the remote Controller to set the master intensity of a content target (*Type*) to the *Level* as a percentage,
with a *Fade* and *Delay* in seconds.

#### Set RGB

Sends a request to the remote Controller to set the *Target* fixture or group *Intensity*, *Red*, *Green*, *Blue* values with an optional *Path*.

#### Clear RGB

Sends a request to the remote Controller to clear all RGB values for the *Target* fixture or group over the *Fade* in seconds.

#### Park Channel

Sends a request to the remote Controller to park the channels in the *Channel List* on a given universe (specified by the *Universe Key*) to the *Level* as an 8-bit value.

#### Unpark Channel

Sends a request to the remote Controller to un-park any parked channels in the *Channel List* on a given universe (specified by the *Universe Key*).

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
