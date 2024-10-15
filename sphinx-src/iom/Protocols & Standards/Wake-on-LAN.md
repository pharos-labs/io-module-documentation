# Wake-on-LAN - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Sends Wake-on-LAN Magic Packets to other IP devices on the network.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Updated documentation.
* &nbsp;Added status variables.
* &nbsp;Added logging option.
* &nbsp;Bug fixes.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

[//]: # (### Instance Properties)

[//]: # (Describe relevant instance properties if there are any beyond the name)

[//]: # (### Triggers)
[//]: # (An event received by the controller that can be acted upon to create a reaction)

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

### Actions

#### Send Wake Up

Sends Wake-on-LAN packets to the target device.

The *Target MAC Address*, *Target Port* and *Broadcast Address* must be set accordingly for the remote device to be able to receive the Wake-on-LAN packets.

*Device Name* is optional but is useful for viewing in the log and on the web interface.

*Packets to Send* is the number of Wake-on-LAN packets to send. Typically, 1 will suffice, but multiple can be used for redundancy.

If *Log* is enabled, Wake-on-LAN send actions and results will appear in the log. This can be used for fault finding or can be disabled to reduce the number of log messages being viewed.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
