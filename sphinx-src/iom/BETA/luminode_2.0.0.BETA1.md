# LumiNode - Version 2.0.0.BETA1

## Module Summary

Interacts with, and controls, Luminex LumiNodes.

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

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

[//]: # (### List instance properties and their function)

Set the *Hostname* to the hostname or ip address of the node.

Optionally a *Password* can be set, this is revealed after checking *Use authentication*.

Setting the *Poll interval* will dictate how often the node is polled for updates.

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
    <tr>
        <td>Active profile</td>
        <td>Currently active profile id and name</td>
    </tr>
    <tr>
        <td>Name</td>
        <td>Device name</td>
    </tr>
    <tr>
        <td>Serial</td>
        <td>Device serial number</td>
    </tr>
    <tr>
        <td>Firmware</td>
        <td>Device firmware version</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Updated connection

Fires when the connection status to the node changes, matching *Status*.

Trigger variables:

* *Variable 1*: <code>Online</code> or <code>Offline</code> (*string*).

#### Updated profile

Fires when the profile matching *Id* updates.\
Setting *Active* limits the trigger to active profiles only.

Trigger variables:

* *Variable 1*: Id (*string*).
* *Variable 2*: Name (*string*).
* *Variable 3*: Active? (*boolean*).

### Actions

#### Recall profile

Sends a request to the node to active profile *Id*.

#### Reboot

Sends a request to the node to reboot.

#### Set LED brightness

Sends a request to the node alter the LED brightness to *Brightness*.

#### Set display

Sends a request to the node set display on or off based on *On*.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
