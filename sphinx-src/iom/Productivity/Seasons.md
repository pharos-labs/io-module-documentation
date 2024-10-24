# Seasons - Version 2.1.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Use the yearly seasons as parameters to control and trigger events.

## Module Status

This IO Module is stable and has been tested internally.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1

* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;Updated module documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

The *Season Event* Trigger allows for events to be triggered when a seasonal change occurs at midnight.

The *Season* Condition enables a Tigger sequence to check whether any given season is/isn't currently occurring.

The Instance Properties allow the definition of the hemisphere and dates over which the seasonal changes happen.

### Instance Properties

From within the Instance Properties specify the *Hemisphere* according to which you wish this IO Module to operate.

Set the *Season Definition* to choose when the dates when season changes happen. The available options are:

* &nbsp;*Solstice/Equinox Start* - Seasons start according to the accurate astronomical Solstice and Equinoxe dates which vary slightly year to year. This means the season will change as soon as the day of the Solstice / Equinox begins.
* &nbsp;*Solstice/Equinox Month Start* - Seasons start according to the meteorological seasons that begin on the first day of the month during with the Solstices and Equinoxes occur:
  * &nbsp;1st March = start of Spring / Autumn.
  * &nbsp;1st June = start of Summer / Winter.
  * &nbsp;1st September = start of Autumn / Spring.
  * &nbsp;1st December = start of Winter / Summer.
* &nbsp;*Solstice/Equinox 21st Start* - Seasons start on the 21st of the month during which the Solstices and Equinoxes occur: March, June, September, and December.
* &nbsp;*Solstice/Equinox Midway* - This setting will treat the astronomical Solstice and Equinox dates as the mid-point of each season. This means the start day for each season happens midway between the astronomical Solstic and Equinox dates, and will vary slightly from year to year, for 2020:
  * &nbsp;4th February = start of Spring / Autumn.
  * &nbsp;5th May = start of Summer / Winter.
  * &nbsp;6th August = start of Autumn / Spring.
  * &nbsp;6th November = start of Winter / Summer.
* &nbsp;*Solstice/Equinox Midway Month* - This setting will also treat the astronomical Solstice and Equinox dates as the mid-point of each season. However, the season change will occur upon the first day of the month that occurs between each Solstice and Equinox:
  * &nbsp;1st February = start of Spring / Autumn.
  * &nbsp;1st May = start of Summer / Winter.
  * &nbsp;1st August = start of Autumn / Spring.
  * &nbsp;1st November = start of Winter / Summer.

Use the *IO module instance* to select the instance with the desired *Hemisphere* and *Season Definition*.

### Triggers

#### Season Event

This Trigger fires at midnight of the night across which the season changes according to the *Season Definition* set in the Instance Properties.

The *Event* Trigger option can be used to specify whether the Trigger should only fire for the start of a specific season.

Use the *IO module instance* to select the instance with the desired *Hemisphere* and *Season Definition*.

### Conditions

#### Season

Set the *Season* for which you wish the Condition to pass; by setting *Season* to Spring the Trigger-Action sequence will proceed only if it is currently the Spring season. By checking the *Negate* checkbox the Condition is reversed, allowing it to pass for all seasons that are not the one defined within the *Season* setting.

Use the *IO module instance* to select the instance with the desired *Hemisphere* and *Season Definition*.

[//]: # (### Actions)
[//]: # (This is the end result started by a trigger)

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
