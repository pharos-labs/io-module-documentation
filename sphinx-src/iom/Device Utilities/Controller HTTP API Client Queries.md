# Controller HTTP API Client Queries - Version 2.1.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Queries a Project from another Project using the Controller HTTP API.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1

* Support for Controllers with security enabled.

#### Version 2.0

* Updated documentation.
* General updates and improvements.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Set the *Destination Controller IP Address* and *Destination Port* to the Controller with the Project to query.

If the destination Controller has security enabled, then the *Username* and *Password* should be set, if the *Username* is omitted then the *Password* is ignored.

Ticking *Use SSL* will attempt to use encrypted HTTPS with the Controller. n.b. You may need to set the matching *Destination Port*, normally <code>443</code>.

### Triggers

#### Response

Fires when a response to a query made from an Action is received.

If *Query Type* is set to <code>Any</code>, the Trigger will be matched for any response,
otherwise the *Query Type* must match the response type for the Trigger to match.

Response data will be passed as Trigger variables, one for each value.

[//]: # (### Conditions)

[//]: # (#### Conditions Name)
[//]: # (#### Start with a verb such as "Is met when..." or "Returns true if...")

### Actions

#### System Info

Sends a request to the remote Controller to return system information data.

The response will fire a *Response* Trigger, passing the returned values as Trigger variables.

#### Project

Sends a request to the remote Controller to return data on the Project.

The response will fire a *Response* Trigger, passing the returned values as Trigger variables.

#### Time

Sends a request to the remote Controller to return data on the Controller's time.

The response will fire a *Response* Trigger, passing the returned values as Trigger variables.

#### Timeline

Sends a request to the remote Controller to return data on the Project's Timelines.

Timelines can be specified in the *Timelines (Optional)* property in comma-dash format, otherwise data on all Timelines will be returned.

The response will fire a *Response* Trigger, passing the returned values as Trigger variables.

#### Timeline

Sends a request to the remote Controller to return data on the Project's Scenes.

Scenes can be specified in the *Scenes (Optional)* property in comma-dash format, otherwise data on all Scenes will be returned.

The response will fire a *Response* Trigger, passing the returned values as Trigger variables.

#### Group

Sends a request to the remote Controller to return data on the Project's Groups.

Groups can be specified in the *Groups (Optional)* property in comma-dash format, otherwise data on all Groups will be returned.

The response will fire a *Response* Trigger, passing the returned values as Trigger variables.

#### Controller

Sends a request to the remote Controller to return data on the Controller.

The response will fire a *Response* Trigger, passing the returned values as Trigger variables.

#### Temperature

Sends a request to the remote Controller to return data on the Controller's temperature.

The response will fire a *Response* Trigger, passing the returned values as Trigger variables.

#### Remote Device

Sends a request to the remote Controller to return data on the Project's remote devices.

The response will fire a *Response* Trigger, passing the returned values as Trigger variables.

#### Text Slots

Sends a request to the remote Controller to return data on the Project's text slots.

A text slot can be specified in the *Text Slots (Optional)* property in comma-dash format, otherwise data on all text slots will be returned.

The response will fire a *Response* Trigger, passing the returned values as Trigger variables.

#### Log

Sends a request to the remote Controller to return all log data.

The response will fire a *Response* Trigger, passing each line of the log as Trigger variables.

#### Protocol

Sends a request to the remote Controller to return data on the Controller's protocols.

The response will fire a *Response* Trigger, passing each line of the log as Trigger variables.

#### Output

Sends a request to the remote Controller to return data on the Controller's DMX output.

The response will fire a *Response* Trigger, passing each line of the log as Trigger variables.

#### Inputs

Sends a request to the remote Controller to return data on the Controller's inputs.

The response will fire a *Response* Trigger, passing the returned values as Trigger variables.

#### Remote Device

Sends a request to the remote Controller to return data on the Project's Triggers.

The response will fire a *Response* Trigger, passing the returned values as Trigger variables.

#### Lua Variables

Sends a request to the remote Controller to return data on the Controller's lua variables.

Lua variables can be specified in the *Variable Names* property in a comma-separated list.

The response will fire a *Response* Trigger, passing the returned values as Trigger variables.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
