# Maintained TCP Connection - Version 2.1.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Maintains and monitors a TCP connection with a remote host and fires Triggers on changes.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1

* &nbsp;Add option to *Send String* to send alternative string, with trigger variable insertion.
* &nbsp;Added *Last Action Message Sent* status variable.
* &nbsp;Added *Termination Characters* instance property.
* &nbsp;Updated documentation.
* &nbsp;Bug fixes.

#### Version 2.0

* &nbsp;Initial implementation:
* &nbsp;*Connected* Trigger.
* &nbsp;*Disconnected* Trigger.
* &nbsp;*Host Not Found* Trigger.
* &nbsp;*Error Detected* Trigger.
* &nbsp;*Message Received* Trigger.
* &nbsp;*Connect To Host* Action.
* &nbsp;*Disconnect From Host* Action.
* &nbsp;*Send String* Action.
* &nbsp;Status variables.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

## Configuration

**Note:** The module establishes a TCP connection with a remote device running a TCP server service.
All client communication is handled internally within the module itself and therefore _should not_ be configured in the Network tab.
The IP and port combination should also not be used elsewhere outside of the module, including in other module instances.

## Operation

### Instance Properties

The *Host Name or IP Address* and *Port* are that of the remote host.

If *Connect At Startup* is checked, the Controller will try to establish a connection as soon as it boots up, otherwise, the *Connect To Host* Action must be used first.

If *Auto Attempt Reconnect* is checked, if the Controller detects a disconnect with the host, it will automatically try to re-establish the connection at 10 second intervals.

*Poll String* and *Send Interval* are optional. If the *Send Interval* is set to anything but <code>Disabled</code>,
the Controller will send the *Poll String* at that interval (if a connection is established).

The *Termination Characters* are appended to every string that is sent. This can be any number of characters with null represented by <code>\0</code>, carriage return by \r, new line by \n etc.

If both *Poll String* and *Termination Characters* are left blank but *Send Interval* is enabled, a single carriage return character will be sent.
If *Termination Characters* is defined by *Poll String* is blank, the *Termination Characters* will be used.

Line ending must be explicitly declared, for example is the *Poll String* is <code>mypollstring</code> a carriage ending or newline may want to be appended in escaped format so,  <code>mypollstring\\r</code> or <code>mypollstring\\n</code>.

Checking the *Log Comms* checkbox will provide more detailed log messages for TCP connection statuses. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Destination&nbsp;&nbsp;&nbsp;</td>
        <td>The Host Name or IP address and port number set in the Instance properties.</td>
    </tr>
    <tr>
        <td>Current State&nbsp;&nbsp;&nbsp;</td>
        <td>The current state of the TCP socket with a timestamp.</td>
    </tr>
    <tr>
        <td>Last Error&nbsp;&nbsp;&nbsp;</td>
        <td>The last error that was detected with a timestamp. If the socket is connected, the error will be erased.</td>
    </tr>
    <tr>
        <td>Last Poll Message Sent&nbsp;&nbsp;&nbsp;</td>
        <td>The poll message and a timestamp of when it was last sent.</td>
    </tr>
    <tr>
        <td>Last Action Message Sent&nbsp;&nbsp;&nbsp;</td>
        <td>The last message that was sent from an action and a timestamp of when it was last sent.</td>
    </tr>
        <tr>
        <td>Last Message Received&nbsp;&nbsp;&nbsp;</td>
        <td>The last string received from the remote host.</td>
        <td></td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Connected

Fires when the TCP socket is successfully established and connected.

Trigger variables:

* &nbsp;*Variable 1*: IP Address (*string*).
* &nbsp;*Variable 2*: Port Number (*integer*)

#### Disconnected

Fires when the TCP socket is disconnected for any reason.

Trigger variables:

* &nbsp;*Variable 1*: IP Address (*string*).
* &nbsp;*Variable 2*: Port Number (*integer*)

#### Host Not Found

Fires when a connection can not be established because the host can not be found.

Trigger variables:

* &nbsp;*Variable 1*: IP Address (*string*).
* &nbsp;*Variable 2*: Port Number (*integer*)

#### Error Detected

Fires when a TCP error has been detected for any reason. If the error causes a disconnect, the *Disconnected* Trigger will also fire (if one exists in the project).

Trigger variables:

* &nbsp;*Variable 1*: IP Address (*string*).
* &nbsp;*Variable 2*: Port Number (*integer*)
* &nbsp;*Variable 3*: Error Description (*string*)

#### Message Received

Fires when a message is received from the host. If *String* is empty, any received message will fire the Trigger.
If a *String* is set, the Trigger will only fire if the received message string matched the Trigger *String*.

Trigger variables:

* &nbsp;*Variable 1*: IP Address (*string*).
* &nbsp;*Variable 2*: Port Number (*integer*)
* &nbsp;*Variable 3*: Message Received (*string*)

**Note: String captures are not supported.**

[//]: # (### Conditions)

[//]: # (#### Conditions Name)
[//]: # (#### Start with a verb such as "Is met when..." or "Returns true if...")

### Actions

#### Connect To Host

Initialises a TCP connection to the remote host. This can be used at any time but is required if *Auto Attempt Reconnect* is not enabled in the Instance properties.

If *Auto Attempt Reconnect* is enabled and the previous disconnect occurred because of a *Disconnect From Host* Action, this will resume auto-reconnects.

#### Disconnect From Host

Tears down a TCP connection if one is already established. This will also stop *Auto Attempt Reconnect* if disabled but the *Connect To Host* Action can be used to resume this.

#### Send String

Sends a *String* to the Host. If the field is left blank, the default *Poll String* will be used instead.

It is possible to insert trigger variables in to a string using variable indexes surrounded by capture tags, for example:

Trigger variables are:

* &nbsp;Variable 1: <code>MY_VARIABLE</code>
* &nbsp;Variable 2: <code>65535</code>

If the *String* property is: <code>hello_<1>_world_<2>_</code> the resulting string would be: <code>hello_MY_VARIABLE_world_65535</code>.

**Note: This will only work for the Action String property and not the instance Poll String**

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
