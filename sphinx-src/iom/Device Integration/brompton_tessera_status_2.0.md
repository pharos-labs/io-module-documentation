# Brompton Tessera Status - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Monitors the online status of Brompton Tessera Processors on a network.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Added *Extended Logging* option.
* &nbsp;Added Status Variables.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

The Processor *IP Address* is required and the module will monitor for presence of a Processor at that address.

The *Serial Number* and *Project File Name* are optional, but are recommend to better identify the Processor and the project.
If the *Serial Number* and *Project File Name* are left blank then the module may match any Tessera Processor.

### Status Variables

The IO Modules tab of the web interface provides Status Variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>IP Address</td>
        <td>The IP address of the Brompton Processor as specified in the Instance properties</td>
    </tr>
    <tr>
        <td>Serial Number</td>
        <td>The serial number of the Brompton Processor as specified in the Instance properties</td>
    </tr>
    <tr>
        <td>Project File Name</td>
        <td>The project file name as specified in the Instance properties</td>
    </tr>
    <tr>
        <td>Online Status</td>
        <td>Shows whether the Processor is online or offline</td>
    </tr>
    <tr>
        <td>Last Status Change</td>
        <td>Timestamp of when the status last changed</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Tessera Discovery Online

Fires when the Instance Tessera Processor is detected as online.

#### Tessera Discovery Offline

Fires when the Instance Tessera Processor is detected as offline.

[//]: # (#### Trigger Name)
[//]: # (#### Start with a verb such as "Fires when..." or "Receives...")

[//]: # (### Conditions)

[//]: # (#### Conditions Name)
[//]: # (#### Start with a verb such as "Is met when..." or "Returns true if...")

[//]: # (### Actions)

[//]: # (#### Action Name)
[//]: # (#### Start with a verb such as "Sends..." or "Sets...")

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
