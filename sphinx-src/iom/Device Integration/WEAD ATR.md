# WEAD ATR - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

[//]: # (Brief description of the module; usually the same as the description in the package)

Poll WEAD ATR Sensors for touch events

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)
This IO Module is stable and has been tested internally.

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
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)
The WEAD sensors must be appropriately patched in Designer, for this module to match the fixture numbers.

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Module Properties

*Polling Rate* sets the desired interval between polling all the fixture instances. This number can affect controller performance.

### Instance Properties

[//]: # (### List instance properties and their function)

Set *Fixture* to the matching Fixture number to be polled by that instance.\
**Note:**Each instance *MUST* have a unique fixture number.

*Interface* should be set to the matching DMX interface for the *Fixture*, based on this selection other interface related properties will be available.\
These should be set to select the desired matching *Interface* number/universe for the *Fixture*.

### Triggers

[//]: # (Start with a verb such as "Fires when..." or "Receives...")

#### Touch Detected

Fires when the fixture reports, via polling, a touch has been detected.

Trigger variables:

* &nbsp;*Variable 1*: Fixture number (*integer*).

### Actions

[//]: # (Start with a verb such as "Requests..." or "Starts...")

#### Pause Polling

Pauses RDM polling for this instance.

#### Resume Polling

Resumes RDM polling for this instance.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
