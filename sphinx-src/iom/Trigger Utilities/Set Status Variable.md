# Set Status Variable - Version 2.1.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Sets a status variable value in IO Module tab of the web interface.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1

* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (Provide a history of the release updates to the module for the end user)

[//]: # (### Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (### Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

Each instance holds one value/status variable and an instance can be created for each value/status variable required. When the *Set Value* action is called, it will set the *Value* of the instance and displays it in the IO Module tab of the web interface. Using *Get Value* will fire the *Value Received* trigger (if one exists), passing the value as a trigger variable.

### Triggers

### Value Received

Fires when the *Get Value* action is called. The instance value will be passed to this trigger as a trigger variable.

[//]: # (An event received by the controller that can be acted upon to create a reaction)

[//]: # (#### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

### Actions

#### Set Value

Sets the *Value* of the instance and displays it in the IO Module tab of the web interface.

#### Get Value

Fires the *Value Received* trigger (if one exists), passing the instance value as a trigger variable.

[//]: # (#### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (#### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (#### Further Notes)
[//]: # (Possible location for further notes, may not be used)
