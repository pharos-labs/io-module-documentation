# Email Notification - Version 2.2.2

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Send notification emails using the Mailgun API.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Release Notes

#### Version 2.2.2
* &nbsp;Added error feedback to logs and Web UI.

#### Version 2.2

* &nbsp;Bug 8273 regular expression validation fix.
* &nbsp;Implemented fair usage policy limit.
* &nbsp;Updated status variables.
* &nbsp;Updated documentation.

#### Version 2.1

* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;Added default *Subject* and *Body* text.
* &nbsp;Added status variables.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

### Module Scope

**Note:** The modules uses an external service, the Mailgun API and there is therefore we operatre a fair usage policy with a maximum number of emails that can be sent per day, per Controller.

This is disaplyed in the log and in status variables. If you require sending more than the maximum in a day, please contact support.

## Operation

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Set *From* to the email address and/or name you wish to show as the sender of the email.

[//]: # (Describe relevant instance properties if there are any beyond the name)

[//]: # (### Triggers)
[//]: # (An event received by the controller that can be acted upon to create a reaction)

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Last Attempt&nbsp;&nbsp;&nbsp;</td>
        <td>The last date and time the *Send* Action was called.</td>
    </tr>
    <tr>
        <td>Status&nbsp;&nbsp;&nbsp;</td>
        <td>The result of the last *Send* Action or an alternative status message.</td>
    </tr>
    <tr>
        <td>Limit&nbsp;&nbsp;&nbsp;</td>
        <td>Information on the number of emails sent in a given day (based on the fair usage policy).</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Actions

#### Send

Sends an email to the *Destination Address* with the *Subject* title and *Body* of the message.

The *Destination Address* is required but if either the *Subject* or *Body* is left blank, then they will be filled with a default message.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
