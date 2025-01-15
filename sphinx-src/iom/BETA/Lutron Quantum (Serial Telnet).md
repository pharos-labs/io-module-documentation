# Lutron Quantum (Serial/Telnet) - Version 2.1.0.BETA1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Interacts with Lutron system using Lutron integration protocol.

[//]: # (Brief description of the module; usually the same as the description in the package)

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (This IO Module is stable and has been tested internally.)
**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.

This module has been tested internally on an Athena system with a QSE-CI-NWK-E Integration Access Point.

[//]: # (Always required)
If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1

* Added Actions:
    * Set Area scene
    * Get Area scene
    * Set Monitoring
    * Other command
* Added Trigger:
    * Other report
* Improved issue tracking

#### Version 2.0

* Initial release.

[//]: # (Always required)
*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

## Requirements
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

A Lutron Integration Access Point with an RS232 interface is required.\
Examples of such interfaces are:
* QSE-CI-NWK-E
* RR-MAIN-REP-WH
* RRK-MAIN-REP-WH

## Configuration
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

### Telnet
The authentication credentials should already have been setup on the Lutron Integration Access Point.\
Generally this is done by establishing a telnet connection with the access point during commissioning and following the prompts.\
Please check the Lutron Integration Access Point documentation for details.

### Serial
The serial settings of the Controller and Lutron Integration Access Point should be set to match.\
Please check the Lutron Integration Access Point documentation for details on how this can be obtained and/or altered.\
The Controllers *Baud rate*, *Data bits*, *Parity*, *Stop bits*, and *Mode*; can be altered from within the *Interfaces* tab of the *Network* page within Designer.

In general, the settings will <i>likely</i> be as follows:
* Mode: <code>RS232</code>
* Baud Rate: <code>9600</code> OR <code>115200</code>
* Data bits: <code>8</code>
* Parity: <code>None</code>
* Stop bits: <code>1</code>

### Integration ID
Throughout the module there is reference to an 'Integration ID', this is a unique number assigned to an object on the Lutron system. ID's are assigned using from the integration dialog within Lutron Designer.\
It is recommend that an integration report is generated, and included with any support requests.

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

<b><i>This module is a generic interface to the Lutron Integration Protocol, as such certain actions, triggers, and parameter combinations; may not be appropriate for the Lutron system and/or target device.\
Please consult the Lutron Integration Protocol documentation support matrix, and observe the Controller's log for error feedback.</b></i>

If there is a required Integration Protocol function missing, please inform support.

### Instance Properties

[//]: # (### List instance properties and their function)

Setting *Interface* will display interface type related options:
* When using serial connection, set the *Serial Port* and *Port* to match the Controller's serial interface connected to the Lutron Integration Access Point.
* When using telnet connection, set the *IP Address* to that of the Lutron Integration Access Point. Set the authentication credentials in *Username* and *Password*.

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.
Checking *Log Comms* with fully log all communication with the Lutron Integration Access Point, this can be useful for diagnosing telnet connection issues. It should be disabled during normal operation.

### Triggers
[//]: # (Start with a verb such as "Fires when..." or "Receives...")

#### Connected

*[Telnet only]* Fires when the Controller establishes an authenticated connection to the Lutron Integration Access Point.

#### Disconnected

*[Telnet only]* Fires when the Controller disconnects from the Lutron Integration Access Point.

#### Access Denied

*[Telnet only]* Fires when the Lutron Integration Access Point rejects the authentication credentials.

#### Area scene

Fires when the Controller receives a matching *Scene*, from an area with *Integration ID*.

Trigger variables:

* &nbsp;*Variable 1*: Integration ID (*integer*).
* &nbsp;*Variable 2*: Scene (*integer*).

#### Area occupancy

Fires when the Controller receives a matching occupancy *State*, from am area with *Integration ID*.

Trigger variables:

* &nbsp;*Variable 1*: Integration ID (*integer*).
* &nbsp;*Variable 2*: Occupancy State (*integer*).
    - &nbsp;1 = Unknown
    - &nbsp;2 = Inactive
    - &nbsp;3 = Occupied
    - &nbsp;4 = Unoccupied

#### Device scene

Fires when the Controller receives a matching *Scene*, from a device with *Integration ID*.

Trigger variables:

* &nbsp;*Variable 1*: Integration ID (*integer*).
* &nbsp;*Variable 2*: Scene (*integer*).

#### Device led state

Fires when the Controller receives a matching LED *State*, from a device with *Integration ID*.

Trigger variables:

* &nbsp;*Variable 1*: Integration ID (*integer*).
* &nbsp;*Variable 2*: LED State (*integer*).
    - &nbsp;0 = Off
    - &nbsp;1 = On
    - &nbsp;2 = Flash
    - &nbsp;3 = Rapid Flash

#### Device light level

Fires when the Controller receives a light level matching *Level is* and *Level*, from a device with *Integration ID*.

Trigger variables:

* &nbsp;*Variable 1*: Integration ID (*integer*).
* &nbsp;*Variable 2*: Level (Percent) (*number*).

#### Group occupancy

Fires when the Controller receives a matching occupancy *State*, from a group with *Integration ID*.

Trigger variables:

* &nbsp;*Variable 1*: Integration ID (*integer*).
* &nbsp;*Variable 2*: Occupancy State (*integer*).
    - &nbsp;3 = Occupied
    - &nbsp;4 = Unoccupied
    - &nbsp;255 = Unknown

#### Output zone level

Fires when the Controller receives a zone level matching *Level is* and *Level*, from an output with *Integration ID*.

Trigger variables:

* &nbsp;*Variable 1*: Integration ID (*integer*).
* &nbsp;*Variable 2*: Level (Percent) (*number*).

#### Other report

Fires when the Controller receives, an otherwise unhandled, custom report for *Command*.

Trigger variables:
* &nbsp;*Variable 1*: Optional parameter 1 (*integer* or *number* or *string*)
* &nbsp;*Variable 2*: Optional parameter 2 (*integer* or *number* or *string*)
* &nbsp;*Variable 3*: Optional parameter 3 (*integer* or *number* or *string*)

Please refer to Lutron documentation for expected parameters.

### Actions
[//]: # (Start with a verb such as "Requests..." or "Starts...")

#### Set Monitoring

Sets the enabled status of messages with *type*, the Lutron system will report, to *Enable*.

#### Get Area occupancy State

Requests the area with *Integration ID* to report its occupancy state.

#### Set Area level

Sets the area with *Integration ID* to zone *Level*, optionally with a *Fade* and *Delay* time.
<i>n.b. The Lutron system is likely to respond with Output zone level.</i>

#### Set Area scene

Sets the area with *Integration ID* to *Scene*.

#### Get Area scene

Requests the area with *Integration ID* to report its current scene.

#### Set Device enable

Sets the enabled status of the device with *Integration ID* to *Enable*.

#### Set Device open

Sets the open status of the device with *Integration ID* to *Open*.

#### Set Device occupied

Sets the occupied status of the device with *Integration ID* to *Occupied*.

#### Set Device button

Sets the button state of the device with *Integration ID* to *Action*.

#### Set Device scene

Sets the device with *Integration ID* to *Scene*.

#### Get Device scene

Requests the device with *Integration ID* to report its current scene.

#### Set Device LED state

Sets the LED state of the device with *Integration ID* to *State*.

#### Get Device LED state

Requests the device with *Integration ID* to report its LED state.

#### Set Device light level

Sets the device with *Integration ID* to light *Level*, optionally with a *Fade* and *Delay* time.

#### Get Device light level

Requests the device with *Integration ID* to report its current light level.

#### Get Group occupancy State

Requests the group with *Integration ID* to report its occupancy state.

#### Set Output zone level

Sets the output with *Integration ID* to zone *Level*, optionally with a *Fade* and *Delay* time.

#### Get Output zone level

Requests the output with *Integration ID* to report its current zone level.

#### Other command

Sends an other wise unavailable custom command, with the specified *Operation* type, and *Command* string.\
Please refer to Lutron documentation for valid *Parameter 1*, *Parameter 2*, and *Parameter 3*.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.
Please include a copy of the Integration report generated by Lutron Designer.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
