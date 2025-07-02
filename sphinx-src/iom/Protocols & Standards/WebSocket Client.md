# WebSocket Client - Version 2.2.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Label*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Communicates with a HTTP/TCP server over a WebSocket.

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)
This IO Module is stable and has been tested internally.

### Release Notes

#### Version 2.2.1
* &nbsp;Fully rewritten WebSocket client library for increased performance and compatibility.
* &nbsp;Added ability to disable keep-alive pings.

#### Version 2.1.1

* &nbsp;Allow the use of HTTP Bearer Authentication Tokens.

#### Version 2.1

* &nbsp;Prevent message from being concatenated during high traffic situations.

#### Version 2.0

* &nbsp;Initial release.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

[//]: # (### List instance properties and their function)

Configure *Hostname*, *Path*, *Protocol* and *Port* to that of the WebSocket server. The protocol prefex ie. <code>wss://</code> should not be entered here.

For testing the module, a free online WebSocket tool can be found on the [Pie Socket website](https://www.piesocket.com/websocket-tester). To use this, enter <code>demo.piesocket.com</code> in to the *Hostname* field and once connected, enter the API path in to the *Path* property. Set the *Protocol* to <code>WSS</code> and leave the *Port* as <code>Default</code> (0).

If *Send keep alive?* is enabled, a ping will be sent a regular intervals to keep the connection open.
Certain WebSocket servers don't support pings and the connection may be aborted, in these instances *Send keep alive?* should be disabled.

If *Auto-Reconnect* is enabled, when the WebSocket and/or the TCP connection is closed, a re-connect attempt will be made.
If enabled and there is a fatal connection error, this may cause the controller to continuously attempt re-connection.

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

Checking the *Log Comms* checkbox will provide more very detailed log messages for TCP frames. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Connection Status&nbsp;&nbsp;&nbsp;</td>
        <td>Status of TCP and WebSocket session with a timestamp of the last change.</td>
    </tr>
    <tr>
        <td>Last Sent&nbsp;&nbsp;&nbsp;</td>
        <td>Last Message sent using the Send Message Action with a timestamp.</td>
    </tr>
    <tr>
        <td>Last Received&nbsp;&nbsp;&nbsp;</td>
        <td>Last message received with a timestamp.</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Connected

Fires when a TCP connection is established with the WebSocket server.

#### WebSocket Established

Fires once a WebSocket session has been established, after TCP has connected. After this point, messages can be exchanged.

#### Disconnected

Fires when a WebSocket and/or the TCP connection has been closed for any reason. Either the *Auto-Reconnect* instance option or a *Connect* Action can be used to re-establish a connection. It is not advised to associate a *Connect* Action with a *Disconnected* _and_ use *Auto-Reconnect*.

#### Messages Received

Fires when a WebSocket message is received from the server and the received message contains the *Match String*, or *Match String* is left blank. Note that *Match String* does not support wildcards.

Trigger variables:

* &nbsp;*Variable 1*: Message received (*string*).

[//]: # (### Conditions)

[//]: # (#### Conditions Name)
[//]: # (#### Start with a verb such as "Is met when..." or "Returns true if...")

### Actions

#### Connect

Establishes a TCP connection and then established a WebSocket session.\
If a HTTP *Bearer Authentication* (RFC 6750) token is required this can be added here.

#### Disconnect

Closes both the TCP socket and the WebSocket session.

#### Send Message

Sends the *Message* over the WebSocket if it is established. If the WebSocket is not established, an error will be printed in the log.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
