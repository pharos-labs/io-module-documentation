# KNXnet/IP - Version 2.4.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Sends and receives boolean values, byte values and dimmer button presses from a KNXnet/IP Router over multicast.

## Module Status

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

#### Module Scope

Please not that this module requires a KNX Router for communication; a KNX Switch does not provide the functionality needed.

#### Version 2.4

* &nbsp;Renamed *Group Address Input* Trigger to *Group Address Boolean Received*.
* &nbsp;Added *Group Address Byte Received* Trigger.
* &nbsp;Added *Group Address Dimming Button Received* Trigger.
* &nbsp;Renamed *Output Group Address* Action to *Send Address Boolean*.
* &nbsp;Added *Send Group Address Byte* Action.
* &nbsp;Added *Send Group Address Dimming Button Press* Action.
* &nbsp;Added *Last Action Sent* status variable.
* &nbsp;Added *Last Trigger Fired* status variable.
* &nbsp;Updated documentation.
* &nbsp;Added extra error handling.
* &nbsp;Performance improvements for high-traffic KNX networks.

#### Version 2.3

* &nbsp;Updated documentation.

#### Version 2.2

* &nbsp;General improvements.

#### Version 2.1

* &nbsp;Performance improvements for high-traffic KNX networks.
* &nbsp;Added *Allow Any Address Match* instance property to match any incoming address in a Trigger.

#### Version 2.0

* &nbsp;Extra error checking and diagnostic logs.
* &nbsp;*Added Extended Logging*.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (#### Configuration / Operation)

## Configuration

Please not that this module requires a KNX Router for communication; a KNX Switch does not provide the functionality needed.

Configure your KNX system using the ETS5 software and ensure a KNX IP Router is included in the system to interface with the Controller. Reserve an *Individual Address* within the KNX system for the Controller.

The Controller must have a Default Gateway set in its configuration for this module to work correctly. If no other Gateway is required, the Controller's own IP Address can be used.

## Operation

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

The *Router Multicast Address* IP address as set in ETS5.

*Router Port* is the port used on the router for communication, as set in ETS5.

The *Group Address Structure* defines whether the message is made up of two or three parts. This will be the structure for both Trigger and Actions (e.g. <code>0/0/1</code> or <code>0/1</code>).
If the Triggers' and Actions' *Group Address* fields don't match this format, an error log message will be displayed if *Extended Logging* is enabled.

The *Individual Address* is the KNX Individual address for the Controller and should be reserved within the KNX system.

If *Self Trigger* is checked, the Controller will fire *Group Address* Triggers within its own programming.

*Allow Any Address Match* is a safety measure to prevent any KNX message matching Trigger unnecessarily.
If any *Group Address* matching is required, (leaving the *Group Address* property in a Trigger empty), then *Allow Any Address Match* must be enabled for this to work.

**Note:** If there is a large amount of KNX traffic on the network, it is strongly advised to have this option disabled to maintain Controller performance.

Checking the *Extended Logging* checkbox will provide more detailed logging for communication, Triggers and Actions. This is for diagnostic purposes and should be disabled during running to maintain Controller performance.

### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Packets Per Second</td>
        <td>The number of KNX messages received in the past second (useful for diagnostics on high traffic KNX networks).</td>
        <td></td>
    </tr>
    <tr>
        <td>Total Packets Received&nbsp;&nbsp;&nbsp;</td>
        <td>The total number of KNX messages received since the Controller last booted (useful for diagnostics on high traffic KNX networks).</td>
        <td></td>
    </tr>
    <tr>
        <td>Last Action Sent</td>
        <td>The last Action sent from the Controller to the KNX network.</td>
        <td></td>
    </tr>
        <tr>
        <td>Last Trigger Fired</td>
        <td>A description of the last KNX messages that successfully matched a Trigger.</td>
        <td></td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Group Address Boolean Received

Fires when a boolean value KNX message is received on the multicast group.

If the received *Group Address* of the message matches the *Group Address* and the *Value* properties of the Trigger, the Trigger will fire.

If any *Group Address* matching is required, (leaving the *Group Address* field in a Trigger empty), then the *Allow Any Address Match* option in the instance properties must be enabled for this to work.

**Note:** If there is a large amount of KNX traffic on the network, it is strongly advised to have this option disabled to maintain Controller performance.

**Note:** If the received value for the given *Group Address* is not a boolean, the Trigger will not fire. If the *Group Address* is set to allow any match, then only values which are detected as booleans will fire the Trigger. If a *Group Address Byte Received* Trigger exists in the project and either shares the same Group Address as the *Group Address Boolean Received* (which if configured correctly, it shouldn't), or the *Group Address Byte Received* Trigger is set to allow any match, then that Trigger will also fire as the received value will be either a <code>0</code> (boolean <code>Off</code>) or <code>1</code> (boolean <code>On</code>). Similarly, a *Group Address Dimming Button Press Received* Trigger will fire with value of <code>1</code> (boolean <code>On</code>) as this is the same as dimmer button <code>Down</code>.

Trigger variables:

* &nbsp;*Variable 1*: Incoming Group Address (*string e.g. "0/0/1"*).
* &nbsp;*Variable 2*: Value (*integer: 0 = Off, 1 = On*).
* &nbsp;*Variable 3*: (*string: "On" or "Off"*).

#### Group Address Byte Received

Fires when a byte value (unsigned 8 bit integer) KNX message is received on the multicast group.

If the received *Group Address* of the message matches the *Group Address* and the *Value* properties of the Trigger, the Trigger will fire.

If any *Group Address* matching is required, (leaving the *Group Address* field in a Trigger empty), then the *Allow Any Address Match* option in the instance properties must be enabled for this to work.

**Note:** If there is a large amount of KNX traffic on the network, it is strongly advised to have this option disabled to maintain Controller performance.

**Note:** If the received value for the given *Group Address* is not an 8 bit byte value, the Trigger will not fire. If the *Group Address* is set to allow any match, then only values which are detected as bytes will fire the Trigger. If a *Group Address Boolean Received* Trigger exists in the project and either shares the same Group Address as the *Group Address Byte Received* (which if configured correctly, it shouldn't), or the *Group Address Boolean Received* Trigger is set to allow any match, then that Trigger will also fire if the received value is either a <code>0</code> (boolean <code>Off</code>) or <code>1</code> (boolean <code>On</code>). Similarly, a *Group Address Dimming Button Press Received* Trigger will fire with value of <code>1</code> as this is dimmer button <code>Down</code> or <code>137</code> as this is dimmer button <code>Up</code>.

Trigger variables:

* &nbsp;*Variable 1*: Incoming Group Address (*string e.g. "0/0/1"*).
* &nbsp;*Variable 2*: Value (*integer: 0-255*).

#### Group Address Dimmer Button Press Received

Fires when a dimmer button KNX message is received on the multicast group.

If the received *Group Address* of the message matches the *Group Address* and the *Value* properties of the Trigger, the Trigger will fire.

If any *Group Address* matching is required, (leaving the *Group Address* field in a Trigger empty), then the *Allow Any Address Match* option in the instance properties must be enabled for this to work.

**Note:** If there is a large amount of KNX traffic on the network, it is strongly advised to have this option disabled to maintain Controller performance.

**Note:** If the received value for the given *Group Address* is not an 8 bit byte value, the Trigger will not fire. If the *Group Address* is set to allow any match, then only values which are detected as bytes will fire the Trigger. If a *Group Address Byte Received* Trigger exists in the project and either shares the same Group Address as the *Group Address Byte Received* (which if configured correctly, it shouldn't), or the *Group Address Byte Received* Trigger is set to allow any match, then that Trigger will also fire if the received value is either a <code><137></code> (dimmer button <code>Up</code>) or <code>1</code> (dimmer button </code>Down</code>). Similarly, a *Group Address Boolean Received* Trigger will fire with value of <code>1</code> (dimmer button <code>Down</code>).

Trigger variables:

* &nbsp;*Variable 1*: Incoming Group Address (*string e.g. "0/0/1"*).
* &nbsp;*Variable 2*: Value (*button press as integer*).
* &nbsp;*Variable 3*: Value String (*string: "On", "Off", "Brighter", "Dimmer"*).

### Actions

#### Send Group Address Boolean

Sends a boolean <code>On</code> (code <code/>1</code>) or <code>Off</code> (code <code>0</code>) value to the KNX *Group Address*.

If the *Self Fire* instance property is enabled, the Controller will fire a *Group Address Boolean Received* Trigger, if one exists and matches the relevant Trigger properties, using the same multicast message that was sent.

#### Send Group Address Byte

Sends an 8-bit byte value, <code>0-255</code>, to the KNX *Group Address*.

If the *Self Fire* instance property is enabled, the Controller will fire a *Group Address Byte Received* Trigger, if one exists and matches the relevant Trigger properties, using the same multicast message that was sent.

#### Send Group Dimmer Button Press

Sends a single dimmer button press, <code>Up</code> (code <code>137</code>) or <code>Down</code> (<code>1</code>), to the KNX *Group Address*.

If the *Self Fire* instance property is enabled, the Controller will fire a *Group Address Dimmer Button Press Received* Trigger, if one exists and matches the relevant Trigger properties, using the same multicast message that was sent.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
