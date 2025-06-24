# Zencontrol TPI - Version 2.0.0.BETA1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

[//]: # (Brief description of the module; usually the same as the description in the package)

Interact with Zencontrol DALI Application controller using Zencontrol Third Party Interface (TPI).

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

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

**Note:** Zencontrol Third Party Interface (TPI) uses multicast for event messages.\
The project controller needs to have a default gateway specified in the Network properties.

### Module Properties

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

### Instance Properties

[//]: # (### List instance properties and their function)

Set the *IP Address* to that configured on the device.

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

Checking the *Log Comms* checkbox will provide detailed protocol communication log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

### Triggers

[//]: # (Start with a verb such as "Fires when..." or "Receives...")

#### Button Press

Fires when the device reports a matching button press.

Trigger variables:

* *Variable 1*: DALI control device address /63 (*integer*).
* *Variable 2*: DALI control device instance number /31 (*integer*).

#### Button Hold

Fires when the device reports a matching button hold.

Trigger variables:

* *Variable 1*: DALI control device address /63 (*integer*).
* *Variable 2*: DALI control device instance number /31 (*integer*).

#### Absolute Input

Fires when the device reports a matching absolute input change.

Trigger variables:

* *Variable 1*: DALI control device address /63 (*integer*).
* *Variable 2*: DALI control device instance number /31 (*integer*).
* *Variable 3*: Absolute input value (*integer*).

#### Level Change

Fires when the device reports a matching device level change.

Trigger variables:

* *Variable 1*: DALI control gear address /63 (*integer*).
* *Variable 2*: Level value /254 (*integer*).

#### Group Level Change

Fires when the device reports a matching group level change.

Trigger variables:

* *Variable 1*: DALI control gear address /63 (*integer*).
* *Variable 2*: Level value /254 (*integer*).

#### Scene Change

Fires when the device reports a matching scene change.

Trigger variables:

* *Variable 1*: Control gear address type (*"GEAR" or "GROUP"*).
* *Variable 2*: DALI control gear address /63 (*integer*).
* *Variable 3*: Scene number /15 (*integer*).

#### Occupancy Detected

Fires when the device reports a matching occupancy detection.

Trigger variables:

* *Variable 1*: DALI control device address /63 (*integer*).
* *Variable 2*: DALI control device instance number /31 (*integer*).

#### RGBWAF Colour Change

Fires when the device reports a matching colour change.

Trigger variables:

* *Variable 1*: DALI control gear address type (*"GEAR" or "GROUP"*).
* *Variable 2*: DALI control gear address /63 (*integer*).
* *Variable 3*: Red value /255 (*integer*)
* *Variable 4*: Green value /255 (*integer*)
* *Variable 5*: Blue value /255 (*integer*)
*The following are optional depending on fixture type*
* *Variable 6*: White value /255 (*integer*)
* *Variable 7*: Amber value /255 (*integer*)
* *Variable 8*: Freecolour value /255 (*integer*)

#### CT Colour Change

Fires when the device reports a matching colour change.

Trigger variables:

* *Variable 1*: DALI control gear address type (*"GEAR" or "GROUP"*).
* *Variable 2*: DALI control gear address /63 (*integer*).
* *Variable 3*: Colour temperature (kelvin) (*integer*)

#### System Variable Change

Fires when the device reports a matching system variable change.

Trigger variables:

* *Variable 1*: Variable number (*integer*).
* *Variable 2*: Variable value (*integer*).

#### Profile Change

Fires when the device reports a matching profile change.

Trigger variables:

* *Variable 1*: Profile number (*integer*).

### Actions

[//]: # (Start with a verb such as "Requests..." or "Starts...")

#### Enable Events

Sends a request to the device to enable event reports.

#### Set Off

Sends a request to the device to set the matching DALI control gear to `off`.

#### Set Level

Sends a request to the device to set the matching DALI control gear to a level.

#### Set Scene

Sends a request to the device to set the matching DALI control gear to a scene.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
