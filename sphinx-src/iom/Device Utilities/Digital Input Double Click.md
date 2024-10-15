# Digital Input Double Click - Version 2.1.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

[//]: # (Describe as briefly and clearly the role of the module)

This module will fire a trigger when a double click on a specified Digital Input / Contact Closure is detected.

## Module Status

[//]: # (If still desired provide a status of the module)

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Release Notes

#### Version 2.1

* &nbsp;Updated documentation.
#### Version 2.0

* &nbsp;General module updates and improvements.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

## Operation

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

[//]: # (Describe relevant instance properties if there are any beyond the name)

*Input* - Select the Device and Input that should be monitored. Each Instance monitors a single input to detect a double click event

*Mode* - Select whether the input is Normally Open (Low) or Normally Closed (High).

*Timeout* - Determines the maximum duration of a double click event that will be detected.

### Triggers

Add the *Digital Input Double Click* trigger to the project and select the instance that relates to the input that should be used for the trigger.

*Note: This module will not override the normal Digital Inut triggers, if you have Digital Input Low triggers, these will also be fired (twice)*

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
