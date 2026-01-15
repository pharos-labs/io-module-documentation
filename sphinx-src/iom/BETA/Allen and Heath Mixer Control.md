# Allen and Heath Mixer Control - Version 2.0.0.BETA1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

[//]: # (Brief description of the module; usually the same as the description in the package)

Interact with an Allen and Heath Mixer using AHM TCP/IP Protocol

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (This IO Module is stable and has been tested internally.)
**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.

[//]: # (Always required)
If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* Initial release.

[//]: # (Always required)
*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)
The mixer should be configured with *Security Level* "No Security"

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

[//]: # (### List instance properties and their function)

Set the *Mixer IP Address* to that configured on the device.

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

### Triggers

[//]: # (Start with a verb such as "Fires when..." or "Receives...")

The integer trigger variable Channel type has the following special meaning:
* 0 = Input
* 1 = Zone
* 2 = Control Group
* 3 = Room

#### Connected

Fires when the Controller connects to the device.

#### Disconnected

Fires when the Controller disconnects from the device.

#### Channel Level Change

Fires when a channel level changes.

Trigger variables:

* *Variable 1*: Channel type (*integer*).
* *Variable 2*: Channel number (*integer*).
* *Variable 3*: dBu level (*number*).

#### Mute Change

Fires when a channel mute changes.

Trigger variables:

* *Variable 1*: Channel type (*integer*).
* *Variable 2*: Channel number (*integer*).
* *Variable 3*: Enabled (*boolean*).

#### Preset Change

Fires when a preset is recalled on the device.

Trigger variables:

* *Variable 1*: Preset number (*integer*).

### Actions

[//]: # (Start with a verb such as "Requests..." or "Starts...")

#### Mute Channel

Sends a request to the device to mute a channel.

#### Unmute Channel

Sends a request to the device to unmute a channel.

#### Set Channel Level

Sends a request to the device to set the level of a channel.

#### Set Pad

Sends a request to the device to enable/disable the preamp pad of a channel.

#### Set Phantom Power

Sends a request to the device to enable/disable the preamp phantom power of a channel.

#### Recall Preset

Sends a request to the device to recall a preset.

#### Audio Playback

Sends a request to the device to playback an audio track.

#### Set Room Combine

Sends a request to the device to combine/un-combine two rooms.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
