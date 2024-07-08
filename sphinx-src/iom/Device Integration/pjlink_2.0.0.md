# PJLink - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Controls and queries PJLink projectors.

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)
This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Updated documentation.
* &nbsp;Added extra logging and error checking.
* &nbsp;General updates and improvements.
* &nbsp;Spelling fixes.
* &nbsp;Command queue is processed upon successful (re)authentication.
* &nbsp;Non-specification trailing characters in commands, specifically during authentication, are ignored.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

PJLink is a unified standard for operating and controlling projectors.

This module enables a Controller to control and query projectors that are compliant with the protocol via TCP.

Triggers give the user the ability to create sub routines in response to the projector being queried.

#### Error messages

Not be confused with error messages reported from projector about it's hardware, these error messages are normally flagged when either a command has been sent at the wrong time (when the projector is in standby) or when the command parameter is incorrect eg. if RGB input number 7 has been selected but does not exist on the projector.

The error messages are as follows:

* &nbsp;Error 1: Undefined command
* &nbsp;Error 2: Out of parameter
* &nbsp;Error 3: Unavailable time
* &nbsp;Error 4: Projector/Display failure

#### Authentication procedure

To communicate with each other using PJLink, both the projector and the Controller must carry out the authentication procedure in advance. If no password is set, simply sending a command to the projector will establish a connection. If a password is set, the password stored in the modules instance properties will be used to attempt authentication before each session starts.

The authentication procedure involves a password verification process. A password is sent to the projector and is encrypted into a 32-byte message with a random number assigned by the Projector/Display. This is done internally and is encrypted using an MD5 algorithm.

Once authenticated, a connection will be established between the Controller and the projector for 30 seconds. After this time has elapsed, the connection is terminated by the projector and the password will automatically be sent again before the next batch of commands.

### Instance Properties

Set the *Projector IP Address* and *Port* to that of the PJLink projector.

If required, enter the *Password* to authenticate with the projector.

### Triggers

#### General Response

Fires when a received message is not a response to a query. This may be an error, confirmation that a command has been executed, or a warning.

Trigger variables:

* &nbsp;*Variable 1*: Response description (*string*).

#### Power Query Response

Fires in response to a *Power Status Query* Action and the received state matches the *Power State Response* property.

Trigger variables:

* &nbsp;*Variable 1*: Power status (*string*).

#### Current Input Query Response

Fires in response to a *Current Input In Use Query* Action and the received input matches the *Input Type* and *Input Number*.

Trigger variables:

* &nbsp;*Variable 1*: Input type (*string*).
* &nbsp;*Variable 1*: Input number (*integer*).

#### Mute Status Query Response

Fires in response to a *Mute Status Query* Action and the received state matches the *Mute Status* property.

Trigger variables:

* &nbsp;*Variable 1*: Mute status (*string*).

#### Error Status Query Response

Fires in response to a *Error Status Query* Action and the received state matches the *Mute Status* property.

Trigger variables:

* &nbsp;*Variable 1*: Error status (*string*).

#### Lamp Hours Query Response

Fires in response to a *Lamp Number/Lighting Hour Query* Action and the received input matches the *Lamp Number* and *Fire if over* properties.

Trigger variables:

* &nbsp;*Variable 1*: Lamp number (*integer*).
* &nbsp;*Variable 1*: Lamp hours (*integer*).

### Actions

#### Power-on Instruction

Sends a command to the projector to power on.

#### Power Status Query

Sends a request to the projector to receive its power status. The response fires a *Power Query Response* Trigger.

#### Input Switch Instruction

Sends a request to the projector to set its input to the input defined by the *Input Type* and *Input Number*.

#### Current Input In Use Query

Sends a request to the projector to receive its current input. The response fires a *Current Input In Use* Trigger.

#### Mute Instruction

Sends a request to the projector to set its current mute state to the *Mute Command*.

#### Mute Status Query

Sends a request to the projector to receive its current mute status. The response fires a *Mute Status Query Response* Trigger.

#### Lamp Number/Lighting Hour Query

Sends a request to the projector to receive its current lamp hours. The response fires a *Lamp Hours Query Response* Trigger.

#### Input List Query

Sends a request to the projector to receive its input list. The response will be logged.

#### Projector/Display Name Query

Sends a request to the projector to receive its name. The response will be logged.

#### Manufacturer Name Information Query

Sends a request to the projector to receive its manufacturer name. The response will be logged.

#### Product Name Information Query

Sends a request to the projector to receive its product name. The response will be logged.

#### Other Information Query

Sends a request to the projector to receive any other miscellaneous information. The response will be logged.

#### Class Information Query

Sends a request to the projector to receive its class type. The response will be logged.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
