# Enocean Via Deuta Enodisc - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Receives telegrams from Encoean devices, such as buttons and sesnosrs, via an Enocean gateway and fires Trigger when specifc values are recieved.

## Module Status

**Note:** This module has been tested internally but has limited field testing. Testing is recommended before being used on a live project.

This module has been developed using a Deuta Enodisc gateway. Whilst this may work with Enocean gateways, this can not be guaranteed.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope

This module has been tested with a Deuta Controls EnoDisc bridge and a selection of Enocean devices including buttons and sensors.

Currently, the supported RORG types are:

* Repeated Switch Communication (0xF6)
* 1 Byte Communication (0xD5)
* 4 Byte Communication (0xA5)

This should cover the majority of cases but if other RORG types are required, please contact support.

The *Function* and *Type*, although can be specified aren't necessary as the Enocean telegram does not contain this information and therefore can't be used to identify devices.

The module does not support the full list of Enocean profiles and therefore profiles paramaters must be defined within the modules.

Each device should specify a profile code and the individual parameters can be found on the [Enocean Website profile page](http://tools.enocean-alliance.org/EEPViewer/).
The properties in the module should match the equipment profile almost exactly for ease of use. The user data portion of an Enocean message contains information outlined in the profile.

**Note: The module handles low-level protocol data and does not return information on devices in JSON format.**

### Release Notes

#### Version 2.0

* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

## Configuration

In most cases, the Encoean hardware an devices are plug-and-play. The information the Controller must know first off is the IP address of the gateway and information on individual transmitters such as their individual ID can be obtaining during run time.

## Operation

The defining profile parameter is specified in the Instance properties and not in the Trigger, for quick set up and removing the need for duplicate Triggers. The defining parameter could be a button ID, a temperature value or a switch state (on/off).

The Trigger specifies the value range on which to match to the above defining parameter. The *Additional Parameter Match* Condition can be used to further filter out parameters.

The *Transmitters* in both the Instance properties and the Trigger can be used to filter out messages by sender. They are used in combination; the Instance property to define a set of transmitters and the Trigger to filter a specific set (or all) of those. As the Enocean telegram does not contain the function and type of a device, setting the *Transmitters* ensures that other Instance Triggers firing erroneously.

### Instance Properties

The *IP Address* and *Port* are that of the gateway. The IP address can be duplicated shared across module Instances and they will all share the same TCP socket. If multiple gateways are used, in this implementation the module, a new Instance for each address/profile pair is required. If logging is enabled for multiple Instance, you may end up getting duplicate log message for each packet received.

Checking the *Log Comms* checkbox will provide more detailed communication logs message. This is for diagnostic purposes and should be disabled during running to maintain controller performance.

Checking the *Log Triggers and Conditions* checkbox will provide more detailed logs message for Trigger and Condition matching. This is for diagnostic purposes and should be disabled during running to maintain controller performance.

The *Function* and *Type* can be entered in the format hexID-space-name eg. <code>04 Position Switch</code>. This information is not actually required for this module to function however it can be useful information to display. The name can be left blank and the hex ID can be set to XX if need be.

The *Transmitters* in both the Instance properties and the Trigger can be used to filter out messages by sender. They are used in combination; the Instance property to define a set of transmitters and the Trigger to filter a specific set (or all) of those. Transmitters are defined in 32bit hex format, separated by semi-colons. By default, both are set to <code>FFFFFFFF</code> which mean any ID. If this appears anywhere in the *Transmitters* property, this will still be treated as any ID.

As the Enocean telegram does not contain the function and type of a device, setting the *Transmitters* ensures that other Instance Triggers firing erroneously. If transmitter IDs are currently unknown,, it can be useful to set both the Instance and Trigger IDs to <code>FFFFFFFF</code> to discover the devices.

The remaining Instance properties are the variables of the defining parameter (eg. a button ID or a temperature value) of the device. All parameter information can be found on the [Enocean Website profile page](http://tools.enocean-alliance.org/EEPViewer/).

The properties in the module should match the equipment profile almost exactly for ease of use. The user data portion of an Enocean message contains information outlined in the profile.

*Bit Offset* (as stated in the profile), the starting bit position of the relevant data within the user data.

*Bit Size* (as stated in the profile); the length of the relevant data within the user data.

Therefore, the relevant data bits within the user data is from the *Bit Offset* index (0 based) to *Bit Offset* plus the *Bit Size*.

*Valid Range Minimum* and *Valid Range Maximum* (as stated in the profile) definer the upper and lower range of a _raw_ value and is always an integer. This may not relate directly to, for example, a temperature value but is used to calculate this, using the ranges.

If there is no scale defined in the profile documentation, the value can be used verbatim such as in the case of an enum or button number. The scale options can be used to convert the raw value in to a more useful value. The scale, if used, can be found in the profile documentation next to the *Valid Range*.

*Range Option* defines whether or not the *Scale Minimum* and *Scale Maximum* are to be used for conversation. If <code>Enum (Ignore Scale)</code> is selected, the raw value will be used. If <code>Use Scale</code> is used, then the *Scale Minimum* and *Scale Maximum* values will be used to convert the raw value to a more useful value.

The *Units/Description* is optional but can be used to better identify the value in the Trigger descriptions, the logs and in the status variables. This could be to show the value is a button ID, a button pressed state or a lux level. If the string <code>\<value\></code> is part of the *Units/Description* then this will be replaced by the value.

Therefore <code>Button \<value\></code> would display <code>Button 1</code>, <code> Button 2</code>.

<code>\<value\>°C</code> would display <code>21°C</code> or <code>10.5°C</code>.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>RORG&nbsp;&nbsp;&nbsp;</td>
        <td>The RORG type from the Instance properties.</td>
    </tr>
    <tr>
        <td>Profile&nbsp;&nbsp;&nbsp;</td>
        <td>The RORG ID-function-type profile code.</td>
    </tr>
    <tr>
        <td>Transmitter ID&nbsp;&nbsp;&nbsp;</td>
        <td>The transmitter ID from the last telegram received from a matched transmitter.</td>
    </tr>
    <tr>
        <td>Last User Data Received&nbsp;&nbsp;&nbsp;</td>
        <td>The user data portion of the last telegram received from a matched transmitter in binary format.</td>
    </tr>
    <tr>
        <td>Last Matched Paramerter&nbsp;&nbsp;&nbsp;</td>
        <td>The value of the last parameter matched. This parameter could be from the Instance property/Trigger or a Condition.</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Enocean Telegram Received

Fires when an Enocean device telegram is received.

The *Transmitters* in both the Instance properties and the Trigger can be used to filter out messages by sender. They are used in combination; the Instance property to define a set of transmitters and the Trigger to filter a specific set (or all) of those. Transmitters are defined in 32bit hex format, separated by semi-colons. By default, both are set to <code>FFFFFFFF</code> which mean any ID. If this appears anywhere in the *Transmitters* property, this will still be treated as any ID.

As the Enocean telegram does not contain the function and type of a device, setting the *Transmitters* ensures that other Instance Triggers firing erroneously. If transmitter IDs are currently unknown, it can be useful to set both the Instance and Trigger IDs to <code>FFFFFFFF</code> to discover the devices.

If the defining parameter of the telegram (eg. a button ID) matches the Instance properties and the defining parameter value is between the Trigger's *Value Range Minimum* and *Value Range Maximum*, and the transmitter ID matches an Instance/Trigger combination, the Trigger will match.

Trigger variables:

* &nbsp;*Variable 1*: The Transmitter ID in 32-bit hex format (*string e.g. "00329D64"*).
* &nbsp;*Variable 2*: The full Enocean user data in binary string format (*string e.g. "Enocean user data: 00010000000010000100011010000000"*).
* &nbsp;*Variable 3*: The last matched parameter value (*integer or real e.g. "21.5" or "128 out of 255*).

The full Enocean user data is used when *Additional Parameter Match* Conditions are used.

The last matched parameter value does not contain units or a description but these can be seen in the log when *Log Triggers and Conditions* is enabled. These values may be either an integer value or a real (float) value depending on the *Range Option*, *Scale Minimum* and *Scale Maximum* values.

### Additional Parameter Match

Matches in exactly the same way as the *Enocean Telegram Received* Trigger, but combines all of the Instance and Trigger properties together.

This is used when filtering out additional values, on top of the value matched in the Trigger. For example, the Instance parameters might look at the button ID, the Trigger would then be used to filter out buttons 1 to 3 and then a Condition could be used to filter out a button press value of 1.

The Condition uses the user data passed from the Trigger via the Trigger variables to extract values, so will only matched if called from an Enocean Telegram Received (ie. "Enocean user data: ..." exists as a Trigger variable).

The value from each Condition will be added to the end of the Trigger Variables:

* &nbsp;*Variable 1*: The Transmitter ID in 32-bit hex format (*string e.g. "00329D64"*).
* &nbsp;*Variable 2*: The full Enocean user data in binary string format (*string e.g. "00010000000010000100011010000000"*).
* &nbsp;*Variable 3*: The last matched parameter from the Trigger value (*integer or real e.g. "21.5" or "128 out of 255*).
* &nbsp;*Variable 4*: The last matched parameter value from the Condition (*integer or real e.g. "21.5" or "128 out of 255*).
* &nbsp;*Variable ...*: The last matched parameter value from the Condition (*integer or real e.g. "21.5" or "128 out of 255*).
* &nbsp;*Variable ...*: The last matched parameter value from the Condition (*integer or real e.g. "21.5" or "128 out of 255*).

[//]: # (### Actions)

[//]: # (#### Action Name)
[//]: # (#### Start with a verb such as "Sends..." or "Sets...")

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
