# ISAAC - Version 2.1.3

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Integrates with Smart Monkey's ISAAC platform by creating objects and receiving playable commands.

## Module Status

This IO Module is stable and has been tested both internally and externally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope

The supported ISAAC objects are playables, variables, and control panels.
The Controller can receive playable start and stop commands but can not Trigger ISAAC.

**Note: It is currently only possible to delete one playable in any one boot cycle.**

### Release Notes

#### Version 2.1.3
* &nbsp;API Updates for Playables

#### Version 2.1.2

* &nbsp;HTTP port correctly applied
* &nbsp;Allow use of SSL for HTTP (HTTPS)
* &nbsp;Added support for control panels
* &nbsp;Added support for API token
* &nbsp;TCP connection reliability improvements
* &nbsp;Add required HTTP content type headers
* &nbsp;Default HTTP port changed from 8000 to 80
* &nbsp;*Description* is now optional for object creation
* &nbsp;Improve handling of object creation responses
* &nbsp;Improve handling of controller project reloads/unloads

#### Version 2.0

* &nbsp;Initial Public release.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

## Requirements

A unique module must be configured for IO the module within the ISAAC subsystem. The module *Subsystem/Module ID* is the unique reference that the module uses for communication so much match that configured in ISAAC.

In this readme, the ISAAC module is referred to as a subsystem to distinguish it from the IO module.

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

*ISAAC IP Address* is the address of the ISAAC Controller.

ISAAC uses both HTTP and TCP for communication and the *HTTP Port* *TCP Port* should be set accordingly. The default *HTTP port* is <code>80</code> and the default *TCP Port* is <code>8099</code>.
If authentication is required then an *API token* can be set.

If *Use SSL (HTTP)* is selected then HTTP will use secure SSL/HTTPS connections. You should ensure your *HTTP port* is appropriately updated for HTTPS.

The *Subsystem Display Name* is an arbitrary description of the ISAAC module. For consistency, it can be set to the same value for the *Subsystem ID*.

The *Subsystem/Module ID* is the unique reference that the module uses for communication so much match the subsystem name in ISAAC.

If *Auto Reconnect* is checked, the Controller will attempt a TCP connection both at start and if the Controller notices that the connection has been closed.
If disabled, the *Connect* and *Disconnect* Actions must be used to manage the TCP connection.

If *Create control panel for this controller* is checked, the Controller will automatically create a control panel directing towards this controller.

If *Enable Triggering On Connect* is enabled, the Controller will send a subscription request to ISAAC to listen to playables being started and stopped. If disabled, *Enable Playable Triggering* and *Disable Playable Triggering* Actions must be used to manage the subscription.

Checking the *Log Comms* and *Log TCP Comms* checkboxes will provide more detailed communication logs messages at debug level. This is for diagnostic purposes and should be disabled during running to maintain Controller performance.

Checking the *Log Triggers and Actions* checkbox will provide more detailed logs information when an Action is called and Triggers are tested/fired.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td> Connection Status &nbsp;&nbsp;&nbsp;</td>
        <td> Shows the TCP connection status to the ISAAC hardware. </td>
    </tr>
    <tr>
        <td> Variables &nbsp;&nbsp;&nbsp;</td>
        <td> A list of variables that exist within an ISAAC subsystems, including display name, external reference and current values. </td>
    </tr>
    <tr>
        <td> Playables &nbsp;&nbsp;&nbsp;</td>
        <td> A list of playables that exist within an ISAAC subsystems, including display name and external reference. </td>
    </tr>
    <tr>
        <td> Playable Triggering Status &nbsp;&nbsp;&nbsp;</td>
        <td> Shows whether the Controller is subscribed to received ISAAC events. </td>
    </tr>
    <tr>
        <td> Control Panels&nbsp;&nbsp;&nbsp;</td>
        <td> A list of control panels that exist within an ISAAC subsystems, including display name and external reference. </td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Connected

Fires when a TCP connection has been successfully established.

#### Disconnected

Fires when a TCP connection is disconnected.

#### Playable Started

Fires when a playable has started in the ISAAC subsystem and the received playable matches the *Display Name* or *External Ref*.

##### Note: Playable Triggering must be enabled for a playable started event to be received.

Trigger variables:

* &nbsp;*Variable 1*: Display Name (*string*).
* &nbsp;*Variable 2*: Command (*string*)
* &nbsp;*Variable 3*: Description (*string*)
* &nbsp;*Variable 4*: Duration (*integer in ms*)
* &nbsp;*Variable 5*: Group (*string*)
* &nbsp;*Variable 6*: External Reference (*string*)

#### Playable Ended

Fires when a playable has ended in the ISAAC subsystem and the received playable matches the *Display Name* or *External Ref*.

##### Note: Playable Triggering must be enabled for a playable ended event to be received.

Trigger variables:

* &nbsp;*Variable 1*: Display Name (*string*).
* &nbsp;*Variable 2*: Command (*string*)
* &nbsp;*Variable 3*: Description (*string*)
* &nbsp;*Variable 4*: Duration (*integer in ms*)
* &nbsp;*Variable 5*: Group (*string*)
* &nbsp;*Variable 6*: External Reference (*string*)

#### Timeline Playable Started

Fires when a playable has started in the ISAAC subsystem and the received playable name matches the *Trigger Number's* name. It is important to maintain the same display name for both the Trigger and the ISAAC playable.

##### Note: Playable Triggering must be enabled for a playable started event to be received.

Trigger variables:

* &nbsp;*Variable 1*: Display Name (*string*).
* &nbsp;*Variable 2*: Command (*string*)
* &nbsp;*Variable 3*: Description (*string*)
* &nbsp;*Variable 4*: Duration (*integer in ms*)
* &nbsp;*Variable 5*: Group (*string*)
* &nbsp;*Variable 6*: External Reference (*string*)

#### Timeline Playable Ended

Fires when a playable has ended in the ISAAC subsystem and the received playable name matches the *Trigger Number's* name. It is important to maintain the same display name for both the Trigger and the ISAAC playable.

##### Note: Playable Triggering must be enabled for a playable ended event to be received.

Trigger variables:

* &nbsp;*Variable 1*: Display Name (*string*).
* &nbsp;*Variable 2*: Command (*string*)
* &nbsp;*Variable 3*: Description (*string*)
* &nbsp;*Variable 4*: Duration (*integer in ms*)
* &nbsp;*Variable 5*: Group (*string*)
* &nbsp;*Variable 6*: External Reference (*string*)

[//]: # (### Conditions)

[//]: # (#### Conditions Name)
[//]: # (#### Start with a verb such as "Is met when..." or "Returns true if...")

### Actions

#### Connect

Attempts a TCP connection with the ISAAC Controller.

#### Disconnect

Closes the TCP connection with the ISAAC Controller.

#### Get Playables

Sends a command to the ISACC Controller to retrieve information on all playables in the ISAAC subsystem.
The response will update the status variables.

#### Create Playable

Sends a request to create a playable in the ISAAC subsystem.

The *Display Name*, *Command*, and *Duration* are mandatory fields; *Description* and *Group* are optional.

When the request is made, an external reference is generated from the *Display Name*, and is displayed in the web interface.
The *Display Name* or external reference can be use when matching Triggers.

#### Create Playable From Timeline

Sends a request to create a playable in the ISAAC subsystem using a timeline's properties.

This is the same underlying request as *Create Playable*, but the display name, duration and group are taken from the timeline specified in the *Timeline Number* property.

The *Command* is mandatory fields but *Description* is optional.

When the request is made, an external reference is generated from the timeline's, and is displayed in the web interface.
The *Display Name* or external reference can be use when matching Triggers.

#### Delete Playable

Sends a request to delete a playable that has the same *Display Name/External Reference* in the ISAAC subsystem. If the playable does not exist, an error will be returned.

#### Get Control Panels

Sends a command to the ISACC Controller to retrieve information on all control panels in the ISAAC subsystem.
The response will update the status variables.

#### Create Control Panel

Sends a request to create a registered control panel in the ISAAC subsystem.
If the control panel already exists, it will be updated.

The *Connection URL* is the control panels iframe target

When the request is made, an external reference is generated from the *Display Name*, and is displayed in the web interface.
The *Display Name* or external reference can be use when matching Triggers.

#### Delete Control Panel

Sends a request to delete a control panel that has the same *Display Name/External Reference* in the ISAAC subsystem. If the control panel does not exist, an error will be returned.

#### Get Variables

Sends a command to the ISACC Controller to retrieve information on all variables in the ISAAC subsystem.
The response will update the status variables.

#### Create Variable

Sends a request to create a variable in the ISAAC subsystem.

The *Type*, *Display Name* and *Initial Value* are mandatory and *Description* and *Tags* are optional.

*Tags* are user-specific labels to cross-reference variables. *Tags* are required to be in comma-separated format and can only be letters, numbers, and underscores.

When the request is made, an external reference is generated from the *Display Name* and is displayed in the web interface.
The *Display Name* or external reference can be use when matching Triggers.

#### Update Variable

Sends a request to update the value of a variable that has the same *Display Name/External Reference* in the ISAAC subsystem. If the playable does not exist, an error will be returned.

#### Enable Playable Triggering

Adds an event subscription in the ISAAC subsystem, which allows playable events to be received when a playable is started or has ended, therefore enabling Trigger firing.

#### Disable Playable Triggering

Deletes the event subscription in the ISAAC subsystem, which dis-allows playable events to be received when a playable is started or has ended, therefore disabling Trigger firing.

[//]: # (#### Action Name)
[//]: # (#### Start with a verb such as "Sends..." or "Sets...")

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
