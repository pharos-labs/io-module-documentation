# Madrix Aura - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Remote control of a Madrix Aura using HTTP.

[//]: # (Brief description of the module; usually the same as the description in the package)

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
This IO Module is stable and has been tested internally.

[//]: # (**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)

[//]: # (Always required)
If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Initial release.

[//]: # (Always required)
*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

## Configuration

The HTTP Remove Event configuration of the Madrix Aura must match that of the Instance Properties.\
Configuration of the Madrix Aura is performed using the Madrix Aura's built in web interface, initial setup is performed using Madrix Hardware Manager.

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

[//]: # (### List instance properties and their function)

Set the *IP Address* to that configured on the device.

Each *Command x* property value should be made to correspond with the matching Madrix Aura HTTP Remove Event Command.\
The default value expressed in the module, match the default values obtained by clicking "D" button in the "Remote Event List" on the Madrix Aura builtin configurer.\
<I>*Please note:* The defaults created by the "D" button may include undesired remote control via eDMX. Ensure that the settings are suitable for your system after setting these defaults.</I>\
Further details on how to set this on the Madrix Aura can be found at [Madrix Aura Support](https://help.madrix.com/aura/html/index.html?hidd_remote.html)

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

### Actions

#### Command Scene

Command the Madrix Aura to recall cue/scene *Value*.

#### Command Play

Command the Madrix Aura to start playback.

#### Command Pause

Command the Madrix Aura to pause playback.

#### Command Stop

Command the Madrix Aura to stop playback.

#### Command Record

Command the Madrix Aura to start recording.

#### Command Next

Command the Madrix Aura to skip to the next cue/scene.

#### Command Previous

Command the Madrix Aura to skip to the previous cue/scene.

#### Command Intensity

Command the Madrix Aura to sets the master brightness to *Value*.

#### Command Intensity (Increment)

Command the Madrix Aura to increase master brightness by *Value*.\
<i>n.b. The remote event action <code>Value Type</code> will need to be set to <code>Input Value</code></i>

#### Command Intensity (Decrement)

Command the Madrix Aura to decrease master brightness by *Value*.\
<i>n.b. The remote event action <code>Value Type</code> will need to be set to <code>Input Value</code></i>

#### Command Speed

Command the Madrix Aura to sets the speed to *Value*.

#### Command Intensity (Increment)

Command the Madrix Aura to increase speed by *Value*.\
<i>n.b. The remote event action <code>Value Type</code> will need to be set to <code>Input Value</code></i>

#### Command Intensity (Decrement)

Command the Madrix Aura to decrease speed by *Value*.\
<i>n.b. The remote event action <code>Value Type</code> will need to be set to <code>Input Value</code></i>

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
