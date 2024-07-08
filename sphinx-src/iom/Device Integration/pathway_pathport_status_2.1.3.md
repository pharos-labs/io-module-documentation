# Pathway Pathport Status - Version 2.1.3

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Monitors the online status of Pathport devices by listening to multicast discovery packets.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

#### Version 2.1

* &nbsp;General updates and improvements.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

On startup, the module joins the Pathport Discovery multicast address 239.255.237.2 on port 3792 and listens for the discovery packets. The IO module web interface tab will show the device statistics for each device, which is extracted from the discovery packet.

### Instance Properties

Each device to be discovered requires its own module instance the *IP Address* must be defined.

The *Status Changed Timeout* defines how long to wait before a device is declared as offline, thus firing the *Device Status Changed* Trigger.

Checking the *Extended Logging* checkbox will provide extra log messages for diagnostics. It is recommended that this is disabled during normal operation to maintain controller performance.

### Triggers

#### Device Status Changed

This will automatically fire when a device changes state, from undiscovered or *Offline* to *Online*, or from *Online* to *Offline*, and if the status of the devices matches the *Status* in the trigger properties.

Below is the list of variables this Trigger passes on together with their type in parentheses:

* &nbsp;Device IP Address (*string*)
* &nbsp;Device IP Status ("Undiscovered", "Online", "Offline") (*string*)
* &nbsp;Device Device ID (*string*)
* &nbsp;Device Device Name (*string*)
* &nbsp;Device Last Discovered Time (*string*)

#### Device Status Receive

This will fire in response to a *Get Device Status* action.

Below is the list of variables this Trigger passes on together with their type in parentheses:

* &nbsp;Device IP Address (*string*)
* &nbsp;Device IP Status ("Undiscovered", "Online", "Offline") (*string*)
* &nbsp;Device Device ID (*string*)
* &nbsp;Device Device Name (*string*)
* &nbsp;Device Last Discovered Time (*string*)

### Conditions

#### Device Status

Returns true if the current online status of the devices matched the *Status* property.

### Action

#### Get Device Status

Fires the *Device Status Received* trigger for a given device using data stored within the module.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
