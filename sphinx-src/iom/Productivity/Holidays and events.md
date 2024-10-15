# Holidays and events - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

National Holidays and events triggering.

[//]: # (Brief description of the module; usually the same as the description in the package)

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)
This IO Module is stable and has been tested internally.

[//]: # (Always required)
If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope
[//]: # (If important to mention explain the limitations and things this module cannot perform)

The module is limited to the following catagories:
* Public and/or Bank Holidays for:

    - England and Wales<sup>1</sup>
    - Northern Ireland<sup>1</sup>
    - Scotland<sup>1</sup>
    - Netherlands

* Federal Holidays for:

    - United States of America

<sup>1</sup> Holiday events may occur on "substitute days".\
i.e. December 25th 2022 was a Sunday, so the Bank holiday occurred on Monday December 26th

Details of the event days for the current year will be posted to the logs if *Extended Logging* is enabled.

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

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

### Triggers

#### Trigger <i>"category"</i>

[//]: # (Start with a verb such as "Fires when..." or "Receives...")
Fires when the Controller date and time matches *Event* and *Time*.

Trigger variables:

* &nbsp;*Variable 1*: Event name (*string*).

### Conditions

#### Condition <i>"category"</i>

[//]: # (Start with a verb such as "Matches if...")
Matches if *Event* is today.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
