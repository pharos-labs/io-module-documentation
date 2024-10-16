# Raritan PX IP PDU Outlet Control - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Controls outlets of a Raritan PX IP PDU using SNMPv2c.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Added status variable for *Last Command Sent* and *Last Response*.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Set the *Hostname* (either the IP address or DNS name) and SNMP *Community String* to that of the Raritan RX device.

### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Last Command Sent&nbsp;&nbsp;&nbsp;</td>
        <td>Last command sent from a Switch Outlets Action.</td>
    </tr>
    <tr>
        <td>Last Response</td>
        <td>The last response message from the device or an error message.</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Actions

#### Switch Outlets

Sends a command to the Raritan RX device to set the *Outlets* to the *State*; <code>On</code>, <code>Off</code> or <code>Cycle</code>.

The *Outlets* are defined in comma-dash format, for example <code>1,3,5</code> or <code>1-5,7-9</code>.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
