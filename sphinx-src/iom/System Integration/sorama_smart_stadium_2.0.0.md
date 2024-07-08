# Sorama Smart Stadium - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary
[//]: # (Brief description of the module; usually the same as the description in the package)

Connects to a Sorama smart stadium server, and returns area 'intensity' values.
'Intensity' is calculated as mean of the current areas low and high decimal, scaled and normalised to a either a _float_, _percentage_, or _byte_.

**Note:** The operating Controller should be spec'd with the number of reporting areas in mind.\
The basic din-rail Controller may not be suitable for your requirements. Please consult with our support team for further hardware advice.

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (This IO Module is stable and has been tested internally.)
**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.

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

Set the *Host address* and *Host address* to that of the Sorama smart stadium server.
*Host address* can be either a hostname or IP address.
Access credentials should be entered into *Username* and *Password*.

The *Websocket endpoint* if left empty will use the default, otherwise a new endpoint can be specified.

Ticking *Auto connect on startup* will automatically connect ot the server on startup.
*Auto reconnect* will reconnect, after a 'cooling off' delay, to the server on error.

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

*Default scale minimum* and *Default scale maximum* set the default decibel scaling values to be used during normalisation. This can be changed during run-time using the action *Set scale*.

*Default scale mixer*, expressed as a _byte_ (0-255), is the liner ratio between user supplied scale minimum/maximum and the Sorama supplied frame minimum/maximum.
This can be changed during run-time using the action *Set mixer*.

*Value range* determinates if the returned value is a _float_ (0-1), _percentage_ (0-100%), -or _byte_ (0-255).

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
        <td>Host address</td>
        <td>Host name or IP address of the currently connected server</td>
    </tr>
    <tr>
        <td>Connection status</td>
        <td>Current bridge connection status.
            <ul style="margin-top:0px;">
                <li><i>'Access Denied'</i></li>
                <li><i>'Connected'</i></li>
                <li><i>'Connecting'</i></li>
                <li><i>'Reconnecting'</i></li>
                <li><i>'Disconnected'</i></li>
                <li><i>'Unknown'</i></li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>Last error</td>
        <td>Last connection error, if any, prepended with the date/time of the error</td>
    </tr>
    <tr>
        <td>Number of areas</td>
        <td>Number of areas last reported on by the server</td>
    </tr>
    <tr>
        <td>Scaling range</td>
        <td>Currently applied value scaling range</td>
    </tr>
    <tr>
        <td>Scaling mixer</td>
        <td>Currently applied scale mixer</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers
[//]: # (Start with a verb such as "Fires when..." or "Receives...")

#### Area value

Fires when the Controller receives an area value update from the server.

Matching properties:

* &nbsp;*Area*: Matching area number, or 'any'.

Trigger variables ('Any' Area):

* &nbsp;*Variable 1*: Area count (*variant*).
* &nbsp;*Variable 2*: Area value 1 (*variant*).
* &nbsp;*Variable n*: Area value n (*variant*).

Trigger variables (Single Area):

* &nbsp;*Variable 1*: Area number (*variant*).
* &nbsp;*Variable 2*: Area value (*variant*).

### Conditions
[//]: # (Start with a verb such as "Matches if...")

#### Connected

Matches if the Controller is currently connected to the server.

### Actions
[//]: # (Start with a verb such as "Requests..." or "Starts...")

#### Connect

Starts a connection to the Sorama server

#### Disconnect

Ends an existing connection with the Sorama server

#### Set scale

Update the scaling range used for normalisation.

Properties:

* &nbsp;*Minimum*: Minimum scale.
* &nbsp;*Maximum*: Maximum scale.

#### Set mixer

Update the scaling mixer used for normalisation.

Properties:

* &nbsp;*Value*: Mixer value.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
