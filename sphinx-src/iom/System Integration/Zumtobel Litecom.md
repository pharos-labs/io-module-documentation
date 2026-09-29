# Zumtobel Litecom - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

[//]: # (Brief description of the module; usually the same as the description in the package)

Interact with a Zumtobel Litecom system using REST API and MQTT.

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (This IO Module is stable and has been tested internally.)
[//]: # (**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)

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

### Instance Properties

[//]: # (### List instance properties and their function)

Set the *IP Address* to that configured on the device.

Set the *Customer Name* and *API Token* to the values of an "REST API & MQTT" API consumer created for the device.

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

### Triggers

[//]: # (Start with a verb such as "Fires when..." or "Receives...")

#### Connected

Fires when the Controller is connected to the device's MQTT broker service.

#### Disconnected

Fires when the Controller is disconnected from the device's MQTT broker service.

#### Scene Recalled

Fires when the device reports a zone matching *Zone ID* (or blank for any), and a scene matching *Scene Number* is recalled.

Trigger variables:

* &nbsp;*Variable 1*: Zone ID (*string*).
* &nbsp;*Variable 2*: Scene Number (*integer*).

#### Zone Level Changed

Fires when the device reports a zone matching *Zone ID* (or blank for any) and an intensity level matching *Level* has been set.

Trigger variables:

* &nbsp;*Variable 1*: Zone ID (*string*).
* &nbsp;*Variable 2*: Level /100 (*integer*).

#### Zone Colour Changed

Fires when the device reports a zone matching *Zone ID* (or blank for any) and an RGB colour matching *Red*, *Green*, *Blue*; has been set.

Trigger variables:

* &nbsp;*Variable 1*: Zone ID (*string*).
* &nbsp;*Variable 2*: Red /255 (*integer*).
* &nbsp;*Variable 3*: Green /255 (*integer*).
* &nbsp;*Variable 4*: Blue /255 (*integer*).

### Actions

[//]: # (Start with a verb such as "Requests..." or "Starts...")

#### Recall Scene

Sends a request to the device to recall *Scene Number* in *Zone ID*.

#### Set Zone Level

Sends a request to the device to set the intensity *Level* in *Zone ID*.

#### Set Zone Colour

Sends a request to the device to set the *Red*, *Green*, and *Blue*; colours in *Zone ID*.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
