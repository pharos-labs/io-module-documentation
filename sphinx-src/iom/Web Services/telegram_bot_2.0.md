# Telegram Bot - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Interact with Telegram messaging as a bot

[//]: # (Brief description of the module; usually the same as the description in the package)

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (**Note:** Please be aware that this is an beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)
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

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

[//]: # (### List instance properties and their function)

Set the *Token* to the unique authentication token obtained from Telegram's @BotFather.
Details on how to obtain this token can be found here: [https://core.telegram.org/bots/features#botfather](https://core.telegram.org/bots/features#botfather)

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.


#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <style type="text/css">
    td {
        padding: 3 10px;
    }
    </style>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>ID</td>
        <td>User ID of the bot</td>
    </tr>
    <tr>
        <td>Name</td>
        <td>Public name of the bot</td>
    </tr>
    <tr>
        <td>Username</td>
        <td>Public username of the bot</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Received Message

[//]: # (Start with a verb such as "Fires when..." or "Receives...")
Fires when the Controller receives a text message which has been sent to the bot, either directly, or via a group or channel the bot has been added to.

The *message* matching property can include variable captures, e.g. `Test<d><d>` would match with `Test12` and return the captured Variables `1` and `2`.
For full details of the available capture patterns, please refer to the Designer manual section [Variables](https://dl.pharoscontrols.com/software_help/designer2/Default.htm#help/reference/trigger/variables.htm).

Matching properties:

* &nbsp;*Chat Type*: Matching Chat Type, or Any.
* &nbsp;*Chat Name*: Matching Chat Name, or any if empty.
* &nbsp;*Chat ID*: Matching Chat ID, or any if empty.
* &nbsp;*Message*: Matching Text message, or any if empty.

Trigger variables:

* &nbsp;*Variable 1*: Chat ID (*string*).
* &nbsp;*Variable 2*: Chat Type: "private", "group", "supergroup", "channel" (*string*).
* &nbsp;*Variable 3*: Chat Name (*string*).
* &nbsp;*Variable 4*: Message (*string*).
* &nbsp;*Variable 5...n*: Optional captured variables (*Variant*).

### Actions

#### Send Message

[//]: # (Start with a verb such as "Requests..." or "Starts...")

Sends a text *Message* to the *Chat ID*.

(**Note:** A bot can only send a *Message* to a *Chat ID* that it has been added to. Unsolicited messages can not be sent to individual users.)

The *Chat ID* is the ID of a Telegram Group or Channel. In the case of a public group or channel that is the name of the channel in the form *@channelName*.

In the case of a private group or channel, it is a number which represents the private group or channel. Consult additional documentation for information on how to get this ID number.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
