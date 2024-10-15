# Enocean Rocker Switch Via Deuta Enodisc - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Receives button press messages for a F6-02-02 Rocker Switch via a Deuta Enodisc.

## Module Status

**Note:** This module has been tested internally but has limited field testing. Testing is recommended before being used on a live project.

This module has been developed using a Deuta Enodisc gateway. Whilst this may work with Enocean gateways, this can not be guaranteed.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope

The module currently only supports integration with the Enocean F6-02-02 rocket switch. Whilst this may work on similar devices, this has not been tested and is not officially being supported.

If two rocker buttons are pressed concurrently, it's not always possible to determine which these are and a best effort attempt is used to work this out. For better reliability, single button presses are advised.

### Release Notes

#### Version 2.0.BETA1

* &nbsp;Initial BETA release.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Set the *IP Address* and *Port* to that of the Deuta Enodisc. The default port is <code>8424</code>.

*Packet Types* defines the types of Enocean messages the Controller should listen to. As this a BETA version, the only type of packets currently supported are telegrams. All other messages will be ignored and an error log will be displayed.

Checking the *Extended Logging* checkbox will provide more detailed log messages for Enocean communication.

### Triggers

#### F6-02-02 Rocker Switch, 2 Pressed

Fires when a button pressed telegram is received. This may be a single button press or a combination of two.

If the transmitter ID of the received press matched one of the *Transmitters* or if any *Transmitters* is set (<code>FFFFFFFF</code>) and the *Button* and *Pressed With* combination match with the received message, the Trigger will fire.

If two rocker buttons are pressed concurrently, it's not always possible to determine which these are and a best effort attempt is used to work this out. For better reliability, single button presses are advised.

#### F6-02-02 Rocker Switch, Released

Fires when a button pressed telegram is received.

If the transmitter ID of the received released matched one of the *Transmitters* or if any *Transmitters* is set (<code>FFFFFFFF</code>) and the *Button* released matches with the received message, the Trigger will fire.

[//]: # (### Conditions)

[//]: # (#### Conditions Name)
[//]: # (#### Start with a verb such as "Is met when..." or "Returns true if...")

[//]: # (### Actions)

[//]: # (#### Action Name)
[//]: # (#### Start with a verb such as "Sends..." or "Sets...")

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
