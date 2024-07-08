# Set and Get Variables - Version 2.1.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Sets and gets stored values to be used in Actions as Trigger variables.

## Module Status

**Note:** Please be aware that this is an beta version of this IO Module which has not yet been fully tested. We recommend testing before use.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Release Notes

#### Version 2.1

* &nbsp;Renamed *Insert Values* to *Inject Values*.
* &nbsp;Added instance options to *Display Value Keys* and *Display Value Types* in status variables.

#### Version 2.0

* &nbsp;Initial release.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

Allows storing of individual values to later be recalled, when needed.

**Note:** Keys must not contain reserved characters: double quotes <code>"</code> commas <code>,</code> full-stop <code>.</code> or chevrons <code>< ></code> .
If the key contains these character, a match may not be made. Strings containing underscores and dashes are advised.

The module has extensive logging for diagnostic purpose. Select *Extended Logging* in the instance properties for more detailed logs.

All current values can be seen in the IO Module tab of the web interface along with the key name and variable type.

### Instance Properties

Define the variable *Key* names for any number of variables; these are used to reference variables/values in Triggers, Conditions and Actions.
Key fields can be left blank if not required.

Checking the *Display Value Keys* checkbox will display the key of the variable in the web interface status variables.

Checking the *Display Value Type* checkbox will display the type of the value in the web interface status variables.

Checking the *Extended Logging* checkbox will provide more detailed log messages for Triggers, Actions and Conditions associated with the module.

### Triggers

#### Variables Received

Fires in response to a "Get Values" Action.
The values for the *Keys* (in comma separated format) will be passed as Trigger variables, in the order defined in *Keys* field of the Trigger.
If the *Keys* field is empty, values of all the *Keys* in the instance properties will be passed as Trigger variables.
Invalid keys or values will still be passed to maintain the order of the entered *Keys* field of the Trigger.

### Conditions

#### Inject Values

Appends specified values to the end of the Trigger variables list.
The values for the *Keys* (in comma separated format) will be passed as Trigger variables, in the order defined in *Keys* field of the Condition.
If the *Keys* field is empty, values of all the *Keys* in the instance properties will be passed as Trigger variables.
Invalid keys or values will still be passed to maintain the order of the entered *Keys* field of the Condition.

#### Match Values

Retrieves the values for each of the *Keys* and compares them with the *Values*.
The *Values* to match need to be separated by commas and any combination of hard values and variables may be used. Example <code>255,128,<1>,0</code> or <code><1>,<3>,<2>,<4></code>

_All_ of the *Keys*' values must match the *Values* in the same order for the Condition to be matched.

If there are insufficient *Values* to match the number of *Keys* then the Condition will not pass.

### Actions

#### Set Values

Sets single or multiple values of *Keys* to *Values*, defined by comma separated values.
The order of the *Keys* much match the order of the *Values*.

**Note:** If only one value is set in *Values*, for multiple *Keys*, all *Keys* values will be set to the single value (useful for initialising values).
Otherwise, *Keys* and *Values* will be set individually. It's possible to set values to Trigger variables using the format eg. "<1>".
These still need to be separated by commas and any combination of hard values and variables may be used. Example <code>255,128,<1>,0</code> or <code><1>,<3>,<2>,<4></code>

#### Get Values

Fires the *Variables Received* with all variable values. The *Keys* field in the Trigger can be used to filer out values.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in Actions)

### Module Use Example

##### Using a Values Received Trigger

1. Set instance property *Key 1* to **red**, *Key 2* to **green**, *Key 3* to **blue**.
2. From three different *Set Values* Actions, set each value by the keys specified in the instance properties.
(The values can either be set as hard values in the *Values* or using variable format eg. "<1>"):
3. *Set Values* Action 1: *Keys*: **red**, *Values*: **255**.
4. *Set Values* Action 2: *Keys*: **green**, *Values*: **128**.
5. *Set Values* Action 3: *Keys*: **blue**, *Values*: **0**.
6. Enqueue a *Values Received* Trigger, entering they *Keys*: **red, green, blue**.
7. Assign a Set RGB Action to the Trigger, using Trigger variables 1, 2, and 3 to set the red, green and blue values.

</br>

##### Alternatively using an Inject Values Condition:

1. Set instance property *Key 1* to **red**, *Key 2* to **green**, *Key 3* to **blue**.
2. From three different *Set Values* Actions, set each value by the keys specified in the instance properties. (The values can either be set as hard values in the *Values* or using variable format eg. "<1>"):
3. *Set Values* Action 1: *Keys*: **red**, *Values*: **255**.
4. *Set Values* Action 2: *Keys*: **green**, *Values*: **128**.
5. *Set Values* Action 3: *Keys*: **blue**, *Values*: **0**.
6. Add an *Inject Values* Condition between any Trigger and the Set RGB Action, again entering the *Keys*: *red, green, blue*.
7. Assign a Set RGB Action to the Trigger, using Trigger variables 1, 2, and 3 to set the red, green and blue values.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
