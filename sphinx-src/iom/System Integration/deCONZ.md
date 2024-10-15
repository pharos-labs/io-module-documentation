# deCONZ - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Interacts with DeCONZ Gateways.

[//]: # (Brief description of the module; usually the same as the description in the package)

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)
This IO Module is stable and has been tested internally.

[//]: # (Always required)
If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Initial release.

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

Set the *IP Address*, *Port Number*, and *Password* to that configured on the device.

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

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
        <td>Gateway connection status</td>
        <ul style="margin-top:0px;">
            <li><code>Access denied</code></li>
            <li><code>Online</code></li>
            <li><code>Offline</code></li>
        </ul>
    </tr>
    <tr>
        <td>Gateway name</td>
        <td>The identifying name of the gateways</td>
    </tr>
    <tr>
        <td>Product name</td>
        <td>The hardware type of the gateway</td>
    </tr>
    <tr>
        <td>Bridge ID</td>
        <td>The unique identifier for the gateway</td>
    </tr>
    <tr>
        <td>Software version</td>
        <td>The software version of the gateway</td>
    </tr>
    <tr>
        <td>Zigbee channel</td>
        <td>The current wireless frequency channel used by the Gateway</td>
    </tr>
    <tr>
        <td>Zigbee pan ID</td>
        <td>The Zigbee pan ID of the gateway</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

[//]: # (Start with a verb such as "Fires when..." or "Receives...")

#### Updated connection

Fires when the connection to the gateway matches *Status*.

Matching properties:

* *Status*: 'Online', 'Offline, or 'ANY'

Trigger variables:

1. Online (*Boolean*)

### Conditions

[//]: # (Start with a verb such as "Matches if...")

#### Connected

Returns true if connected to the gateway.

Condition variables:

1. Online status 'Online', 'Offline', 'Access denied' (*String*)

### Actions

[//]: # (Start with a verb such as "Requests..." or "Starts...")

#### Set light state

Sends a request to the gateway to set the light state of *Light*.
There are multiple <code>Set light state</code> actions, each with a different subset of properties, covering a different aspect of light control.

**Note:** Depending on the target light, some properties may be ignored. e.g. When using *Switch*, the light is likely to ignore *Transition Time*.

Properties:

* *Light*: Target light ID
* *Switch*: Switch lamp 'On', 'Off', or leave as-is with 'Don't Change'
* *Brightness*: Lamp brightness (0-255)
* *CCT*: Colour temperature (kelvins)
* *Hue*: Colour hue (0-360°)
* *Saturation*: Colour saturation (0-255)
* *x* and *y*: CIE xy colour coordinates (0-1)
* *Transition time*: Fade time for state change (Seconds)

#### Recall scene

Recall a *Scene* from *Group*.

Properties:

* *Group*: Target group ID containing the Scene
* *Scene*: Target Scene ID

#### Store scene

Re-record *Scene* in *Group*.

Properties:

* *Group*: Target group ID containing the Scene
* *Scene*: Target Scene ID

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
