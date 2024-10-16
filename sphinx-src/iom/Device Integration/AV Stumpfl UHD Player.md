# AV Stumpfl UHD Player - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Controls an AV Strumpfl UHD player via its API over a UDP connection.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Added status variables.
* &nbsp;Updated documentation.
* &nbsp;Added extra error checking.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Set the *Player IP Address* and *Control Port* to that of the AV Strumpfl UHD Player.
These settings can be found and configured on the Player's web interface.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

### Triggers

#### Playback Query Response

Fires in response to a playback query (get Action) from the player.

If <code>Any</code> *Query* is selected, Trigger variable 1 is the query type (*string*) and variable 2 is the value (*string or integer*).

*Query* <code>Play State</code>: Trigger variable 1 is the state: playing, paused, stopped (*string*).

*Query* <code>Playback Speed</code>: Trigger variable 1 is the speed as a percentage (*integer*).

*Query* <code>Skip Size</code>: Trigger variable 1 is the size in seconds (*integer*).

*Query* <code>Playback Time</code>: Trigger variable 1 is the size in milliseconds (*integer*).

*Query* <code>Time to Finish</code>: Trigger variable 1 is the size in seconds (*integer*).

#### Playback Audio Query Response

Fires in response to an audio query (get Action) from the player.

If <code>Any</code> *Query* is selected, Trigger variable 1 is the query type (*string*) and variable 2 is the value (*string, integer or number*)

*Query* <code>Volume</code>: Trigger variable 1 is the volume from <code>0</code> (mute) to <code>10</code> (highest) (*integer*).

*Query* <code>Muted</code>: Trigger variable 1 is the muted mode <code>0</code> for unmuted and <code>1</code> for muted. (*integer*).


### Actions

#### Playback - Pause

Sends a command to the player to pause the current playback.

#### Playback - Play

Sends a command to the player to start the playback of a media file.

If the playback is stopped, it starts the playback from the beginning of the playlist (or alphanumeric order when no playlist is used).

#### Playback - Toggle

Sends a command to the player to toggle between playback and pause.

#### Playback - Stop

Sends a command to the player to stop playback (the display will turn black).

#### Playback - Next

Sends a command to the player to jump to the next media file.

#### Playback - Play Index

Sends a command to the player to play the media file with the specified *Index* (according to the item number in the playlist or alphanumeric order when no playlist is used).
The play *Index* of alphanumeric order starts with <code>0</code>.

#### Playback - Play File

Sends a command to the player to play the media file according to the specified *File* name (exact *File* name).

#### Playback - Set Speed

Sends a command to the player to sets the playback *Speed* of the current media file (in %).
The playback speed of media files with audio output can only be set to a value between <code>50%</code> and <code>120%</code>.

#### Playback - Set Skip Size

Sends a command to the player to set the *Skip Size* length in seconds.

#### Playback - Skip Forward

Sends a command to the player to skip forward within the playback to the previously set *Skip Size*.

#### Playback - Backward

Sends a command to the player to skip backwards within the playback to the previously set *Skip Size*.

#### Playback - Jump to Time

Sends a command to the player to jump to a certain location within the playback (*Time* in milliseconds).

#### Playback - Jump to Percent

Sends a command to the player to jump to a certain *Time* within the playback (*Percent*.)

#### Playback - Get Play State

Sends a query to the player to get the current playback mode (playing, paused, stopped).

The response will fire a *Playback Query Response* Trigger (*Query* type <code>Play State</code> or <code>Any</code>).

#### Playback - Get Speed

Sends a query to the player to get the current speed.

The response will fire a *Playback Query Response* Trigger (*Query* type <code>Playback Speed</code> or <code>Any</code>).

#### Playback - Get Skip Size

Sends a query to the player to get the current speed.

The response will fire a *Playback Query Response* Trigger (*Query* type <code>Skip Size</code> or <code>Any</code>).

#### Playback - Get Playback Time

Sends a query to the player to get the current playback time in milliseconds.

The response will fire a *Playback Query Response* Trigger (*Query* type <code>Playback Time</code> or <code>Any</code>).

#### Playback - Get Time to Finish

Sends a query to the player to get the remaining playback time of the current media file in seconds.

The response will fire a *Playback Query Response* Trigger (*Query* type <code>Time to Finish</code> or <code>Any</code>).

#### Audio - Volume Up

Sends a command to the player to increase the volume by 1 step.

#### Audio - Volume Down

Sends a command to the player to decrease the volume by 1 step.

#### Audio - Set Volume

Sends a command to the player to set the *Volume* to a specific value: value range from <code>0</code> (mute) to <code>10</code> (highest).

#### Audio - Mute

Sends a command to the player to mute the audio.

#### Audio - Unmute

Sends a command to the player to unmute the audio.

#### Audio - Toggle

Sends a command to the player to toggle between mute and unmute.

#### Audio - Get Volume

Sends a query to the player to get the current playback volume.

The response will fire a *Audio Query Response* Trigger (*Query* type <code>Volume</code> or <code>Any</code>).

#### Audio - Get Muted

Sends a query to the player to get the current mute mode.

The response will fire a *Audio Query Response* Trigger (*Query* type <code>Muted</code> or <code>Any</code>);
<code>0</code> for unmuted and <code>1</code> for muted.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
