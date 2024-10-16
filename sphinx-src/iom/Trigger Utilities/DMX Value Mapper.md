# DMX Value Mapper - Version 2.0.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Maps DMX channel values to trigger variables, when a change in a fixture is detected.

## Module Status

Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use and we can not take responsibility for issues experienced should this be used on a live project.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Initial release.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

The fixture and universe parameters are defined in the instance properties. When a change in fixture parameters is detected, a trigger will fire with the channel number and parameters values.

### Instance Properties

[//]: # (Describe relevant instance properties if there are any beyond the name)

Select a DMX *Protocol* and *Universe* number for a DMX universe **of the network primary** controller (the controller the IO module is running on). If the *Protocol* and *Universe* combination not for the controller, an error will be logged at startup and at regular intervals.

Set the *Start Address* to the address of the **first fixture's address**; the lowest fixture number in the range. If the *Fixture Numbers* are not in numerical order (which is perfectly valid), the first fixture will be dtermined by the module.

*Fixture Type* defines the parameters of each fixture in string format, eg. *IRGBW* or *CwMwWw*. The supported parameters are *I R G B A W Ww Cw Mw Nw H S Ct M Uv*. The order and parameter count are calculated from this string and should match how the fixtures are patched to the physical universe.

Enter the *Fixture Numbers* in numeric, comma and dash separated format eg. *1-5*, *1, 3, 5* or *1-5, 7, 9,*. The DMX start addresses of each fixture is determined by the parameter count (in *Fixture Type*), the universe DMX *Start Address* and the number of *Bits*. If fixture numbers are not sequential (*1, 3, 5* as opposed to *1-5*) then the non-specified numbers will be skipped in the DMX address space ie. in the example *1, 3*, the parameters of *1* are checked for a change, *2* is ignored and *3* is checked. For optimum performance, to is recommended that only the fixtures required are entered here.

**Note:** A 16 bit parameter value will be passed to the trigger as a single value, not as individaul byte values.

The order defined in *Fixture Numbers* will be the order the triggers are fired.

The *Conversation Range Max* is used to calculate the trigger variable values. Examples: A *Conversion Range Max* of 255 will convert a value (whether *8 Bit* or *16 Bit*) in the range of 0 - 255, 1 in the range of 0 - 1, and 100 as a percentage of 0 - 100%. If checked, *Round Values* will round a calculated value to the nearest whole number, otherwise the value may be in decimal format. If the value is a whole number, the *Conversion Range Max* value will also be used as the variable range format.

*Trigger Refresh* determines how often triggers should fire (one trigger for each channel). The lower the number, the more often triggers will be fired when a change in values is detected. For optimum performance, it is recommended to have as high number as possible, whilst maintaining usability.

**Note:** There will only ever be one trigger per channel change in the given *Trigger Refresh* cycles. This mean that if a channel changes values multiple times in a refresh cycle, only the latest changed values will be passed to the trigger. Triggers will only be fired if a change in values is detected ie. if a fixture is set to a static colour, a trigger will be fired during the transition but not once settled. If, within a refresh cycle, a fixtures starts in one colour, transitions to another colour and then back to the first colour, this is counted as a change and will fire a trigger at the end of the cycle.

If there are a large number of channels, you may wish to limit the number of triggers using *Max Triggers per Refresh*. This may mean that some changes could be missed in a given cycle, if the number of changed fixtures exceeds the *Max Triggers per Refresh*. Only fixtures with changed values contribute to the triggers per refresh. If *Drop Excess Triggers* is checked, at the end of the refresh cycle, if the number of changes exceeds the *Max Triggers per Refresh*, the changes up to *Max Triggers per Refresh* will fire triggers and the rest will be dropped. Triggers will fire in order defined in *Fixture Numbers*. If *Drop Excess Triggers* is not checked, at the end of the refresh cycle, if the number of changes exceeds *Max Triggers per Refresh*, the remaining changes will be queued for the next refresh cycle. If the values change within this time, the new values will be the ones passed to the trigger.

Checking the *Extended Logging* checkbox will provide more detailed log messages for diagnostic purposes. It is highly recommended that this is disabled during normal operation to maintain controller performance.

### Triggers

#### DMX Value Changed

Fires when parameters of a fixture specified in *Fixture Numbers* of the instance properties change. *Fixture Numbers* of the trigger specified are specified in numeric, comma and dash separated format eg. *1-5*, *1, 3, 5* or *1-5, 7, 9,*. If any of the numbers specified match a fixture with changed values, the trigger will match and execute the action. If the *Fixture Numbers* string is left blank, any fixtures with changed values will fire.

**Note:** The trigger will fire only if there are changes, not just on every refresh cycle.

A trigger variable will be passed for each parameter specified in instance *Fixture Type*. If *Extended Logging* is checked, a detailed message will show in the log with parameter labels and values to determine which trigger variable relates to which parameter:

* &nbsp;*Variable 1*: *Always* Fixture Number (*integer*).
* &nbsp;*Variable 2...n*: Parameter values (*integer*).

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

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
