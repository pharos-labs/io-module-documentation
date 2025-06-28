# Level Developments LCH-360 - Version 2.1.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Receives angle values from the Level Developments LCH-360 Single Axis Inclinometer Sensor, over an RS232 serial port.

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)
This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1
* Improved serial buffer management

#### Version 2.0

* &nbsp;Updated module documentation.
* &nbsp;Added *Set Transmission Rate* action.
* &nbsp;Added status variables.
* &nbsp;Added *Maximum Forward Step* and *Maximum Backwards Step* to smooth anomalous values.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

## Configuration

Connect the LCH-360 sensor via the RS232 port of either the Controller or a connected RIO Remote Device. Note the serial port number the LCH-360 sensor has been connected to as this will be needed in the Instance Properties.

It is recommended to set the controller log to Extended to prevent the Serial Input log messages from being displayed as often as the *Transmission Rate* set within the Instance Properties.

## Operation

Once connected the LCH-360 sensor is capable of sending both a stream of constant angle values at a regular interval, and provide an angle value when requested.

The regular interval of angle value transmission can be set by adjusting the *Transmission Rate* value in the Instance Properties. Whereas, running the *Get Angle* Action will send a request for a single angle value.

If the *Transmission Rate* is set to <code>0s</code> then the LCH-360 sensor will not transmit any angle values unless requested to do so by the *Get Angle* Action.

All angle values received will fire the *Get Angle Input* Trigger and can be passed as variables.

### Instance Properties

Specify the *Serial Port* to which the LCH-360 sensor has been connected by selecting the device and port number of the used RS232 connection used.

When the *Transmission Rate* is set to a non-zero value this specifies the time interval, or rate, at which the LCH-360 sensor will send angle values. In such a case the LCH-360 sensor will begin sending values as soon as the Controller has started up and transmitted the *Transmission Rate* request to the LCH-360 sensor.

The *Transmission Rate* can be either <code>0s</code>, or a value between <code>0.100s</code> and <code>9.999s</code>. If the *Transmission Rate* is set to <code>0s</code> then the LCH-360 sensor will only provide angle values when requested by the *Get Angle* Action.

The *Offset* parameter allows the specification of a constant angle offset from the received value. The offset adds degrees in the specified *Offset* degrees in a clockwise direction. This can be useful to correctly align lighting displays that have a required orientation.

Whenever smooth image rotation is key, it is possible to dial in the *Maximum Forward Step* and *Maximum Backward Step* possible in degrees for each new value received from the LCH-360. The default value is 180 degrees which allows any new value received from the LCH-360 to be accepted. These parameters also ensure that any momentary anomalous value that could be received is prevented from causing an image rotation to flicker or back track in an undesirable manner.

**NOTE** that the *Maximum Forward Step* and *Maximum Backward Step* are **advanced** Instance Properties that will require fine tuning to make them perform as desired, especially when working with small angle margins. It is also worth taking extra care in such a situation that if the installation is knocked in a way that advances the degrees by a value greater than the maximum step values, then it will be out of sync and would need to be reset.

### Triggers

This Trigger fires when the Controller receives an angle value from the LCH-360 sensor.

The angle received is a percentage value expressed as a number between 0 to 1, corresponding to 0 and 360 degrees.

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

### Actions

##### Enable

This Action will request the LCH-360 sensor to begin transmitting a constant stream of angle values according at the rate specified by the *Transmission Rate* within the Instance Properties.

##### Disable

This Action will request the LCH-360 sensor to stop transmitting a constant stream of angle values.

It will still be possible to receive angle values by using the *Get Angle* Action.

##### Get Angle

This Action sends a request to the LCH-360 sensor to provide an angle value. Once this has been sent by the LCH-360 sensor it can be received by the *Get Angle Input* Trigger.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
