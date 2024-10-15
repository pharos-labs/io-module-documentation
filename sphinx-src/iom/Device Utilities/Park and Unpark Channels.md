# Park and Unpark Channels - Version 2.0.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Parks and Unparks output channels for a given Universe or EDN port.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Added option to select the Controller on which to park channels.
* &nbsp;Added status variables for currently parked channels.
* &nbsp;Added extra Actions to support EDN.
* &nbsp;Added *Extended Logging*.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation



[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Checking the *Extended Logging* checkbox will provide more detailed error messages.

[//]: # (### Triggers)

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

### Actions

#### Park Channels [Protocol]

Sets the selected *Channels* in a specified *Universe* to the 8-bit *Level* and captures control of those *Channels*.
The levels cannot then be controlled elsewhere until an *Unpark Channels \[Protocol\]* action is used on the selection.

Set the *Protocol* type and *Universe* number, and DMX/eDMX *Channels* in comma-dash format for example: <code>1-5,11,13,21-25</code>.
All *Channels* in the selection will be parked at the same *Level* value.

**Note:** *Channels* refers to DMX addresses, not fixture numbers.

If an invalid Universe or channel is specified, a log message will be displayed.

#### Unpark Channels [Protocol]

Releases control of selected *Channels* in a specified *Universe*.

Set the *Protocol* type and *Universe* number, and DMX/eDMX *Channels* in comma-dash format for example: <code>1-5,11,13,21-25</code>.

**Note:** *Channels* refers to DMX addresses, not fixture numbers.

If an invalid *Device Number* or *Port Number* is specified for that *Type* of device, a log message will be displayed.

#### Park Channels [EDN]

Sets the selected *Channels* on a specified *Port* of an EDN to the 8-bit *Level* and captures control of those *Channels*.

The levels cannot then be controlled elsewhere until an *Unpark Channels \[EDN\]* action is used on the selection.

Set the *Protocol* type and *Universe* number, and DMX/eDMX *Channels* in comma-dash format for example: <code>1-5,11,13,21-25</code>.
All *Channels* in the selection will be parked at the same *Level* value.

**Note:** *Channels* refers to DMX addresses, not fixture numbers.

The *Type* and *Device Number* must match a physically device on the network.
If an invalid *Device Number* or *Port Number* is specified for that *Type* of device, a log message will be displayed.

#### Unpark Channels [EDN]

Releases control of selected *Channels* on a specified *Port* of an EDN.

Define *Channels* in comma-dash format for example: <code>1-5,11,13,21-25</code>.

**Note:** *Channels* refers to DMX addresses, not fixture numbers.

The *Type* and *Device Number* must match a physical device on the network.
If an invalid *Device Number* or *Port Number* is specified for that *Type* of device, a log message will be displayed.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
