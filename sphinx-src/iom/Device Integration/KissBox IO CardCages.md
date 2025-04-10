# KissBox IO CardCages - Version 2.1.3

## Module Summary

[//]: # (Describe as briefly and clearly the role of the module)
Reads and writes values to and from KissBox I/O-Cards in a KissBox I/O CardCage IO3CC or IO8CC.

## Module Status

This IO Module is stable and has been tested internally, and on live project.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Release Notes

#### Version 2.1.3

* &nbsp; Adds instance property *Card Cage* to limit operations on non-existent slots.

#### Version 2.1.2

* &nbsp; Adds helper action *Toggle Digital Channel*.

#### Version 2.1.1

* &nbsp;For a digital output, any value > 0 will be displayed as true.

**Note:** This only affects display in logs and status variables, not operation. When writing a digital *Value* using this Action, any value greater than 0 will work,
but conventionally, a value of <code>1</code> should be used.
Alternatively, use the *Write Digital Channel* Action.

#### Version 2.1

* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;General updates and improvements.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

## Configuration

This module works with the KissBox IO8CC and the IO3CC.

Use KissBox Editor to configure your KissBox I/O Mode Setup to UDP mode with the Destination IP Address set to the IP Address of your Network Primary.
A Port should be chosen and entered in the KissBox Configuration.

The Input card should be configured with Automatic Time Control (or the Read Channel/Read All Channels Action should be used to query the inputs).
As well as setting the UDP port in the main configuration window, the destination port must be set in "I/O Mode Setup" dialog which can be accessed by double-clicking on the gateway node in the browser panel.
The Controller IP address can be optionally specified.

**Note:** Your KissBox I/O must be running the TCP/UDP Firmware, not the Art-Net firmware.

## Operation

### Instance Properties

Set *KissBox IP Address* to the IP Address of the KissBox I/O.

Set *KissBox UDP Port* to the UDP Port set in the Network Configuration of the CardCage.

Set *Local Port* should be set to the same Port number as in the I/O Mode Setup of the CardCage.

If *Check at Startup* is checked the Controller will query the state of the inputs and fire Triggers accordingly.

The *Connection Poll* property defines how often the Controller checks whether the KissBox is accessible on the network
, and will fire a *Connection Status Changed* Trigger (if one exist in the show) when the status changes.

*Card Cage* selects the number of slots KissBox Card Cage type, and alters the number of available slots for configuration.

*Slot [x] Card* - Selecting the Card type will enable displaying the current status of each card on the Controller's Web Interface.

Checking *Extended Logging* will provide extra log messages for diagnostic purposes.

### Triggers

#### Digital Input Value Received

Fires when a digital value is received from the KissBox I/O CardCage specified in the Instance properties. The *Slot* and *Channel* can be used to filter out required values.

#### Analog Input Value Received

Fires when an analog value is received from the KissBox I/O CardCage specified in the Instance properties. The *Slot* and *Channel* can be used to filter out required values.

#### Connection Status Changed

Fires when a TCP socket is opened or closed, or when polled or queried, the KissBox I/O CardCage has not responded.

### Actions

#### Read Channel

Requests the value of a single *Channel* on a specified *Slot*. The response will fire the relevant *Digital Input Value Received* or *Analog Input Value Received* Trigger, dependant on the value type received.

#### Read All Channels

Requests all values on a specified *Slot*. The response will fire multiple *Digital Input Value Received* or *Analog Input Value Received* Triggers, dependant on the value types received.

#### Write Channel

Writes a single analog or digital *Value* of a *Channel* on a specified *Slot*.

When writing a digital *Value* using this Action, any value greater than 0 will work, but conventual, a value of <code>1</code> should be used.
Alternatively, use the *Write Digital Channel* Action.

#### Write All Channels

Writes all channels on a specified *Slot* with the values specified as a comma separated list.

An example for a 3 channel analog slot would be *8,16,32*.

When writing a digital *Value* using this Action, any value greater than 0 will work, but conventual, a value of <code>1</code> should be used.
Alternatively, use the *Write All Digital Channels* Action.

An example for an 8 channel digital slot would be *1,1,1,1,0,0,0,0*.

####  Write Digital Channel

Writes a single digital *Value* of a *Channel* on a specified *Slot*.

#### Write All Digital Channels

Writes all digital channels on a specified *Slot*, using the drop-down boxes to specify a value per channel.

#### Toggle Digital Channel

Toggles the value of a single digital *Channel* on a specified *Slot*.

#### Start Polling Values

Continually requests the values of slots using the time specified in the *Connection Poll* Instance variable.

#### Stop Polling Values

Stops the poll timer to stop requesting values.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
