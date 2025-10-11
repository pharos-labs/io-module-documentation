# Dynalite DyNet - Version 2.6.0.BETA1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

<style type = "text/css">
    .config { width:100% }
    .config .td1 { text-align: right; padding: 0px 5px; background: #e6e6e6; }
    .config .td2 { padding: 0px 5px; }

    .portSupport { }
    .portSupport .td1 { text-align: right; padding: 0px 5px; background: #e6e6e6; }
    .portSupport .td2 { padding: 0px 5px; }

    .presetBank { width:100%; }
    .presetBank th { text-align: center; padding: 2px 5px; }
    .presetBank .tr1 { background: #c9c9c9; }
    .presetBank .tr2 { background: #e6e6e6; }
    .presetBank .tr3 { background: #f5f2f2; }
    .presetBank .td1 { text-align: center; padding: 0px 5px; background: #e6e6e6; } */
</style>

## Module Summary

Integrates the Controller with Philips Dynalite Systems.

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (This IO Module is stable and has been tested internally.)
**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this IO Module cannot perform)

### Release Notes

#### Version 2.6
* New combined module replacing *Dynalite DyNet (Serial)* and *Dynalite DyNet (IP)*

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

<hr>

## Requirements

In order for the Controller to be able to communicate with a DyNet Network, and its DyNet Devices, a connection must be made using the Ethernet Port (Mode IP), or the Controller's RS232/RS485 Serial Port (Mode Serial).

When using ethernet, a Philips Dynalite Ethernet Gateway (PDEG) is required.

## Configuration

### Via IP
When using IP as the connection mode, the following Configuration details maybe of use:

Configure your Philips Dynalite Ethernet Gateway (PDEG) with a fixed IP address from the Philips Dynalite System Builder.

To do so, go to the Port Editor tab, and add an IPv4 port with the following settings:

<div>
  <table class="config">
    <tr>
        <td class="td1">Port Type:</td>
        <td class="td2">DyNet 1 or DyNet 2</td>
    </tr>
    <tr>
        <td class="td1">Mode:</td>
        <td class="td2">Server</td>
    </tr>
    <tr>
        <td class="td1">Port Number:</td>
        <td class="td2">(PDEG Server Port Number)</td>
    </tr>
    <tr>
        <td class="td1">Protocol:</td>
        <td class="td2">UDP</td>
    </tr>
    <tr>
        <td class="td1">Connection:</td>
        <td class="td2">Spur or Trunk</td>
    </tr>
    <tr>
        <td class="td1">Area zero Transmit:</td>
        <td class="td2">Disabled</td>
    </tr>
    <tr>
        <td class="td1">Sign on at start up:</td>
        <td class="td2">Enabled</td>
    </tr>
    <tr>
        <td class="td1">Reply using Unicast Message:</td>
        <td class="td2">False</td>
    </tr>
  </table>
</div>

And add an additional IPv4 port with the following settings:<br>

<div>
  <table class="config">
    <tr>
      <td class="td1">Port Type:</td>
      <td class="td2">DyNet 1 or DyNet 2</td>
    </tr>
    <tr>
      <td class="td1">Mode:</td>
      <td class="td2">Client</td>
    </tr>
    <tr>
      <td class="td1">IP Address:</td>
      <td class="td2">(Network Primary)</td>
    </tr>
    <tr>
      <td class="td1">Port Number:</td>
      <td class="td2">(Port number)</td>
    </tr>
    <tr>
      <td class="td1">Protocol:</td>
      <td class="td2">UDP</td>
    </tr>
    <tr>
      <td class="td1">Connection:</td>
      <td class="td2">Spur or Trunk</td>
    </tr>
    <tr>
      <td class="td1">Area zero Transmit:</td>
      <td class="td2">Disabled</td>
    </tr>
    <tr>
      <td class="td1">Sign on at start up:</td>
      <td class="td2">Enabled</td>
    </tr>
    <tr>
      <td class="td1">Reply using Unicast Message:</td>
      <td class="td2">False</td>
    </tr>
  </table>
</div>

<hr>

## Operation

This IO Module uses a fixed set of OpCodes, the most common ones, from the DyNet protocol.
However, by using the *Custom Logical Command* Action, you can use any OpCode that is not currently supported by this IO Module's Actions.
This requires that you understand the DyNet Message Protocol, and the desired DyNet Command / OpCode you wish to send.
Refer to both the *Custom Logical Command* Action, and [Dynalite documentation](https://dynalite.com/) for more information on OpCodes.

For your information and convenience, Triggers and Actions specify the OpCode(s) used.

This IO Module is also capable of both sending, and receiving status requests to, and from, the DyNet Network.
By using request-type Triggers the Controller can receive status requests from the DyNet Network, and can respond using report-type Actions; conversely the Controller can use request-type Actions to make status requests from the DyNet Network, and use report-type Triggers to receive the response.
These Actions and Triggers contain either *Request* or *Report* in their names.

**Note** when using *Preset OpCodes* this IO Module only works with the Preset number directly, and deals with the DyNet Command bytes requirements for the Preset Bank internally (except for the Custom Logical Command Action).
Please see the Further Notes section at the bottom for more details.

### Instance Properties

The Instance Properties cover all the details for communicating with the DyNet Network.

<code>*Mode*</code> selects the physical connection type for communicating with the DyNet Network, be that ethernet if *IP* is selected, or a serial port with *Serial*.\
Properties are only visible based upon this *Mode*.

<code>*Port Type*</code> defines the default DyNet version to use for transmission of messages. For further details see *"DyNet 1 vs DyNet 2"* below.

You can also specify a default <code>*Area*</code> of the DyNet Network for each instance you create. This will make it easier to manage Triggers and Actions for a specific Area of the DyNet Network with which the Controller will be communicating.
It is thus recommended that each *Area* (of the DyNet Network) is dealt with by a separate instance of this IO Module, please read below for more details.

Checking the <code>*Extended Logging*</code> checkbox will provide more detailed log messages for fired Triggers and Actions as well as responses from the DyNet Network.

#### Mode IP
The <code>*PEDG IP Address*</code> defines the IP address for the Philips Dynalite Ethernet Gateway (PDEG).

Select the communication <code>*Protocol*</code> (TCP or UDP) as well as the <code>*PDEG Server Port Number*</code>, and <code>*Controller Port Number*</code>. These should match the settings configured for the PDEG.

#### Mode Serial
Use <code>*Serial Port*</code> to specify which physical port is communicating with the DyNet Network. The settings for communication with the DyNet Network over serial need to be set for the Controller from the Interfaces tab within the Network view of Designer. Use the following settings:

* &nbsp;Protocol: RS485.
* &nbsp;Baud Rate: 9600.
* &nbsp;Start and Stop Bits: 1.
* &nbsp;Parity: None.
* &nbsp;Data Bits: 8.

#### Using the Default Area

Within the *Default Area* specify the value for the Area within the DyNet Network that you wish to be considered the default Area for the given instance of this IO Module. Most Triggers and Actions have an *Area* property which can be set to *Instance Default*, meaning it will take the value given in the IO Module's Instance Properties. This means all the Triggers and Actions can be remapped onto different Areas from this one property. If, however, the *Area* property is set to any other value, the Triggers and Actions will use that given value over the default one.

### All Areas

DyNet devices are contained within isolated areas, however a commands can be directed to all areas by using the special area "0".
Devices must specifically setup to operate with area 0; please consult device documentation regarding this.

### DyNet 1 vs DyNet 2

Support for DyNet 2 is included with this module, while retaining compatibility with DyNet 1.

DyNet 2 expands the allowable ranges for Area and Preset numbers.
Setting a value outside of the allowable range for DyNet 1 will result in the message being logged and dropped.

<table class="portSupport">
  <tr>
    <td class="td1" >DyNet 1:</td>
    <td class="td2">
      Areas 1 to 255<br>
      Channels 1 to 255<br>
      Fade Time 0 to
      <ul>
        <li>21 Min 50 Sec <i>(OpCode 0x00, 0x01, 0x02, 0x03)</i></li>
        <li>25.5 Sec <i>(OpCode 0x71)</i></li>
        <li>4 Min 15 Sec <i>(OpCode 0x72)</i></li>
        <li>4 Hrs 15 Min <i>(OpCode 0x73)</i></li>
        <li>5.1 Sec <i>(OpCode 0x80, 0x81, 0x82, 0x83)</i></li>
      </ul>
      Presets 1 to 2048<br>
    </td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2">
      Areas 1 to 65535<br>
      Channels 1 to 65535<br>
      Fade Time 0 to 23.3 Hours<br>
      Presets 1 to 65519<br>
    </td>
  </tr>
</table>

Some actions, trigger, et cetera; are only appropriate for DyNet 1 or DyNet 2.
If the selected port type is not support by the action or trigger, then the supported port type will be used in place. e.g. If *Set Area Level* had only support for DyNet 1, but DyNet 2 was selected as the instances *Port Type*, then the DyNet 1 would still be used to send the *Set Area Level* message.
Support status will be noted below.

While the configuration requires that either DyNet 1 or DyNet 2 is selected for transmission, the controller will allow reception of both DyNet 1 and DyNet 2 concurrently.

<hr>

### Triggers

#### Online Reported

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCodes 0 (0x00)<br>
    </td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2"><i>Not yet supported</i></td>
  </tr>
</table>

This Trigger fires when the controller receives an OpCode reporting the online status (signon) for a specified *Device Code* and *Box Number* on the DyNet Network.

The variables this Trigger receives and passes onto the Action are:

1. &nbsp;*Device code* (<code>integer</code>): Reported Device code.
1. &nbsp;*Box number* (<code>integer</code>): Reported Box number.

#### Set Area to User Preset

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCodes*<br>
        1 (0x01), 2 (0x02), 3 (0x03), 4 (0x04)<br>
        10 (0x0A), 11 (0x0B), 12 (0x0C), 13 (0x0D)
    </td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2">OpCode 1 (0x01)</td>
  </tr>
</table>

<i>*The OpCode for this Trigger is variable as it specifies the Preset number, please see the Further Notes section at the bottom for more details.</i>

This Trigger fires when the controller receives an OpCode to set an Area of the DyNet Network to a user Preset.

Set the Trigger to fire for the desired *Area* that can either be the *Instance Default* specified one, or any desired (<code>integer</code>) value.

Using *Preset* specify whether you wish the Trigger to fire for *Any* Preset, or a specific one using a value (<code>integer</code>).

The variables this Trigger receives and passes onto the Action are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
1. &nbsp;*Preset* (<code>integer</code>): Specified Preset for the given Area.
1. &nbsp;*Fade time* (seconds as <code>integer</code>): Time over which the change to the specified Preset will occur, usually set to 0.

#### Set Area Level

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 121 (0x79)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2"><i>OpCode 16 (0x10) SubOpCode 2 (0x02)</i></td>
  </tr>
</table>

This Trigger fires when the Controller receives the OpCode to change the level for a specified Area of the DyNet Network.

Set the Trigger to fire for the desired *Area* that can either be the *Instance Default* specified one, or any desired (<code>integer</code>) value.

The variables this Trigger receives and passes onto the Action are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
1. &nbsp;*Level* (percentage as <code>integer</code>): Level to be set for the specified Area.
1. &nbsp;*Fade time* (seconds as <code>integer</code>): Time over which the change to the specified level will occur, usually set to 0.

#### Set Channel Level

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 113 (0x71) <i>Fade Time</i> specified in deciseconds*<br>
        OpCode 114 (0x72) <i>Fade Time</i> specified in seconds<br>
        OpCode 115 (0x73) <i>Fade Time</i> specified in minutes*<br>
    </td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2">OpCode 16 (0x10) SubOpCode 2 (0x02)</td>
  </tr>
</table>

**Fade Time* is converted into seconds for the variable it passes onto Actions.

This Trigger fires when the Controller receives the OpCode to change the level for a Channel within an Area of the DyNet Network.

Set the Trigger to fire for the desired *Area* that can either be the *Instance Default* specified one, or any desired (<code>integer</code>) value.

Using *Channel* specify whether you wish the Trigger to fire for *Any* Channel, or a specific one set using a value (<code>integer</code>).

The variables this Trigger receives and passes onto the Action are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
1. &nbsp;*Channel* (<code>integer</code>): Specified affected Channel for the given Area.
1. &nbsp;*Level* (percentage as <code>integer</code>): Level to be set for the Channel.
1. &nbsp;*Fade time* (seconds as <code>integer</code>): Time over which the change to the specified level will occur, usually set to 0.

**Note** if you wish to pass the *Fade Time* variable onto an Action, you will need to use the *Set Channel Level (seconds)* Action.

#### Increment Area Level

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 6 (0x06)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2"><i>Not yet supported</i></td>
  </tr>
</table>

This Trigger fires when the Controller receives the OpCode to increment the level for a specified Area of the DyNet Network.

Set the Trigger to fire for the desired *Area* that can either be the *Instance Default* specified one, or any desired (<code>integer</code>) value.

The variables this Trigger receives and passes onto the Action are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.

#### Decrement Area Level

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 5 (0x05)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2"><i>Not yet supported</i></td>
  </tr>
</table>

This Trigger fires when the Controller receives the OpCode to decrement the level for a specified Area of the DyNet Network.

Set the Trigger to fire for the desired *Area* that can either be the *Instance Default* specified one, or any desired (<code>integer</code>) value.

The variables this Trigger receives and passes onto the Action are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.

#### Set Area to Off

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 4 (0x04)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2"><i>Not yet supported</i></td>
  </tr>
</table>

This Trigger fires when the Controller receives the OpCode to set an Area of the DyNet Network to off.

The variables this Trigger receives and passes onto the Action are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
1. &nbsp;*Fade time* (seconds as <code>integer</code>): Time over which the change to the specified Preset will occur, usually set to 0.

#### Request Channel Level

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 97 (0x61)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2">OpCode 34 (0x22) SubOpCode 0 (0x00)</td>
  </tr>
</table>

This Trigger fires when the Controller receives the OpCode requesting information (by the DyNet Network) about the current set level for a specified Channel within an Area of the DyNet Network.

Set the Trigger to fire for the desired *Area* that can either be the *Instance Default* specified one, or any desired (<code>integer</code>) value.

Using *Channel* specify whether you wish the Trigger to fire for *Any* Channel, or a specific one set using a value (<code>integer</code>).

Use the *Target Level Minimum* & *Target Level Maximum*, and *Current Level Minimum* & *Current Level Maximum* to filter out the range within which the Trigger should fire.

The variables this Trigger receives and passes onto the Action are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
1. &nbsp;*Channel* (<code>integer</code>): Specified affected Channel for the given Area.

#### Channel Level Reported

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 96 (0x60)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2">OpCode 35 (0x23) SubOpCode 0 (0x00)</td>
  </tr>
</table>

This Trigger fires when the Controller receives the OpCode reporting the current level for a specified Channel within an Area of the DyNet Network.

Set the Trigger to fire for the desired *Area* that can either be the *Instance Default* specified one, or any desired (<code>integer</code>) value.

Using *Channel* specify whether you wish the Trigger to fire for *Any* Channel, or a specific one set using a value (<code>integer</code>).

The variables this Trigger receives and passes onto the Action are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
1. &nbsp;*Channel* (<code>integer</code>): Specified affected Channel for the given Area.
1. &nbsp;*Target Level* (percentage as <code>integer</code>): The level the Channel is fading towards (if it is currently fading).
1. &nbsp;*Current Level* (percentage as <code>integer</code>): The current level for the Channel.

#### Requested Current Preset
<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 99 (0x63)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2">OpCode 32 (0x20) SubOpCode 0 (0x00)</td>
  </tr>
</table>

This Trigger fires when the Controller receives the OpCode requesting information (by the DyNet Network) about the current Preset being used for a specified Area of the DyNet Network.

Set the Trigger to fire for the desired *Area* that can either be the *Instance Default* specified one, or any desired (<code>integer</code>) value.

Using *Preset* specify whether you wish the Trigger to fire for *Any* Preset, or a specific one set using a value (<code>integer</code>).

The variables this Trigger receives and passes onto the Action are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.

#### Current Preset Reported

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 98 (0x62)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2"><i>Not yet supported</i></td>
  </tr>
</table>

This Trigger fires when the Controller receives the OpCode reporting the current Preset for a specified Area of the DyNet Network.

Set the Trigger to fire for the desired *Area* that can either be the *Instance Default* specified one, or any desired (<code>integer</code>) value.

Using *Preset* specify whether you wish the Trigger to fire for *Any* Preset, or a specific one set using a value (<code>integer</code>).

The variables this Trigger receives and passes onto the Action are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
1. &nbsp;*Preset* (<code>integer</code>): Specified Preset for the given Area.

#### DALI Ballast Status Reported

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">Physical OpCode 76 (0x4D) SubOpCode 1 (0x01)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2">OpCode 131 (0x83) SubOpCode 259 (0x0103)</td>
  </tr>
</table>

This Trigger fires when the Controller receives the OpCode reporting the current DALI Ballast Status for a specified *Channel* of the DyNet Network.

Using *Device code*, *Box number*, and *Channel*; specify whether you wish the Trigger to fire for *Any* Channel, or a specific one set using a value (<code>integer</code>).

The variables this Trigger receives and passes onto the Action are:

1. &nbsp;*Device* (<code>integer</code>): Source device code.
1. &nbsp;*Box* (<code>integer</code>): Source box number.
1. &nbsp;*Channel* (<code>integer</code>): Specified affected Channel of the DyNet Network.
1. &nbsp;*Ballast Status* (<code>integer</code>): Status of control gear; "0" = OK.
1. &nbsp;*Lamp failure* (<code>integer</code>): Status of Lamp; "0" = OK.
1. &nbsp;*Lamp arc power on* (<code>integer</code>): Status of Lamp arc power on; "0" = OFF.
1. &nbsp;*Limit Error* (<code>integer</code>): Status of Limit Error; "0" = Last requested arc power level is between
MIN and MAX LEVEL or OFF
1. &nbsp;*Fade Running* (<code>integer</code>): Status of Fade running; "0" = fade is ready; "1" = fade is running
1. &nbsp;*Reset State* (<code>integer</code>): Status of reset; 0" = "No"
1. &nbsp;*Short Address Missing* (<code>integer</code>): Missing short address? "0" = "No"
1. &nbsp;*Power failure* (<code>integer</code>): Status since power failure; "0" = "No"; "RESET" or an arc power control
command has been received since last power-on.

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

<hr>

### Actions

#### Report Device Online

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">Physical OpCode 0 (0x00)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2"><i>DyNet 1 is always used for this action</i></td>
  </tr>
</table>

This Action sends a Device Identify.

#### Request Device Online

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">Physical OpCode 128 (0x80)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2"><i>DyNet 1 is always used for this action</i></td>
  </tr>
</table>

This Action sends an OpCode to the DyNet Network requesting the online status of the device matching *Device code* and *Box number*.

The values / variables this Action uses are:

1. &nbsp;*Device code* (<code>integer</code>): Specified affected Device code.
1. &nbsp;*Box number* (<code>integer</code>): Specified affected Box number.

#### Set Area to User Preset

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCodes*<br>
        1 (0x01), 2 (0x02), 3 (0x03), 4 (0x04)<br>
        10 (0x0A), 11 (0x0B), 12 (0x0C), 13 (0x0D)
    </td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2">OpCode 1 (0x01)</td>
  </tr>
</table>

<i>*The OpCode for this Trigger is variable as it specifies the Preset number, please see the Further Notes section at the bottom for more details.</i>

This Action sets an Area of the DyNet Network to a specified user Preset.

The values / variables this Action uses are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
1. &nbsp;*Preset* (<code>integer</code>): Specified Preset for the given Area.
1. &nbsp;*Fade time* (seconds as <code>integer</code>): Time over which the change to the specified Preset will occur, usually set to 0.

#### Set Area Level

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 121 (0x79)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2"><i>OpCode 16 (0x10) SubOpCode 2 (0x02)</i></td>
  </tr>
</table>

This Action sets an Area of the DyNet Network to a given level.

The values / variables this Action uses are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
1. &nbsp;*Level* (percentage as <code>integer</code>): Level to be set for the specified Area.
1. &nbsp;*Fade time* (seconds as <code>integer</code>): Time over which the change to the specified level will occur, usually set to 0.

#### Fade Channel to Level (seconds)

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 114 (0x72)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2">OpCode 16 (0x10) SubOpCode 2 (0x02)</td>
  </tr>
</table>

This Action sets a level for a Channel within an Area of the DyNet Network, the *Fade Time* is specified in seconds.

The values / variables this Action uses are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
1. &nbsp;*Channel* (<code>integer</code>): Specified affected Channel for the given Area.
1. &nbsp;*Level* (percentage as <code>integer</code>): Level to be set for the specified Channel, usually set to 100.
1. &nbsp;*Fade time* (seconds as <code>integer</code>): Time over which the change to the specified level will occur, usually set to 0.

#### Fade Channel to Level (minutes)

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 115 (0x73)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2">OpCode 16 (0x10) SubOpCode 2 (0x02)</td>
  </tr>
</table>

This Action sets the level for a Channel within an Area of the DyNet Network, the *Fade Time* is specified in minutes.

The values / variables this Action uses are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
1. &nbsp;*Channel* (<code>integer</code>): Specified affected Channel for the given Area.
1. &nbsp;*Level* (percentage as <code>integer</code>): Level to be set for the specified Channel, usually set to 100.
1. &nbsp;*Fade time* (minutes as <code>integer</code>): Time over which the change to the specified level will occur, usually set to 0.

#### Set Channel n to Level with Fade

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCodes*<br>
        128 (0x80), 129 (0x81), 130 (0x82), 131 (0x83)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2">OpCode 16 (0x10) SubOpCode 2 (0x02)</td>
  </tr>
</table>

*The specific OpCode used is calculated internally and depends on the channel number.

This Action sets a level for a Channel within an Area of the DyNet Network, the *Fade Time* is specified in seconds.



The values / variables this Action uses are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
1. &nbsp;*Channel* (<code>integer</code>): Specified affected Channel for the given Area.
1. &nbsp;*Level* (percentage as <code>integer</code>): Level to be set for the specified Channel, usually set to 100.
1. &nbsp;*Fade time* (seconds as <code>integer</code>): Time over which the change to the specified level will occur, usually set to 0.

#### Increment Area Level

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 6 (0x06)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2"><i>Not yet supported</i></td>
  </tr>
</table>

This Action increments the level for an Area of the DyNet Network.

The values / variables this Action uses are:

* &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
* &nbsp;*Fade time* (seconds as <code>integer</code>): Time over which the change to the specified level will occur, usually set to 0.

#### Decrement Area Level

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 5 (0x05)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2"><i>Not yet supported</i></td>
  </tr>
</table>

This Action decrements the level of an Area of the DyNet Network.

The values / variables this Action uses are:

* &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
* &nbsp;*Fade time* (seconds as <code>integer</code>): Time over which the change to the specified level will occur, usually set to 0.

#### Set Area to Off

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 4 (0x04)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2"><i>Not yet supported</i></td>
  </tr>
</table>

This Action turns off an Area of the DyNet Network.

The values / variables this Action uses are:

* &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
* &nbsp;*Fade time* (seconds as <code>integer</code>): Time over which the turning off the Area will occur, usually set to 0.

#### Request Channel Level

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 97 (0x61)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2">OpCode 34 (0x22) SubOpCode 0 (0x00)</td>
  </tr>
</table>

This Action sends an OpCode to the DyNet Network requesting information about the current level of a specified Channel within an Area.

The values / variables this Action uses are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
1. &nbsp;*Channel* (<code>integer</code>): Specified affected Channel for the given Area.

#### Channel Level Report

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 96 (0x60)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2">OpCode 35 (0x23) SubOpCode 0 (0x00)</td>
  </tr>
</table>

This Action sends an OpCode to the DyNet Network giving information about the current level of a specified Channel within an Area.

The values / variables this Action uses are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
2. &nbsp;*Channel* (<code>integer</code>): Specified affected Channel for the given Area.
3. &nbsp;*Level* (percentage as <code>integer</code>): The current level for the Channel.

#### Request Current Preset

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 99 (0x63)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2">OpCode 32 (0x20) SubOpCode 0 (0x00)</td>
  </tr>
</table>

This Action sends an OpCode to the DyNet Network requesting information about the current Preset being used for a specified Area.

The values / variables this Action uses are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.

#### Report Current Preset

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">OpCode 98 (0x62)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2">OpCode 33 (0x21) SubOpCode 0 (0x00)</td>
  </tr>
</table>

This Action sends an OpCode to the DyNet Network giving information about the current Preset being used for a specified Area.

The values / variables this Action uses are:

1. &nbsp;*Area* (<code>integer</code>): Specified affected Area of the DyNet Network.
1. &nbsp;*Preset* (<code>integer</code>): Specified Preset for the given Area.

#### Request DALI Ballast Status

<table class="portSupport">
  <tr>
    <td class="td1">DyNet 1:</td>
    <td class="td2">Physical OpCode 76 (0x4C) SubOpCode 1 (0x01)</td>
  </tr>
  <tr>
    <td class="td1">DyNet 2:</td>
    <td class="td2"><i>Not yet supported</i></td>
  </tr>
</table>

[//]: # (DyNet 2 OpCode 130 SubOpCode 259 has been disabled)

This Action sends an OpCode to the DyNet Network requesting information about the current DALI ballast status for the specified *Channel* on device matching *Device code* and *Box number*.

The values / variables this Action uses are:

1. &nbsp;*Device code* (<code>integer</code>): Specified affected Device code.
1. &nbsp;*Box number* (<code>integer</code>): Specified affected Box number.
1. &nbsp;*Channel* (<code>integer</code>): Specified affected Channel.

#### Custom Logical Command

This Action allows the user to pass any OpCode to the DyNet Network. To use this requires that an understanding of the DyNet Message Protocol, and the desired DyNet Command / OpCode you wish to send. Please refer to the [Dynalite documentation](https://dynalite.com/) for more information on OpCodes.

Of the 8 bytes required to send a DyNet Command, 3 have default / automatically calculated values:

* &nbsp;1st Byte (Byte 0): this is the Logical Address or Sync Byte and has a default value of 28 (0x1C).
* &nbsp;7th Byte (Byte 6): this is the Join Code and has a default value of 255 (0xFF).
* &nbsp;8th Byte (Byte 7): this is the Checksum for the packet and is automatically calculated by this IO Module.

The remaining 5 bytes are the values / variables this Action uses:

1. &nbsp;Area: 2nd Byte (Byte 1) - this specifies the *Area* affected by the DyNet Command, it can be set to either be the *Instance Default* specified one, or any desired (<code>integer</code>) value.
2. &nbsp;Data 1: 3rd Byte (Byte 2) - see below\*
3. &nbsp;OpCode: 4th Byte (Byte 3) - this is the OpCode byte, specify the desired OpCode (<code>integer</code>) for the command you wish to send.
4. &nbsp;Data 2: 5th Byte (Byte 4) - see below\*
5. &nbsp;Data 3: 6th Byte (Byte 5) - see below\*

\* These variables carry different information depending on the OpCode being sent, please look these up. **Note** They can take any <code>integer</code> value including zero, or simply be left as *0 (Not Used)* since some OpCodes do not use some of these bytes.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

<hr>

## Support

If you encounter any issues with this IO Module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of IO Module use)

## Further Notes

The OpCode to specify the Preset number works a little differently as it can take multiple values and works together with the <code>Preset Bank</code>.
The <code>Preset OpCode</code> specifies the chosen Preset number within the specified <code>Preset Bank</code> of the full DyNet Command. There are only 8 possible <code>Preset OpCodes</code>: 0-3 and 10-13, and the <code>Preset Bank</code> will determine what Preset number each of these OpCodes relates to. <code>Preset Bank = 0</code> holds Preset numbers 1 through 8, and <code>Preset Bank = 1</code> holds Preset numbers 9 through 16, and so on.
Hence the two need to be specified together to obtain the desired Preset number: a <code>Preset OpCode = 12</code> and <code>Preset Bank = 2</code> gives Preset number 23 (P23 for short). Below is a summary of these:

<div>
<table class="presetBank">
    <tr class="tr1">
        <th rowspan="3">DyNet 1<br>OpCode</th>
        <th colspan="4">Preset Bank</th>
    </tr>
    <tr class="tr2">
        <th>0</th>
        <th>1</th>
        <th>2</th>
        <th>3</th>
    </tr>
    <tr class="tr3">
        <td>(P1-8)</td>
        <td>(P9-16)</td>
        <td>(P17-24)</td>
        <td>(P25-32)</td>
    </tr>
    <tr>
        <td class="td1">0 (0x00)</td>
        <td>P1</td>
        <td>P9</td>
        <td>P17</td>
        <td>P25</td>
    </tr>
    <tr>
        <td class="td1">1 (0x01)</td>
        <td>P2</td>
        <td>P10</td>
        <td>P18</td>
        <td>P26</td>
    </tr>
    <tr>
        <td class="td1">2 (0x02)</td>
        <td>P3</td>
        <td>P11</td>
        <td>P19</td>
        <td>P27</td>
    </tr>
    <tr>
        <td class="td1">3 (0x03)</td>
        <td>P4</td>
        <td>P12</td>
        <td>P20</td>
        <td>P28</td>
    </tr>
    <tr>
        <td class="td1">10 (0x0A)</td>
        <td>P5</td>
        <td>P13</td>
        <td>P21</td>
        <td>P29</td>
    </tr>
    <tr>
        <td class="td1">11 (0x0B)</td>
        <td>P6</td>
        <td>P14</td>
        <td>P22</td>
        <td>P30</td>
    </tr>
    <tr>
        <td class="td1">12 (0x0C)</td>
        <td>P7</td>
        <td>P15</td>
        <td>P23</td>
        <td>P31</td>
    </tr>
    <tr>
        <td class="td1">13 (0x0D)</td>
        <td>P8</td>
        <td>P16</td>
        <td>P24</td>
        <td>P32</td>
    </tr>
</table>
</div>
