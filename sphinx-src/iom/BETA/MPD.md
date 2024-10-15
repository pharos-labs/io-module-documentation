# MPD - Version 2.0.0.BETA1

## Module Summary

Interact and control an Music Player Daemon (MPD) server

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

* Initial release.

[//]: # (Always required)
*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

## Requirements

Requires a functional MPD server setup.

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Set the *IP Address* and *Port Number* (default <code>6600</code>) to that configured on the device.

Checking the *Extended Logging* checkbox will provide more detailed log messages.\
Checking the *Comms Logging* checkbox will provide more detailed log messages about the commands sent.\
These are intended for diagnostics and problem solving and should ideally be disabled during normal operation.

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
        <td>Playback State</td>
        <td>Current playback state</td>
            <ul style="margin-top:0px;">
                <li><code>play</code></li>
                <li><code>stop</code></li>
                <li><code>pause</code></li>
            </ul>
    </tr>
    <tr>
        <td>Song artist</td>
        <td>Artist of the song in playback</td>
    </tr>
    <tr>
        <td>Song title</td>
        <td>Title of the song in playback</td>
    </tr>
    <tr>
        <td>Song album</td>
        <td>Album of the song in playback</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Connected

Fires when the Controller is connected to the MPD server.

#### Disconnected

Fires when the Controller is disconnected from the MPD server.

#### Playback state

Fires when the playback state matches *State*.

Trigger variables:

* *Variable 1*: Playback state: "play", "pause", "stop" (*string*).

#### New song

Fires when a new song is in playback.

Trigger variables:

* *Variable 1*: Song artist (*string*).
* *Variable 2*: Song title (*string*).
* *Variable 3*: Song album (*string*).

### Conditions

#### Playback state

Returns true if *State* matches the current playback state.

### Actions

#### Play

Sends a request to start playback.

#### Pause

Sends a request to pause playback.

#### Stop

Sends a request to stop playback.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
