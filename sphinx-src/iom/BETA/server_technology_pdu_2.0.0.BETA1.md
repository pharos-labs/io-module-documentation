# Server Technology PDU - Version 2.0.0.BETA1

## Module Summary

Control and monitor Server Technology PDUs using JSON API Web Service (JAWS).

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (This IO Module is stable and has been tested internally.)
**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.

[//]: # (Always required)
If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* Initial release.

[//]: # (Always required)
*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

### Instance Properties

Set the *Hostname* and *Port* to that configured on the device.\
Checking *Use SSL* will force ensure the use of a secure connection.\
If *Port* is set to <code>Default</code> then port 443 will be used, If *Use SSL* is unchecked, then port 80 will be used.

Authentication credentials should be entered into *Username* and *Password*.

*Default Unit Id* and *Default Cord Id* control the <code>Instance Default</code> value passed to Actions and Conditions.

Setting the *Poll interval* will dictate how often the PDU is polled for updates.

Checking the *Extended Logging* and/or *Log Comms* checkboxes will provide more detailed log messages. These are intended for diagnostics and problem solving and should ideally be disabled during normal operation.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <style type="text/css">
    td {
        padding: 3 10px;
    }
    </style>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Connection</td>
        <td>Result of last connection attempt</td>
            <ul style="margin-top:0px;">
                <li><code>Access denied</code></li>
                <li><code>Offline</code></li>
                <li><code>Online</code></li>
                <li><code>Unknown</code></li>
            </ul>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Updated connection

Fires when the connection status to the PDU changes, matching *Status*.

Trigger variables:

* *Variable 1*: <code>Online</code> or <code>Offline</code> (*string*).

#### Updated outlet name

Fires when the Controller receives an updated name for the outlet matching *Unit Id*, *Cord Id*, and *Index*.

Trigger variables:

* *Variable 1*: Unit Id (*string*).
* *Variable 2*: Cord Id (*string*).
* *Variable 3*: Index (*integer*).
* *Variable 4*: Name (*string*).

#### Updated outlet state

Fires when the Controller receives an updated state for the outlet matching *Unit Id*, *Cord Id*, and *Index*.

Trigger variables:

* *Variable 1*: Unit Id (*string*).
* *Variable 2*: Cord Id (*string*).
* *Variable 3*: Index (*integer*).
* *Variable 4*: State ('on' or 'off').

### Conditions

#### Outlet state

Returns true if the outlet matching *Unit Id*, *Cord Id*, and *Index*; has a matching *State*

* *Variable 1*: State ('on' or 'off').

### Actions

#### Control outlet

Sends a request to the PDU to set the *State* of outlet *Unit Id*, *Cord Id*, and *Index*.

#### Control group

Sends a request to the PDU to set the *State* of group *Name*.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
