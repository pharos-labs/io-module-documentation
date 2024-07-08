# Network Status Project Touch Device - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Checks if a project Touch Device is online using a Condition and displays the status of a Controller in the web interface.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Added *Touch Device Number* default Instance property.
* &nbsp;Added status variables to show the status of the Instance default *Touch Device*.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

The *Touch Device Number* Instance property specifics a default Touch Device number to monitor. The status of this Touch Device will show in the web interface.
If the *Touch Device Number* in the *Project Touch Device Online* Condition is set to <code>Use Instance Default (0)</code> then the *Touch Device Number* from the Instance properties will be used.

#### Status Variables

* &nbsp;*Default Touch Device Status*

The IO module tab of the web interface provides status variables to show the current online status of the Instance default Touch Device;
whether online, offline or if it does not exist in the project. The status is polled every second.


[//]: # (### List instance properties and their function)

[//]: # (### Triggers)

[//]: # (#### Trigger Name)
[//]: # (#### Start with a verb such as "Fires when..." or "Receives...")

### Conditions

#### Project Touch Device Online

Matches (returns true) if the status of the Touch Device specified by the *Touch Device Number* is online.
If the *Touch Device Number* is set to <code>Use Instance Default (0) </code> then the *Touch Device Number* from the Instance properties will be used.

[//]: # (### Actions)

[//]: # (#### Action Name)
[//]: # (#### Start with a verb such as "Sends..." or "Sets...")

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
