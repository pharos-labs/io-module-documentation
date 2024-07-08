# VideoLan VLC Player Client (HTTP) - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Controls VideoLAN VLC Media Player running on a network connected compute, using the HTTP API.

**Note:** This module replaces the TCP version. The TCP module has been deprecated and no longer supported.

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (This IO Module is stable and has been tested internally.)
[//]: # (**Note:** Please be aware that this is an beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Initial implementation: This module replaces *VideoLAN VLC Player TCP Client*.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

## Configuration

[Download VLC Player from the VideoLAN website](https://www.videolan.org/vlc/#download)

##### Storing Media for playback

By default, VLC player points to its own installation directory for media files, the default for Windows being: `C:\Program Files (x86)\VideoLAN\VLC`.
For ease of use, media files can be placed here or a sub directory or this directory.

The relative file path will need to be prepended to the file name in *Add To Playlist* and *Enqueue To Playlist* Actions.

##### Running VLC Player to Allow Remote Control

Details on how to enable the web interface can be found on the [VLC Wiki](https://wiki.videolan.org/Documentation:Modules/http_intf/#VLC_2.0.0_and_later)

## Operation

One IO module Instance must be created for each VLC Player application.

### Instance Properties

Set the *VLC Player IP Address* and *VLC Player Port Number* to that of the host machine/set when running the commands in the last section.

The *Username* for the HTTP API is not necessarily required and can be left empty in most cases.

The *Password* should match the password set the Configuration settings.

### Status Variables

The IO Modules tab of the web interface provides Status Variables to shows information about the module and monitor its state.

### Triggers

#### Any Response Received

Fires when a response is received from the VLC Player in response to an Action. The first Trigger variable will be the current playback state followed by a result messages, which may be an error.

### Condition

#### Playback State

Matches true if the playback *State* matches the current known *State* of the VLC Player.

### Actions

#### Play Playlist

Starts the playlist running.

If *Item ID* is anything but <code>Optional</code>, the playlist will begin from this item. If the *Item ID* is set to </code>Optional</code> or the VLC Player does not recognise the *Item ID*, the playlist will begin from the start.

**Note:** The *Item ID* may not match the ID in VLC Player. Check the instance status variable in the web interface to find out the correct ID.

#### Play Item and Stop

Plays the *Item ID* once and then stops playback.

**Note:** This Action is not inherently part of the API. The file plays and then the remaining time is used to decide when to stop the playlist. The *Stop Playback* Action will be called when the remaining time reaches 0.

**Note:** The *Item ID* may not match the ID in VLC Player. Check the instance status variable in the web interface to find out the correct ID.

#### Add To Playlist

Adds the media file (*File Name*) to the end of the playlist.

If the media file is anywhere other than the install directory location, the relative file path will need to be prepended to the file name eg. <code>media/file.mov</code>.

#### Add To Playlist and Start Playback

Adds the media file (*File Name*) to the playlist and starts the media file running.

If the file is anywhere other than the install directory location, the relative file path will need to be prepended to the file name eg. <code>media/file.mov</code>.

#### Jump to Next Item Next

Starts the next media file running.

#### Jump To Previous Item

Starts the previous media file running.

#### Pause Playback

Pauses current playback.

#### Toggle Pause

Toggles between playing and pausing the playlist.

#### Resume If Paused

Resumes the playlist it is it currently paused.

#### Stop Playback

Stops all playback.

#### Sort Playback

TODO: API Call does not currently work as expected.

#### Delete Item From Playlist

Deletes the *Item ID* from the playlist.

If the *Item ID* does not exist or is set to <code>None</code>, no  media file will be deleted.

**Note:** The *Item ID* may not match the ID in VLC Player. Check the instance status variable in the web interface to find out the correct ID.

#### Empty Playlist

Clears the entire playlist - use with care.

#### Add Subtitle to Current Playing File

Adds the subtitle file (*File Name*) as displays the text over the current playing file

If the subtitle file is anywhere other than the install directory location, the relative file path will need to be prepended to the file name eg. <code>media/file.mov</code>.

#### Set Volume Level

Sets the *Value* of the volume either as a percentage, absolute value or relative plus or minus *Format*.

#### Set Audio Delay

Sets the audio *Delay* in seconds of the playlist.

#### Set Subtitle Delay

Sets the subtitle *Delay* in seconds of the playlist.

#### Set Playback Rate of Current Item

Sets the playback *Rate* of the current running media file.

**Note:** This applies only to the current item and the rate will be reset when the next media file  plays. This is a limitation of the API.

#### Set Aspect Rate

Sets the aspect *Ratio* of the playlist.

#### Toggle Random Playback

Toggles between random on and off.

#### Toggle Loop

Toggles between loop off and loop all.

**Note:** It is not possible to define the loop type from the Action. This is a limitation of the API.

#### Toggle Repeat

Toggles between repeat on and repeat off.

**Note:** It is not possible to define the repeat type from the Action. This is a limitation of the API.

#### Toggle Fullscreen

Toggles fullscreen mode.

**Note:** It is not possible to define the fullscreen state from the Action. This is a limitation of the API.

#### Execute Command

Executes a custom *Command*.

Most commands of the API are available through Actions, however if there is a *Command* that is not supported, this Action can be used. It is not necessary to prepend <code>?command=</code> to the *Command*.

The list of API commands can be found [on the VLC Wiki](https://wiki.videolan.org/VLC_HTTP_requests/).

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
