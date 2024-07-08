# Network Status Project Controller - Version 2.0.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Checks if a project Controller is online using a Condition and displays the status of a Controller in the web interface.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0.1

* Fix functionality for newer Designer versions

#### Version 2.0

* Added *Controller Number* default Instance property.
* Added status variables to show the status of the Instance default *Controller*.
* Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

The *Controller Number* Instance property specifics a default Controller number to monitor. The status of this Controller will show in the web interface.
If the *Controller Number* in the *Project Controller Online* Condition is set to <code>Use Instance Default</code> then the *Controller Number* from the Instance properties will be used.

#### Status Variables

* &nbsp;*Default Controller Status*

The IO module tab of the web interface provides status variables to show the current online status of the Instance default Controller;
whether online, offline or if it does not exist in the project. The status is polled every second.


[//]: # (### List instance properties and their function)

[//]: # (### Triggers)

[//]: # (#### Trigger Name)
[//]: # (#### Start with a verb such as "Fires when..." or "Receives...")

### Conditions

#### Project Controller Online

Matches (returns true) if the status of the Controller specified by the *Controller Number* is online.
If the *Controller Number* is set to <code>Use Instance Default</code> then the *Controller Number* from the Instance properties will be used.

[//]: # (### Actions)

[//]: # (#### Action Name)
[//]: # (#### Start with a verb such as "Sends..." or "Sets...")

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
