# Syslog - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Sends a custom Syslog messages to a Syslog server.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Added *Log Send Actions* instance property.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Define the *Hostname* and *Port* of the remote Syslog server.

The *Origin* and *Tag* options are meta data send with the Syslog message. They can be left empty but can not contain spaces.

If *Log Send Actions* is checked, outgoing Syslog messages will be show in the Controller log, otherwise they will be sent silently.

[//]: # (### Triggers)
[//]: # (An event received by the controller that can be acted upon to create a reaction)

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

### Actions

#### Send Syslog

Sends the Syslog *Message* to the server specified in the instance properties.
The *Severity* and *Facility* properties are meta data values sent with the message for the server to determine
how to display the message.
They can be left as the default <code>*Informational*</code> and <code>local use 0 (local0)</code> respectively.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
