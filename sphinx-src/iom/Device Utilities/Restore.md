# Restore - Version 2.1.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Saves current scene and timeline states to disk for restoration later.

### <u>Important note</u>
<b>This module writes to the controllers flash disk.\
Flash disks have a limited write count, and useable lifespan <i>could</i> be reduced by this module.\
For advice further please contact our support team.
</b>

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

#### Version 2.1

* Multi-controller improvements.

#### Version 2.0

* Initial release.

[//]: # (Always required)
*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Module Properties

[//]: # (### List instance properties and their function)

Unchecking *Restore on clean startup* will clear the saved states from disk on <i>expected</i> reloads (reboot, project upload, et cetera). Allowing the module to only restore on <i>unexpected</i> reloads (watchdog, power loss, et cetera).\
If *Restore on clean startup* is ticked, then saved states are available for restoration at any point.

### Instance Properties

Checking *Limit to single timeline per group* or *Limit to single scene per group* will limit state saves to a single timeline or scene per group.\
e.g. If Timeline 1 and 2 are in group "A": Timeline 1 is started and then Timeline 2; only the state of Timeline 2 will be saved.\
<i>Ungrouped timelines and scenes will <u>not</u> be limited.</i>

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
        <td>Saved states</td>
        <td>Contents of currently saved restoration file</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Actions

[//]: # (### Actions)

[//]: # (#### Action Name)
[//]: # (Start with a verb such as "Sends..." or "Sets...")

#### Clear saved Scene States

Clear this currently saved scene states from disk.
If *Restore on clean startup* is unticked, this operation happens automatically before a planned reboot or project upload.

#### Restore Scene States

Restore the state of any saved scene states.

#### Save Scene State

Save the *Scene* state to disk.

Properties:

* &nbsp;*Scene*: Scene number.

#### Clear saved Timeline States

Clear this currently saved timelines states from disk.
If *Restore on clean startup* is unticked, this operation happens automatically before a planned reboot or project upload.

#### Restore Timeline States

Restore the state of any saved timeline states.

#### Save Timeline State

Save the *Timeline* state to disk.

Properties:

* &nbsp;*Timeline*: Timeline number.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
