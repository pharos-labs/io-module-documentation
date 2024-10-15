# C-Bus (Serial) - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Sends commands to a C-Bus system via a C-Bus PCI.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Added *Extended Logging* Instance property.
* &nbsp;Added extra error checking.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Set the *Serial Port* to that configured in the Network tab. The following settings should be used:

* Mode: RS232
* Baud Rate: 9600
* Data Bits: 8
* Parity: None
* Stop Bits: 1

The *Lighting Application Address* is defined in decimal format and converted to its hex equivalent when a command is sent e.g. Address <code>$38</code> would be set here as <code>56</code>.

Checking the *Extended Logging* checkbox will provide more detailed communication logs message. This is for diagnostic purposes and should be disabled during running to maintain controller performance.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Last Command Sent&nbsp;&nbsp;&nbsp;</td>
        <td>Last C-Bus message sent.</td>
    </tr>
        <tr>
        <td>Last Response Received&nbsp;&nbsp;&nbsp;</td>
        <td>Last response from the C-Bus system, either a confirmation or error.</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Actions

#### Set Group On

Sets the *Group* on the C-Bus system (in decimal format) to on.

#### Set Group Off

Sets the *Group* on the C-Bus (in decimal format) system to off.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
