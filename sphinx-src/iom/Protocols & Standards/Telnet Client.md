# Telnet Client - Version 2.3.2

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Opens a Telnet connection to another device running a Telnet service, to send and receive Telnet messages.
## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (#### Module Scope)
[//]: # (TODO)

#### Release Notes

#### Version 2.3.2
* Upper limits for numeric capture are now supported. e.g. <code>\<3d:255\></code>
* Fixes *Reconnect on Poll* instance property

#### Version 2.3
* Improved string capturing.
* Allow for match strings to be terminated with <code>\r</code> and/or <code>\n</code>.
* Fix handling of empty/defaulted <code>username</code> and <code>password</code> fields.
* Updated documentation.

#### Version 2.2.1

* Added handshake string.
* Improved string capturing.
* Updated documentation.
* Fix misleading log line.
* Fix ASCII case matching.

#### Version 2.1

* Added support for sending raw bytes and capturing bytes from incoming messages.
* Improved string capturing.
* Extra logging and error checking.

#### Version 2.0

* Initial release.
* Added support for string capturing.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

Properties, as required, need explicit carriage returns and newlines. These are expressed as `\r` and `\n` respectively.\
e.g. To issue the username 'MyUserName' terminated with both a carriage return and newline, it would be entered in the *Username* property as `MyUserName\r\n`

### Instance Properties

Set *Remote Host* is the destination Telnet device's IP address or host name.

*Username* and *Password* are the login detail for the Telnet connection. If login is not required, leave these blank. *Login Command String* and *Password Command String* define the command received from the remote host to prompt the controller to send login credentials. When the controller receives the *Login Command String*, it will automatically send the *Username* and then when the controller receives the subsequent *Password Command String*, the password is sent. By default, *Login Command String* is "login" and *Password Command String* is "password".

*Handshake* string will be sent immediately after a connection is established.\
The string is sent before any login negotiation and could be used, for example, to trigger a login prompt.

Response keywords to be disregarded can be added to ignore to the *Ignore List*, in comma-separated formats. If a message is received that begins with one of the keywords, the message will not fire a Trigger. If *Log TCP* comms is checked, you will be able to see this message received and the log will show the message will be ignored. It's advisable to add the polling reply keyword (see *Poll Interval*) to the *Ignore List*, otherwise the reply will fire the Trigger, although will not be matched if the message does not match the Trigger *Match String*.

If a reply is not received within the time defined in *Response Timeout*, a log message will be showed if *Log TCP* is checked. This is for informational purposes and will not fire a Trigger.

If *Poll Interval* is enabled, the controller will send a simple message, a carriage return, to the host. If a message is not received in the time defined in *Response Timeout*, a log message will show. If you do not want the response to fire a Trigger, add the reply string to the *Ignore List*.

If *Log Polls* is enabled and the *Poll Interval* is not *Disabled*, then poll messages will show in the controller log.

If *Reconnect on Poll* is enabled and the *Poll Interval* is not *Disabled*, if a poll response has not been received, the connection will be attempted on every poll cycle until the connection is re-established.

If checked, *Error Fires Trigger* will allow and error message to fire a Trigger. Messages are compared with a set of known error strings. If you notice a particular error is still firing the Trigger, add the reply string to the *Ignore List*.

Checking the *Log Triggers* checkbox will provide more detailed logs for Trigger matching.

Checking the *Log Actions* checkbox will show Actions in the log.

Checking the *Log TCP Comms* checkbox will provide more detailed log messages for the TCP connection, including the state (connected disconnected) of the socket as well as all messages received, whether in the *Ignore List* or not. This will also show all poll messages.

### Triggers

#### Telnet Received

Fires when a Telnet message is received by the Controller. The *Match String* can be used to match against known message or can be used to capture variables as defined in the variables section of the Designer help document.

If the *Match String* is empty, the whole message will be passed as a Trigger variable. If the received message is a match to the *Match String*, the whole message will be passed as a Trigger variable.

If the *Match String* contains capture tags (denoted by *<>*), the captured variables (if any) will be passed as Trigger variables (but not the whole message).

##### Differences and limitations
* Floats (numbers with a fractional part, i.e. 1.0) can be captured using the syntax <code>\<f\></code>.

If <code>Bytes</code> is selected, only hex character and escaped characters are allowed (e.g. <code>090A0B0C</code>).\
To capture bytes, the syntax should be eg. <1><2><3> or FF<1>\n<3>.\
If the capture sting is invalid, this will be shown in the logs.

#### Telnet Connection Status Changed

If a *Telnet Connection Status Changed* Trigger is added, this will fire when the Telnet TCP connects or disconnects.

### Actions

#### Send Telnet

Sends the *String*, either as *Type* ASCII or raw bytes, to the host specified in the instance properties.

Escaped characters are supported in both string types for example, as <code>ASCII</code>helloWorld\r\n</code> is valid and for <code>00FF00FF\r\n</code> is valid for <code>Bytes</code>.

### Support

If you encounter any issues with this module, please contact our support team.

[//]: # (#### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (#### Further Notes)
[//]: # (Possible location for further notes, may not be used)
