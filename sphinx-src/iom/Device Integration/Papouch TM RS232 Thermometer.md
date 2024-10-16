# Papouch TM RS232 Thermometer - Version 2.1.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Fires a trigger when live temperature values are received from the Papouch TM RS232 Thermometer and passes the value to an action as a trigger variable.

## Module Status

[//]: # (If still desired provide a status of the module)

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (#### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1

* &nbsp;Updated documentation.
#### Version 2.0

[//]: # (Provide a history of the release updates to the module for the end user)

* &nbsp;General updates and improvements.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*


[//]: # (### Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

## Configuration

This module requires a Papouch Temperature Sensor connected to a RS232 serial input on a controller. The sensor is powered by the serial bus and once the serial connection is initiated, the sensor will send the current temperature every 10 seconds as an ASCII string. The string is parsed within the module and passed as a trigger variable.

## Operation

### Instance Properties

The *Serial Port* is the physical local port that the sensor is attached to.

[//]: # (#### Conditions)
[//]: # (Conditions are other criteria that need to be met after a Trigger to activate an Action)

### Triggers

#### Temperature Received

The trigger will fire when the captured temperature is greater than or equal to the *Minimum* temperature *and* less than or equal to the *Maximum* temperature.
This value is passed to conditions or actions as trigger variable 1 (*real number*).

[//]: # (#### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (#### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (#### Further Notes)
[//]: # (Possible location for further notes, may not be used)
