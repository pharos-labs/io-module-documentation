# Cue Stack - Version 2.1.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Cycles through a defined set of Timelines and Scenes using Actions, acting as a console-style Cue Stack.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1.1
* &nbsp;Correctly handle condition variables.

#### Version 2.1

* &nbsp;Added option to *Loop* through the Cue Stack.
* &nbsp;Added *Release Time*.
* &nbsp;Added *Shuffle* option.
* &nbsp;Improved logging using *Extended Logging* option.
* &nbsp;Added *Is Cue Stack Running* Condition.
* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;Added option to allow *Next/Last Starts Cues* (enabled by default).

## Operation

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Define the *Cues* as a set of Timelines and Scenes, using the comma-dash format for continuous ranges and individual Timelines and Scenes
e. <code>t1-3,s1-3</code> or <code>t1,t3,t5,s1,s3,s5</code>.

The order of Cues in this list will be preserved in the Cue Stack unless *Shuffle* is enabled.

If *Shuffle* is selected, the Cue List order be randomised when the Cue Stack is started or when all Cues have been played.
If *Shuffle* is not selected, the Cues will be defined by the order in the *Cue* Instance property.

Checking *Loop* will allow you to infinitely loop through the Cues using *Next* and *Last* Actions. If unchecked, *Next* on the last Cue or *Previous* on the first Cue will not start a Cue.

If *Release Previous* is checked, when the Cue Stack is started, all other Timelines and Scenes in the Cue Stack will be released, whether started from the Cue Stack or not.

If *Release Previous* is checked, the *Release Time* will be used for releasing all other Timelines and Scenes for *Next*, *Last* and *Stop* Actions.

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

#### Status Variables

The IO module tab of the web interface provides status variables to monitor:

* &nbsp;*Cues*
* &nbsp;*Properties*
* &nbsp;*Last Action*
* &nbsp;*Previous Cue*
* &nbsp;The *Current Cue*
* &nbsp;The *Next Cue*

### Actions

#### Start

Starts the Cue Stack running, using the *Cue Index* as the first Cue in the sequence.

If *Shuffle* is selected, the Cue List order be randomised when the Cue Stack is started or when all Cues have been played.
If *Shuffle* is not selected, the Cues will be defined by the order in the *Cue* Instance property.

#### Next

Plays the next Cue in the sequence.

If *Shuffle* is selected, the Cue List order be randomised when the Cue Stack is started or when all Cues have been played.
If *Shuffle* is not selected, the Cues will be defined by the order in the *Cue* Instance property.

If *Next/Last Starts Cues* is enabled and the Cue Stack is not already running, then the first Cue in the Cue List will be played, otherwise the Cue Stack must first be started using the *Start* Action.

If the current Cue is the last in the Clue Stack and *Loop* is selected, the next Cue to be played will be the first in the Stack.
Otherwise, the Cue Stack will remain on the last Cue.

#### Previous

Plays the previous Cue in the Stack.

If *Shuffle* is selected, the Cue List order be randomised when the Cue Stack is started or when all Cues have been played.
If *Shuffle* is not selected, the Cues will be defined by the order in the *Cue* Instance property.

If *Next/Last Starts Cues* is enabled and the Cue Stack is not already running, then the first Cue in the Cue List will be played, otherwise the Cue Stack must first be started using the *Start* Action.

If the current Cue is the first in the Clue Stack and *Loop* is selected, the next Cue to be played will be the last in the Stack.
Otherwise, the Cue Stack will remain on the first Cue.

#### Pause

Pauses the current Cue (if it is a Timeline).

#### Resume

Resumes the current Cue (if it is a Timeline and in a paused state).

#### Stop

Stops the Cue Stack, releasing the currently running Cue.

### Conditions

#### Timeline In Cue Stack

Returns true if the *Timeline* exists in the Cue Stack Cues. The *Timeline* is a Timeline’s identifying number, not the Cue index.

If the *Variable* option is checked, the number set in the *Timeline* field will be used as an index for a Trigger Variable instead of the *Timeline*.
If the Trigger variable does not exist or is in the wrong format, the Condition will return false.

#### Scene In Cue Stack

Returns true if the *Timeline* exists in the Cue Stack Cues. The *Timeline* is a Timeline’s identifying number, not the Cue index.

If the *Variable* option is checked, the number set in the *Timeline* field will be used as an index for a Trigger Variable instead of the *Timeline*.
If the Trigger variable does not exist or is in the wrong format, the Condition will return false.

#### Is Cue Stack Running

Returns true if the Cue Stack for the specified Instance is in a running state (a Cue is on stage).

#### Example Setup

* *Cues* <code>t1-10</code>
* *Shuffle* <code>Unchecked</code>
* *Loop* <code>Checked</code>
* *Release Previous* <code>Checked</code>
* *Release Time* <code>10.0 seconds</code>
* *Next/Last Starts Cues* <code>Checked</code>
* *Extended Logging* <code>Unchecked</code>

The Triggers below will start the Cue Stack at startup and loop through it continuously in the order defined in *Cues*.

* Trigger 1: *Startup*, Action: *Start* from *Cue Index* <code>1</code>
* Trigger 2: *Timeline Ended*, Condition: In *Timeline In Cue Stack*, Action: *Next*

The Condition in Trigger 2 allows the project to have other Timelines running that aren't part of the Cue Stack.
The Trigger will only be fired when a Cue Stack Timeline ends.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
