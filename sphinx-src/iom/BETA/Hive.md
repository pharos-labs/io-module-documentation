# Hive - Version 2.0.0.BETA1

## Module Summary

Integrate with Hive Media Control

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (This IO Module is stable and has been tested internally.)
**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.

[//]: # (Always required)
If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope
[//]: # (If important to mention explain the limitations and things this module cannot perform)

This module does not support authentication, this must be disabled on the Hive Media Controller

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

Set the *IP address* to that configured on the device.

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

### Actions

#### Select Media File

Sends a request to the device to select media *File* number for *Layer*.

#### Select Media Folder

Sends a request to the device to select media *Folder* number for *Layer*.

#### Select In Frame

Sends a request to the device to select the *Frame* number from which media playback should start for *Layer*.

#### Select Out Frame

Sends a request to the device to select the *Frame* number from which media playback should should end or loop for *Layer*.

#### Select Play Mode

Sends a request to the device to select the *Mode* which should be applied to how the media plays for *Layer*.

#### Select Play Speed

Sends a request to the device to select the play *Speed* of the media for *Layer*.

<table>
    <thead>
        <tr>
            <th>Value</th>
            <th>Description</th>
        </tr>
    </thead>
    <tr>
        <td>0.0</td>
        <td>Stop</td>
    </tr>
    <tr>
        <td>0.001 to 0.499</td>
        <td>Slower</td>
    </tr>
    <tr>
        <td>0.5</td>
        <td>Normal speed</td>
    </tr>
    <tr>
        <td>0.501 to 1.0</td>
        <td>Faster</td>
    </tr>
</table>

#### Select Scale

Sends a request to the device to select the *Scale* of the media for *Layer*.

<table>
    <thead>
        <tr>
            <th>Value</th>
            <th>Description</th>
        </tr>
    </thead>
    <tr>
        <td>0.0 to 4999</td>
        <td>Zoom out</td>
    </tr>
    <tr>
        <td>0.5</td>
        <td>100%</td>
    </tr>
    <tr>
        <td>0.5001..1.0</td>
        <td>Zoom in</td>
    </tr>
</table>

#### Select Blend Mode

Sends a request to the device to select the *Mode* which should be applied to blending with any layers appearing below *Layer*.

#### Set Intensity

Sends a request to the device to select media *Intensity* for *Layer*.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
