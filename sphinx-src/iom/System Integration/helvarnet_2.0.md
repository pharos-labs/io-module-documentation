# HelvarNet - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Controls and queries devices on a HelvarNet network via Helvar routers.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope

### Release Notes

#### Version 2.0

* Initial release.


*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

## Configuration

The Helvar Design software is used to discover and configure the routers and can be used to obtain information on network settings, scenes, groups and devices, which can be used to configure this module in Designer.

The module communicates with Helvar DIGIDIM 905/910 and IMAGINE 920/945/950 Routers.

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)
It is recommended that *Push Messages* is set to <code>True</code> for routers on the Helvar system.\
This is enabled using Helvar Designer, and details can be found within Helvar Designer's help system.

### Instance Properties

The *Helvar Router Address* is the IP address of the Helvar router.
This information can be obtained from Helvar Designer once a router is discovered.

The *Cluster ID* and *Router ID* are used for pattern matching incoming messages.
HelvarNet would traditionally use the first and second octets of the router IP address for this, but these have been exposed separately for convenience.

The *Router Listener Port* is the TCP port that the controller will connect to on the Helvar router.
The default as set by Helvar for TCP is <code>50000</code>.

Checking the *Log Comms* checkbox will provide more detailed information on communication with the Helvar router, connection information and raw message data. This is intended for diagnostic purposes and should ideally be disabled during normal operation.

If enabled, *Log Triggers and Action* will show information on Actions and Triggers, including errors, in the log.

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
        <td>Router Address</td>
        <td>Configured router IP address</td>
    </tr>
    <tr>
        <td>Cluster ID</td>
        <td>Configured Cluster ID</td>
    </tr>
    <tr>
        <td>Router ID</td>
        <td>Configured Router ID</td>
    </tr>
    <tr>
        <td>Connection Status</td>
        <td>Time of last connection event</td>
    </tr>
    <tr>
        <td>Last Command Sent</td>
        <td>A description of the last command sent form the Controller to the Helvar router</td>
    </tr>
    <tr>
        <td>Last Command Received</td>
        <td>A description of the last command received form the Controller to the Helvar router</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Connected

Fires upon a successful connection with the router.

#### Disconnected

Fires upon disconnection from the router.

#### Latest scene in Group

Fires when a matching scene is recalled in the matching group.

Matching properties:
* *Group*: Matching Group number, or 'any'.
* *Block*: Matching Block number, or 'any'.
* *Scene*: Matching Scene number, or 'any'.
* *Constant Light*: Matching Constant Light Scene flag, or 'any'.
* *Fade Time*: Matching Fade time, or 'any'.

Trigger variables:

1. *Group* (<code>integer</code>)
1. *Block* (<code>integer</code>)
1. *Scene* (<code>integer</code>)
1. *Constant Light Scene* (<code>boolean</code>)
1. *Fade Time (ms)* (<code>integer</code>)

#### Latest level in Group

Fires when a matching level is set in the matching group.

Matching properties:
* *Group*: Matching Group number, or 'any'.
* *Level*: Matching Level, or 'any'.
* *Fade Time*: Matching Fade time, or 'any'.

Trigger variables:

1. *Group* (<code>integer</code>)
1. *Level* (<code>integer</code>)
1. *Fade Time (ms)* (<code>integer</code>)

#### Latest CCT in Group

Fires when a matching Corrected Colour Temperature is set in the matching group.

Matching properties:
* *Group*: Matching Group number, or 'any'.
* *Level*: Matching Level, or 'any'.
* *CCT*: Matching Corrected Colour Temperature, or 'any'.
* *Fade Time*: Matching Fade time, or 'any'.

Trigger variables:

1. *Group* (<code>integer</code>)
1. *Level* (<code>integer</code>)
1. *CCT* (<code>integer</code>)
1. *Fade Time (ms)* (<code>integer</code>)

#### Direct Proportion Received (Group)

Fires when a matching direct Proportion (<code>-100% to +100%</code>) is set in the matching group.

Matching properties:
* *Group*: Matching Group number, or 'any'.
* *Proportion*: Matching Proportion, or 'any'.
* *Fade Time*: Matching Fade time, or 'any'.

Trigger variables:

1. *Group* (<code>integer</code>)
1. *Proportion* (<code>integer</code>)
1. *Fade Time (ms)* (<code>integer</code>)

#### Modify Proportion Received (Group)

Fires when a matching modified Proportion (<code>-100% to +100%</code>) is set in the matching group.

Matching properties:
* *Group*: Matching Group number, or 'any'.
* *Proportion*: Matching Proportion modifier, or 'any'.
* *Fade Time*: Matching Fade time, or 'any'.

Trigger variables:

1. *Group* (<code>integer</code>)
1. *Proportion modifier* (<code>integer</code>)
1. *Fade Time (ms)* (<code>integer</code>)

### Actions

#### Connect

Start connection to Helvar router.

#### Disconnect

Disconnect from Helvar router.

#### Recall Scene (Group)

Sends a command to the router to recall a *Scene* (in the scene *Block*) on a given *Group*, over the *Fade Time* in seconds.

Properties:

* *Group*: Target Group.
* *Block*: Target Scene Block.
* *Scene*: Target Scene.
* *Constant Light*: Set Constant Light Scene flag.
* *Fade Time*: Target Fade time, in seconds.

#### Recall Scene (Device)

Sends a command to the router to recall a *Scene* (in the scene *Block*) on a *Device* in a specific *Subnet*, over the *Fade Time* in seconds.

Properties:

* *Subnet*: Target device subnet.
* *Device*: Target device.
* *Block*: Target Scene Block.
* *Scene*: Target Scene.
* *Fade Time*: Target Fade time, in seconds.

#### Direct Level (Group)

Sends a command to the router to set devices in a *Group* to a fixed *Level*, over the *Fade Time* in seconds.

Properties:

* *Group*: Target Group.
* *Level*: Target intensity level.
* *Fade Time*: Target Fade time, in seconds.

#### Direct Level (Device)

Sends a command to the router to set a *Device* in a specific *Subnet* to a fixed *Level*, over the *Fade Time* in seconds.

Properties:

* *Subnet*: Target device subnet.
* *Device*: Target device.
* *Level*: Target intensity level.
* *Fade Time*: Target Fade time, in seconds.

#### Direct CCT (Group)

Sends a command to the router to set devices in a *Group* to a fixed *CCT*, over the *Fade Time* in seconds.

Properties:

* *Group*: Target Group.
* *CCT*: Target Colour Corrected Temperature.
* *Fade Time*: Target Fade time, in seconds.

#### Direct CCT (Device)

Sends a command to the router to set a *Device* in a specific *Subnet* to a fixed *CCT*, over the *Fade Time* in seconds.

Properties:

* *Subnet*: Target device subnet.
* *Device*: Target device.
* *CCT*: Target Colour Corrected Temperature.
* *Fade Time*: Target Fade time, in seconds.

#### Direct XY (Group)

Sends a command to the router to set devices in a *Group* to a fixed *X* and *Y* colour, over the *Fade Time* in seconds.

Properties:

* *Group*: Target Group.
* *X*: Target CIE X colour point.
* *Y*: Target CIE Y colour point.
* *Fade Time*: Target Fade time, in seconds.

#### Direct XY (Device)

Sends a command to the router to set a *Device* in a specific *Subnet* to a fixed *X* and *Y* colour, over the *Fade Time* in seconds.

Properties:

* *Subnet*: Target device subnet.
* *Device*: Target device.
* *X*: Target CIE X colour point.
* *Y*: Target CIE Y colour point.
* *Fade Time*: Target Fade time, in seconds.

#### Direct Proportion (Group)

Sends a command to the router to relatively increase or decrease (*Proportion* <code>-100% to +100%</code>) the level of devices in a *Group*, over the *Fade Time* in seconds.

Properties:

* *Group*: Target Group.
* *Proportion*: Target direct proportion.
* *Fade Time*: Target Fade time, in seconds.

#### Direct Proportion (Device)

Sends a command to the router to relatively increase or decrease (*Proportion* <code>-100% to +100%</code>) the level of a *Device* in a specific *Subnet*, over the *Fade Time* in seconds.

Properties:

* *Subnet*: Target device subnet.
* *Device*: Target device.
* *Proportion*: Target direct proportion.
* *Fade Time*: Target Fade time, in seconds.

#### Modify Proportion (Group)

Sends a command to the router to relatively increase or decrease (*Proportion* <code>-100% to +100%</code>) the previous Direct Proportion applied to devices in a *Group*, over the *Fade Time* in seconds.

Properties:

* *Group*: Target Group.
* *Proportion*: Target direct proportion modifier.
* *Fade Time*: Target Fade time, in seconds.


#### Modify Proportion (Device)

Sends a command to the router to relatively increase or decrease (*Proportion* <code>-100% to +100%</code>) the previous Direct Proportion applied to *Device* in a specific *Subnet*, over the *Fade Time* in seconds.

Properties:

* *Subnet*: Target device subnet.
* *Device*: Target device.
* *Proportion*: Target direct proportion modifier.
* *Fade Time*: Target Fade time, in seconds.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
