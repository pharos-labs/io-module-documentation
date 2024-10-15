# Casambi Lithernet Gateway - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Sends commands to and receives data from Lithernet Casambi Gateway.

## Requirements

**A Lithernet Casambi Gateway is essential for this module to work. The controller cannot connect directly to the Casambi network but instead via the Gateway.**

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)
This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0.BETA1

* &nbsp; Initial release.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

## Configuration

The Lithernet Gateway needs to be in UDP Casambi Command mode which can be done via the Gateway's web interface.

1. Open the web interface by typing the Gateway's IP address in a browser.
2. Navigate to "General Settings" > "Configuration".
3. Under "Control System", click "Wizard".
4. Select "UDP Casambi Command" and click "next step".
5. Set the "Net ID" (this can be left as default 0), set "DEC or HEX" to "Decimal with hash"
6. Set the "UDP-Port" or leave it as the default 6454
7. Click "reboot..." and the Gateway will reset with the new settings

Ensure your Gateway is running the most recent firmware (at least 2.11 REV1)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Set the *IP Address*, *Port* and *Net ID* to that configured in the Gateway's web interface.

If known, set the *Node ID* of the gateway. This can be left as the default <code>1</code>.

The *Default Fade Time* is used if the *Fade Time* of a *Set Scene Level* or *Set Group Level* Action is set to <code>Instance Default</code>.
Otherwise, the Action *Fade Time* will be used.

Checking the *Log Comms* checkbox will provide more detailed communication logs message. This is for diagnostic purposes and should be disabled during running to maintain controller performance.

Checking the *Log Actions* checkbox will provide more detailed logs information when an Action is called.

Checking the *Log Triggers* checkbox will provide more detailed logs message for Trigger matching. This is for diagnostic purposes and should be disabled during running to maintain controller performance.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td> Scenes &nbsp;&nbsp;&nbsp;</td>
        <td> Requested scene data including active state and levels. </td>
    </tr>
    <tr>
        <td> Groups &nbsp;&nbsp;&nbsp;</td>
        <td> Requested group data including levels. </td>
    </tr>
    <tr>
        <td> Switches &nbsp;&nbsp;&nbsp;</td>
        <td> On/off status of Gateway switches. </td>
    </tr>
    <tr>
        <td> Unit ID &nbsp;&nbsp;&nbsp;</td>
        <td> Gateway ID retrieved from the Gateway. </td>
    </tr>
    <tr>
        <td> Priority &nbsp;&nbsp;&nbsp;</td>
        <td> Priority status eg. "Manual Control". </td>
    </tr>
    <tr>
        <td> Node Type &nbsp;&nbsp;&nbsp;</td>
        <td> Description of node mode. </td>
    </tr>
    <tr>
        <td> Condition &nbsp;&nbsp;&nbsp;</td>
        <td> Condition description eg. "OK" or "Overheated". </td>
    </tr>
    <tr>
        <td> Online &nbsp;&nbsp;&nbsp;</td>
        <td> Gateway online status. </td>
    </tr>
    <tr>
        <td> Last Command Sent &nbsp;&nbsp;&nbsp;</td>
        <td> Last command sent to the Gateway. </td>
    </tr>
    <tr>
        <td> Last Command Received &nbsp;&nbsp;&nbsp;</td>
        <td> Last command received from the Gateway. </td>
    </tr>
    </tbody>
</table>

### Triggers

#### Node Status Received

Fires in response to a *Request Node Status* Action. This will always match true and will always pass the Trigger variables.

Trigger variables:

* &nbsp;*Variable 1*: Unit ID (*integer*).
* &nbsp;*Variable 2*: Scene ID (active scene) (*integer*)
* &nbsp;*Variable 3*: Priority eg."Manual Control" (*string*)
* &nbsp;*Variable 4*: Node type (*string*)
* &nbsp;*Variable 5*: Condition description eg. "OK" or "Overheated" (*string*)
* &nbsp;*Variable 6*: Online status (*string*)

#### Scene Status Received

Fires in response to a *Request Scene Status* Action and can be used to monitor the state of individual scenes.

The Trigger will match true if the *Scene* number (or <code>Any</code> scene) and *State* match, and if the scene level <code>Is In Range</code>, <code>Enters Range</code> or <code>Changes within Range</code> of the *Minimum* and *Maximum* level.

Trigger variables:

* &nbsp;*Variable 1*: Scene ID (*integer*).
* &nbsp;*Variable 2*: Level /255 (*integer*).
* &nbsp;*Variable 3*: Activated/deactivated description (*string*).
* &nbsp;*Variable 4*: Scene state description (*string*).

#### Group Status Received

Fires in response to a *Request Group Status* Action and can be used to monitor the state of individual groups.

The Trigger will match true if the *Group* number  (or <code>Any</code> group) matched and if the _average group level_ <code>Is In Range</code>, <code>Enters Range</code> or <code>Changes within Range</code> of the *Minimum* and *Maximum* level.

Trigger variables:

* &nbsp;*Variable 1*: Scene ID (*integer*).
* &nbsp;*Variable 2*: Average level /255 (*integer*).
* &nbsp;*Variable 3*: Last set level /255 (*integer*).
* &nbsp;*Variable 4*: CCT level (*integer*).
* &nbsp;*Variable 5*: Group state description (*string*).

#### Switch Change Received

Fires when a switch status is received from a scene recalled message.
As a scene recalled message does not contain the scene number, only switch values, the scene number can not be matched and is not passed as a Trigger variable. After a scene recalled scene message is received, the module will query the current active scene (which will also fire a *Scene Status Received* Trigger) and so the *Last Scene Active* Condition can be used in conjunction with this Trigger.

The Trigger will match true all the switch states match the switch properties, *Switch 1* through *Switch 8*. The <code>Any</code> switch state can be used to filter out individual switches, any set to <code>On</code> or <code>Off</code>.

Trigger variables:

* &nbsp;*Variable 1*: Switch 1 state (*integer: 0 for off, 255 for on*).
* &nbsp;*Variable 2*: Switch 2 state (*integer: 0 for off, 255 for on*).
* &nbsp;*Variable 3*: Switch 3 state (*integer: 0 for off, 255 for on*).
* &nbsp;*Variable 4*: Switch 4 state (*integer: 0 for off, 255 for on*).
* &nbsp;*Variable 5*: Switch 5 state (*integer: 0 for off, 255 for on*).
* &nbsp;*Variable 6*: Switch 6 state (*integer: 0 for off, 255 for on*).
* &nbsp;*Variable 7*: Switch 7 state (*integer: 0 for off, 255 for on*).
* &nbsp;*Variable 8*: Switch 8 state (*integer: 0 for off, 255 for on*).
* &nbsp;*Variable 9*: The 8-bit value derived from the binary switches (*integer: 0-255*).

### Conditions

#### Last Scene Active

Returns true if the last known active scene matches the *Scene* property.

As a scene recalled message does not receive the scene number, only switch data, a request is made after a scene recalled message to get the active scene number (the response will _not_ fire a *Scene Status Received* Trigger).

### Actions

#### Request Node Status

Sends a request to the Gateway to get data on its current state such as active scene ID and condition.
The response fires a *Node Status Received* Trigger and updates the node status variables (whether a Trigger exists or not).

#### Request Scene Status

Sends a request to the Gateway to get the status of a *Scene*.
A succession of *Request Scene Status* Actions can be used to get the status of multiple scenes.

The response fires a *Scene Status Received* Trigger and updates the *Scenes* status variables (whether a Trigger exists or not).

#### Request Group Status

Sends a request to the Gateway to get the status of a *Group*.
A succession of *Request Scene Group* Actions can be used to get the status of multiple groups.

The response fires a *Group Status Received* Trigger and updates the *Group* status variables (whether a Trigger exists or not).

#### Set Scene Level

Sends a command to the *Scene* to a *Level* out of 255, in the Action *Fade Time* or if the *Fade Time* is set <code>Instance Default</code>, the instance *Default Fade Time* property will be used.

After the Action is called, a request for the status of all known scenes will be sent.

#### Set Group Level

Sends a command to the *Group* to a *Level* out of 255, in the Action *Fade Time* or if the *Fade Time* is set <code>Instance Default</code>, the instance *Default Fade Time* property will be used.

After the Action is called, a request for the status of all known groups will be sent.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
