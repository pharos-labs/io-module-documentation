# Pragma Innovations ARVIGOmoto - Version 2.1.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Receives and sets fader values, button states, button statuses (colours) and connection status for a Pragma Innovations ARVIGOmoto device, over the IBEX 1 protocol.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1

* &nbsp;Added Trigger variables for all fader values and button statuses to *Status Received* Trigger.
* &nbsp;Initialises button state to <code>Released</code> at startup.

#### Version 2.0

* &nbsp;Initial implementation.
* &nbsp;*Fader Move* Trigger.
* &nbsp;*Button Input* Trigger.
* &nbsp;*Connection* Trigger.
* &nbsp;*Heartbeat* Trigger.
* &nbsp;*Status Received* Trigger.
* &nbsp;*Button Input* Condition.
* &nbsp;*Button LED Status* Condition.
* &nbsp;*Set Fader* Action.
* &nbsp;*Set All Faders* Action.
* &nbsp;*Set Button LED* Action.
* &nbsp;*Initialise Communication* Action.
* &nbsp;*Status Request* Action.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

The current fader values, button states and button LED statuses can be viewed in the IO tab of the web interface.

### Instance Properties

The *IP Address* and *Port Number* are those of the ARVIGOmoto device.
The *Port Number* that the ARVIGOmoto uses for communication by default is <code>10002</code> but this can be configured and changed if needed.

If checked, *Connect at Startup* will initialise communication once the Controller boots.
If this option is not selected, communication can be started by using the *Initialise Connection* Action but will also be attempted when
sending a command.

If *Continue Reconnect Attempts* is selected, when a break in communication is detected, the Controller will continue to connect to the ARVIGOmoto.
until a connection is established. If unselected, two attempts will be made before the ARVIGOmoto is deemed offline.
A disconnect status can occur either from a close in the TCP connection or if two heartbeats have been missed.

The *Extended Logging* option will provide more detailed log messages for Triggers and Actions.
This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

The *Log TCP Option* option will provide more detailed log messages ffor TCP connection states and errors, as well as raw TCP data received.
This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

### Triggers

#### Fader Move

Fires when a fader value is received from the ARVIGOmoto. If the *Fader* is set to <code>Any</code>, the Trigger will fire when a value for
any of the 8 faders is received, otherwise the Trigger will only fire when a value for the specified *Fader* is received.

Trigger variables:

* &nbsp;*Variable 1*: Fader number (*integer: 1-8*).
* &nbsp;*Variable 2*: Fader value (*integer 0-255*).
* &nbsp;*Variable 3*: Message received (*string*).

#### Button Input

Fires when the input state (pressed or released) of a button is received.

If the *Button* is set to <code>Any</code>, the Trigger will fire when a state for
any of the 5 buttons is received, otherwise the Trigger will only fire when a value for the specified *Button* is received.

Similarly, the *Event* can allow the Trigger to fire for <code>Any</code> *Event* or specifically when the button *Event* is <code>Pressed</code> or <code>Released</code>.

Trigger variables:

* &nbsp;*Variable 1*: Button number (*integer: 1-5*).
* &nbsp;*Variable 2*: Button state (*integer 0 (released) or 1 (pressed)*).
* &nbsp;*Variable 3*: Message received (*string*).

#### Connection

Fires when a change in the connection status of the ARVIGOmoto is detected.

If the detected status matches the *Status* property, the Trigger will match.

A *Status*: <code>Connected</code> Trigger will fire once a connection has been established with the ARVIGOmoto either on first connect or once the ARVIGOmoto has been
offline and then reconnected.

A *Status*: <code>Disconnected</code> Trigger will only fire if the ARVIGOmoto has already been connected and then disconnects. It will not fire again until a reconnection has been made and then another disconnect has happened.

If the *Continue Reconnect Attempts* Instance property is selected, if a disconnect is detected and the Trigger *Status* is set to <code>Disconnected</code>,
the Trigger will fire once and then reconnection attempts will be made.

A disconnected status can occur either from a close in the TCP connection or if two heartbeats have been missed.

Trigger variables:

* &nbsp;*Variable 1*: Connection state (*integer 0 (disconnected) or 1 (connected)*).
* &nbsp;*Variable 2*: Connection state (*string*).

#### Heartbeat

Fires when a heartbeat message has been received which will be every five seconds if the ARVIGOmoto is online and connected.
This Trigger is not essential for operation.

There are no Trigger variables for this Trigger.

#### Status Received

Fires in response to a status request from the Controller to the ARVIGOmoto, either at startup or using a *Status Request* Action.

Trigger variables:

* &nbsp;*Variable 1*: Message received (*string*).

### Conditions

#### Button Input

Condition is met if a *Button*'s *Button State* matches the last known state.
The current state can be viewed on the IO tab of the web interface.

#### Button LED Status

Condition is met if a *Button*'s *LED Status* (colour) matches the last known status.
The current state can be viewed on the IO tab of the web interface.

### Actions

#### Set Fader

Sends a command to the ARVIGOmoto to set a given *Fader* to the *Value*.

#### Set All Faders

Sends a command to the ARVIGOmoto to set the levels of all faders; *Fader [Fader Number]*.

#### Set Button LED

Sends a command to the ARVIGOmoto to set a given *Button* to the *Status* (colour).

#### Initialise Communication

Sends a message to the ARVIGOmoto to establish a connection.
If TCP is not already connected, this will first be established and then the message is sent.

If the *Connect at Startup* Instance property is not set, this Action will be required to establish a connection,
although a connection will also be attempted if any other Action is used.

#### Status Request

Sends a request to the ARVIGOmoto to return all fader values, button states and LED statues (colours).

When a reply is received, the *Connection Status Received* will be fired with the data.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
