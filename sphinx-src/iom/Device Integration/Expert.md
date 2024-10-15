# Expert - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Interacts with an Expert Controller using Pharos HTTP API.

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

Set the *IP Address* and *Port* to that configured for the HTTPS interface on the Expert Controller.\
The default *Port* is 443.

If the remote Controller has security enabled, then the *Username* and *Password* should be set. If security is disabled, leave these blank.

The local Controller will auto connect on startup if *Auto connect?* is enabled, and will automatically reconnect should an issue occur if *Auto reconnect?* is enabled.

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
        <td>Controller name</td>
        <td>Remote Controller's name, i.e. 'Controller 1'</td>
    </tr>
    <tr>
        <td>Controller type</td>
        <td>Remote Controller's type, i.e. 'Expert Control'</td>
    </tr>
    <tr>
        <td>Controller serial</td>
        <td>Remote Controller's serial number</td>
    </tr>
    <tr>
        <td>Controller firmware version</td>
        <td>Remote Controller's main firmware number</td>
    </tr>
    <tr>
        <td>Project name</td>
        <td>The name of the project currently loaded on the remote Controller</td>
    </tr>
    <tr>
        <td>Project author</td>
        <td>The author's name of the project currently loaded on the remote Controller</td>
    </tr>
    <tr>
        <td>Project filename</td>
        <td>The filename of the project currently loaded on the remote Controller</td>
    </tr>
    <tr>
        <td>Project UUID</td>
        <td>The unique ID of the project currently loaded on the remote Controller</td>
    </tr>
    <tr>
        <td>Project date</td>
        <td>The last save date of the project currently loaded on the remote Controller</td>
    </tr>
    <tr>
        <td>Cloud state</td>
        <td>Current cloud connectivity status of the remote Controller</td>
            <ul style="margin-top:0px;">
                <li><code>Unknown</code></li>
                <li><code>Not connected</code></li>
                <li><code>Connecting</code></li>
                <li><code>Connected</code></li>
            </ul>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

[//]: # (Start with a verb such as "Fires when..." or "Receives...")

#### Access denied

Fires if the *Username*/*Password* combination is invalid.

Trigger variables:

* &nbsp;*Variable 1*: Access denied reason message (*string*).

#### Connected

Fires when connection to the remote Controller is established.

#### Disconnected

Fires when connection to the remote Controller is lost.

#### Beacon status

Fires when beacon status of the remote Controller changes to match *Status*.

Trigger variables:

* &nbsp;*Variable 1*: Beacon on? (*boolean*).

#### Cloud status

Fires when cloud connectivity status of the remote Controller changes to match *Status*.

#### Scene recalled

Fires when a scene is recalled on the remote Controller that matches scene *Number*, and *Space* number.

Trigger variables:

* &nbsp;*Variable 1*: Scene number (*integer*).
* &nbsp;*Variable 2*: Scene name (*string*).
* &nbsp;*Variable 3*: Space number (*integer*).

#### Tag activated

Fires when a tag is activated on the remote Controller that matches tag set *Set*, and tag *Number*.

Trigger variables:

* &nbsp;*Variable 1*: Tag set number (*integer*).
* &nbsp;*Variable 2*: Tag set name (*string*).
* &nbsp;*Variable 3*: Tag number (*integer*).
* &nbsp;*Variable 4*: Tag name (*string*).

### Conditions

[//]: # (Start with a verb such as "Matches if...")

#### Is connected

Matches if currently connected to the remote Controller.

### Actions

[//]: # (Start with a verb such as "Requests..." or "Starts...")

#### Connect

Starts a connection to the remote Controller.

#### Disconnect

Initiate a disconnect from the remote Controller.

#### Toggle beacon

Requests the remote controller to toggle beacon status.

#### Channel park

Requests the remote controller to park an output *Channel* number on port *Universe index* of protocol *Universe protocol* at a *Level*.

#### Channel unpark

Requests the remote controller to unpark an output *Channel* number on port *Universe index* of protocol *Universe protocol*, previously parked.

#### Scene recall

Requests the remote controller to recall scene *Number*.

#### Space off

Requests the remote controller to set space *Number* to off.

#### Space master intensity

Requests the remote controller to set space *Number* to master intensity to *Intensity* percent.

#### Tag activate

Requests the remote controller to activate tag *Number* in tag set *Set*.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
