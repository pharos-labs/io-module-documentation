# Kumux - Version 2.1.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Interacts with [KUMUX](https://kumux.io/), getting the value of the Correlated Colour Temperature (CCT) for a given date, time, location and application.

[//]: # (Brief description of the module; usually the same as the description in the package)

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)
This IO Module is stable and has been tested internally.

[//]: # (Always required)
If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1

* Add condition: *Latest Smart Lighting Target*
* Remove scaling properties

#### Version 2.0

* Initial release.

[//]: # (Always required)
*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

## Requirements
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

The module requires an active Kumux subscription and API key.
Please contact [projects@kumux.io](mailto://projects@kumux.io) for more details.

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

For correct operation the Designer project should have accurate Latitude and Longitude set in the Project Properties.

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Module Properties

Set the *API Key* and *API Secret* as obtained from the Kumux API Developer Portal.

### Instance Properties

[//]: # (### List instance properties and their function)

Set the *Space* as appropriate for the target environment.

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

### Triggers
[//]: # (Start with a verb such as "Fires when..." or "Receives...")

#### Smart Lighting Target

Fires when the Controller should react to KUMUX Dynamic Scenes.

Trigger variables:

1. Target Brightness (Percent) (*integer*).
1. Target CCT (kelvin) (*integer*).
1. Fade time (seconds) (*integer*).

### Conditions
[//]: # (Start with a verb such as "Matches if...")

#### Latest Smart Lighting Target

Returns, as variables, the latest Smart Lighting Target.\
The properties, and returned variables, mirror Trigger <code>Smart Lighting Target</code>

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
