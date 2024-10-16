# Thermokon Li65+ Lux-Temperature RS485 Sensor - Version 2.1.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Reads lux and temperature values from a Thermokon Li65+ sensor over RS485, using the Modbus RTU protocol.

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (This IO Module is stable and has been tested internally.)
[//]: # (**Note:** Please be aware that this is an beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope

This module can currently only be used with LPCs and TPCs with attached RIOs. It can not currently be used with LPCX, VLC and VLC+ controllers.

### Release Notes

#### Version 2.1

* &nbsp;Increased maximum *Polling time* (300s)
* &nbsp;Fixed bug ranges not reponsive to values.

#### Version 2.0

* &nbsp;Initial release.
* &nbsp;Added *Lux Level Changed* Trigger.
* &nbsp;Added *Temperature Changed* Trigger.
* &nbsp;Added *Start Polling* Action.
* &nbsp;Added *Stop Polling* Action.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

## Configuration

The Thermokon Li65++ Temp RS485 Modbus device will need settings matching the module to be compatible.
For more information see the [device datasheet](https://www.thermokon.de/direct/alterra-base/mimes/get/04f36050786d2b9fc).

The DIP switches on board of the device should be configured as below.

**Measuring DIP switches (set of 6 switches)**

Light range (0 to 50 kLux):
* &nbsp;DIP 1: On
* &nbsp;DIP 2: Off
* &nbsp;DIP 3: On

Temperature range (-20°C to +80°C):
* &nbsp;DIP 4: Off
* &nbsp;DIP 5: Off

Units (SI)
* &nbsp;DIP 6: Off

**Addressing DIP switches (top row of 5 switches)**

* &nbsp;DIPs 1 - 5: Modubs slave address/ID set in binary format. By default, both the Li65+ and the module use ID 1.

If more than one Li65+ devices are being used, they must have unique addresses/slave IDs and a new module Instance must be used for each.

**Addressing DIP switches (bottom row of 5 switches)**

Termination (Off)
* &nbsp;DIP 1: Off

Baud rate (9600)
* &nbsp;DIP 2: Off
* &nbsp;DIP 3: Off

Parity (None)
* &nbsp;DIP 4: Off
* &nbsp;DIP 5: Off

**Designer Port Configuration**

The serial port of the Controller (whether local or a RIO) must be configured in the Network tab > Interfaces settings.

* &nbsp;Mode: RS485
* &nbsp;Baud Rate: 9600
* &nbsp;Parity: None

## Operation

### Instance Properties

The *Serial Port* must be the same as the previously configured *Serial Port* in the Network tab.

The *Modubs Slave ID* must match that set on the Li65+ device. By default, both the Li65+ and the modules use ID 1.
If more than one Li65+ devices are being used, they must have unique addresses/slave IDs and a new module Instance must be used for each.

Lux and temperature values are requested from the Li65+ by polling. The *Poll Time* determines how often to retrieve the values.
If both *Lux* and *Temperature* are set to poll in the *Start Polling* Action, both will use the same *Poll Time* but for reliability,
the temperature will be requested two seconds behind the lux level.

If *Log Trigger Matches Logging* is enabled, non-matched triggers will be logged with a reason as to why it was not matched.
This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

### Status Variables

The values can be viewed on the IO Module tab of the web interface.

* &nbsp;Current Lux Level (lux)
* &nbsp;Current Temperature (degrees Celcius)

### Triggers

#### Lux Level Changed

Fires when a lux level is received from the Li65+.

If the *Match Type* is <code>Enters Range</code>, if the previous value was not between the *Minimum* and *Maximum* values but the new value is,
the trigger will be fired and the new lux level will be passed as Trigger variable *1*. If the previous value was already in the range,
the trigger will not fire.

If the *Match Type* is <code>Changes within Range</code>, if the new value is between the *Minimum* and *Maximum* values and not the same as the
previous value, the Trigger will fire and the lux level will be passed as Trigger variable <code>1</code>.

#### Temperature Changed

Fires when a temperature value is received from the Li65+.

If the *Match Type* is <code>Enters Range</code>, if the previous value was not between the *Minimum* and *Maximum* values but the new value is,
the trigger will be fired and the new temperature value will be passed as Trigger variable *1*. If the previous value was already in the range,
the trigger will not fire.

If the *Match Type* is <code>Changes within Range</code>, if the new value is between the *Minimum* and *Maximum* values and not the same as the
previous value, the Trigger will fire and the temperature value will be passed as Trigger variable <code>1</code>.

[//]: # (### Conditions)

[//]: # (#### Conditions Name)
[//]: # (#### Start with a verb such as "Is met when..." or "Returns true if...")

### Actions

#### Start Polling

Starts/enables the poll timer using the interval set in the Instance property, *Poll Time*. By default, both *Lux* and *Temperature* values will be queried,
but the properties can be used to poll just *Lux* or *Temperature*.

This Action must be used to start the querying of values. Without starting the poll timer, Triggers will not fire.

If both *Lux* and *Temperature* are set to poll, both will use the same *Poll Time* but for reliability,
the temperature will be requested two seconds behind the lux level.

#### Stop Polling

Stops/disables the poll timer. By default, both *Lux* and *Temperature* will cease being polled,
but the properties can be used to stop just *Lux* or *Temperature* polling.

Polling can be resumed using the *Start Polling* action.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
