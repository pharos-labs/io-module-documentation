# Color Kinetics Luminous Textile - Version 2.0.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Control a Color Kinetics Luminous Textile installation.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Set the *IP Address* and *UDP Port* to that of the Luminous Textile device.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

### Actions

#### Control

Sends a command *Action* to the Luminous Textile device to <code>Play</code>,
<code>Stop</code> playing,
<code>Toggle</code> play,
<code>Pause</code>,
go to <code>Next</code> preset,
go to <code>Previous</code> preset or
<code>Identify</code> the device.

#### Recall Preset

Sends a command to the Luminous Textile device to play a given *Preset*.

#### Set Brightness

Sends a command to set the Luminous Textile device to an *Intensity* between <code>0</code> and <code>255</code>.

#### Adjust Brightness

Sends a command to the Luminous Textile device to make an *Adjustment* to the brightness, either <code>Up 10%</code> or <code>Down 10%</code>.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
