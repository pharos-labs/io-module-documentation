# Touch Button Timeline Labels - Version 2.1.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Labels Touch Buttons with the Timeline names of the same number.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope

**Designer 2.14.1 and earlier:** This module will only populate touch button labels on a TPC (touch Controller) and not on a TPS (remote device).\
**Designer 2.14.2 and later:** This module will populate touch button labels on *all* touch devices.

### Release Notes

#### Version 2.1
* &nbsp;Adds variable button suffix width

#### Version 2.0

* &nbsp;General updates and improvements.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

At startup, the Controller will set the button labels.

**Note:** The module only sets button labels. Triggers for the buttons will need to be additionally configured.

### Instance Properties

Enter the *Range* of Timelines in comma-dash format (eg. <code>1-4,8,10</code>) that will be linked to corresponding buttons.

Set the *Button Prefix* property to the format of the button names e.g. <code>"button"</code> if the keys are "button001", "button002" etc.

Set the *Button Suffix Width* property to alter the width of the numeric portion of the button name. Values will be padded, as required, with "0"\
e.g. <code>3</code> produces a key of "button001", <code>4</code> produces a key of "button0001",

Set the *Name Format* of the button label using the tags:
<code>\<number\></code> will be replaced by the Timeline number and <code>\<name\></code> will be replaced by the Timeline name.
Any addition string can be added outside of theses tags.

<code>\<number\>:\<name\></code> might yield a button label of <code>"1:Timeline Red"</code>

[//]: # (### Triggers)

[//]: # (#### Trigger Name)
[//]: # (#### Start with a verb such as "Fires when..." or "Receives...")

[//]: # (### Conditions)

[//]: # (#### Conditions Name)
[//]: # (#### Start with a verb such as "Is met when..." or "Returns true if...")

[//]: # (### Actions)

[//]: # (#### Action Name)
[//]: # (#### Start with a verb such as "Sends..." or "Sets...")

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
