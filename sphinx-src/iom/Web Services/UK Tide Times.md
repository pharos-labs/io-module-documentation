# UK Tide Times - Version 2.0.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

[//]: # (Brief description of the module; usually the same as the description in the package)

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Updated documentation.
* &nbsp;Added status variables.
* &nbsp;Added *Tide Status* Condition.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

## Requirements

Requires valid UK Tidal API *Subscription Key*, available from [Admiralty](https://www.admiralty.co.uk/)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Enter you either your Primary or Secondary API Key in *Subscription Key* and select the required UK *Station* from the drop-down list.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Station Name</td>
        <td>Taken from the Instance properties.</td>
    </tr>
    <tr>
        <td>Station ID</td>
        <td>The station ID associated with the station name.</td>
    </tr>
    <tr>
        <td>Current Tide</td>
        <td>The current tide status: <code>High</code> or <code>Low</code>.</td>
    </tr>
    <tr>
        <td>Current Height</td>
        <td>The current flow type: <code>Ebbing</code> or <code>Flowing</code>.</td>
    </tr>
    <tr>
        <td>Last Tide Change&nbsp;&nbsp;&nbsp;</td>
        <td>The last time the tide went from <code>High</code> to <code>Low</code> or <code>Low</code> or <code>High</code>.</td>
    </tr>
    <tr>
        <td>Last Updated</td>
        <td>The last time tide data was requested (may not have fired a Trigger).</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Tide Event

Fires when a tide change happens as per the data retrieved from Admiralty.

If the *Event* is set to <code>Any</code> then the Trigger will match is the tide is <code>High</code> or <code>Low</code>,
otherwise the current event type must match the *Event* property.

### Conditions

#### Tide Event

Condition is met if the last tide event matches the *Event* property; <code>High</code> or <code>Low</code>.

#### Tide Direction

Condition is met if the last tide direction matches the *Direction* property; <code>Ebbing</code> or <code>Flowing</code>.

[//]: # (### Actions)

[//]: # (#### Action Name)
[//]: # (#### Start with a verb such as "Sends..." or "Sets...")

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
