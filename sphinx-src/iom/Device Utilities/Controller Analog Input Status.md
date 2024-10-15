# Controller Analog Input Status - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Label*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Displays the status of each of a Network Primary's analog inputs in the IO modules tab of the web interface.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope

The analog inputs can only be those physically on the Network Primary or any RIOs associated with the Network Primary.

### Release Notes

#### Version 2.0

* &nbsp;Initial release.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

There are no Triggers, Conditions or Actions associated with this module. The status of analog input can be viewed in the IO module tab of the web interface.

### Instance Properties

The *Suffix* is a string that will appended to the value in the status variable.

*Display Conversion Range From* and *Display Conversion Range To* define how the value is displayed in the status variables. The incoming input value is by default in the range 0-255, so if, for example,
the value is to be displayed as a percentage, *Display Conversion Range From* would be set to <code>0</code>, *Display Conversion Range To* to <code>100</code> and *Suffix* to <code>%</code>.

**Note: The above properties and for display purposes and does not affect the incoming value.**

Set the *Input \[number\]* to the physical analog input, as configured in the Network tab. Optionally, a descriptive *Input \[number\] Label* can be specified that will be displayed
on the IO module table of the web interface along with the input's current value (or an error message if applicable).

The inputs would commonly be inputs 1-8 of an LPC but can in fact be any combination of inputs on the Network Primary Controller or any RIO devices associated with thew Network Primary.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows the state of each input.

[//]: # (### Triggers)

[//]: # (#### Trigger Label)
[//]: # (#### Start with a verb such as "Fires when..." or "Receives...")

[//]: # (### Conditions)

[//]: # (#### Conditions Label)
[//]: # (#### Start with a verb such as "Is met when..." or "Returns true if...")

[//]: # (### Actions)

[//]: # (#### Action Label)
[//]: # (#### Start with a verb such as "Sends..." or "Sets...")

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
