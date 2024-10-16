# Australian Reefs - Version 2.1.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)
## Module Summary

Requests water parameters for Australian reefs, using the API at: [https://api.aims.gov.au/moua/climate](https://api.aims.gov.au/moua/climate).

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1

* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

## Configuration

To the able to request and receive data via the API, the Controller requires an Internet connection and its default gateway IP address set accordingly.

## Operation

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Select one of the pre-defined *Reef*s, supported within the API. This is the *Reef* used by the *Request Water Temperature* action, to make the request to [https://api.aims.gov.au/moua/climate](https://api.aims.gov.au/moua/climate).
### Triggers

#### Water Temperature Received

Fires when a response has been received from the remote API, having called a *Request Water Temperature Action* for the *Reef* specified in the instance properties. If the received temperature is greater than or equal to *Temperature Min* and less than or equal to *Temperature Max*, the trigger will return true and continue on to the conditions and actions, passing the temperature in degrees Celsius as trigger variable 1.

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)
### Actions

#### Request Water Temperature

Sends a request to the API to get the water temperature for the *Reef* specified in the instance properties. When a reply is received, the *Water Temperature Received* trigger is fired.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
