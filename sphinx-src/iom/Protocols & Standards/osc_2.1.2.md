# OSC - Version 2.1.2

<head>
<style type="text/css">
td,
th {
padding-bottom: 10px;
}
th {
    padding-top: 10px;
}
</style>
</head>

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Send and receive Open Sound Control (OSC) messages over UDP.

## Module Status

[//]: # (If still desired provide a status of the module)

This module has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

#### Module Scope

**Note:** This module uses OSC versions 1.0 formatting.

### Release Notes

#### Version 2.1

* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;Fixed rounding error in received OSC values.
* &nbsp;Added new action, *Output Using Values* with the ability to define fixed values or insert trigger variables.
* &nbsp;Added condition, *Convert Value*, to convert an incomming value in to desired number format format (percentage, 8 bit or 0-1 float).
* &nbsp;Added new trigger, *Button Input* for receiving pressed or released (1 or 0) button values.
* &nbsp;Added *Trigger Rate* instance property to optomise controller performance in a network of high OSC traffic.
* &nbsp;Added *Extended Logging* feature for debugging.
* &nbsp;General performance improvements.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

## Operation

### Instance Properties

Within the Instance Properties, specify the *Input* and *Output Ports* for communicating with OSC compatible hardware. If you have different devices set to communicate using different port configurations, use a new Instance for each port configuration.

*Trigger Rate* determines the frequency of processing incoming messages and firing the *Input* trigger. *Normal* is optimised for controller performance and reliability. *High* will process more messages and fire more triggers in a shorter timeframe but may have a significant impact on performance and potentially overload the controller. *Low* will process messages slower but may cause jitter when using sliders.

Checking the *Extended Logging* checkbox will provide more detailed log messages for fired Triggers and Actions as well as responses from the OSC Network. This is intended for problem solving and should be ideally be disabled during normal operation.

### Triggers

#### Input

This Trigger fires when an OSC message is received by the Controller. The message's arguments are simply passed onto the Conditions and Actions as trigger variables.

#### Button Input

This Trigger fires when an OSC button message is received by the Controller. If the button value (1 for pressed or 0 for released) matches the *Button State*, the trigger will fire and pass the button value as a trigger variable. If the value is not a valid button value, the trigger will not fire and this will be logged.

### Conditions

#### Convert Value

This Condition allows the conversion of numeric value types to facilitate communication&nbsp;/&nbsp;integration between OSC devices and other systems. The Condition allows the conversion between *Float*, *Percentage*, and *8 Bit* values for any received trigger variable.

Use the *Variable Number* to specify the variable to be converted by this Condition.

Use the *Conversion Type* to specify the desired conversion type for the variable.

It is important to understand that OSC communicates percentages as a decimal *Float* number between 0 and 1. However, by using this Condition, such a float value can be converted into either an 8 bit number or an integer percentage.

When converting from a *0-1 Float* to either an integer percentage, or 8 bit number, values are rounded up to the nearest whole number. In 8 bit, the float is represented as an 8 bit percentage value, so a 0.5 float would be 128 as an 8 bit number because <code>128/256 = 0.5</code>.

When converting to a *0-1 Float*, values are rounded up to the nearest 2 decimal places.

The *Conversion Type* can be done in any direction between the 3 value types.

**Note** that when this Condition is used, it does *NOT* replace the variable, but rather appends the converted value to the end of the Trigger Variables Table. Please see the below example:

##### Example

The *Convert Value* Condition receives a Trigger Variable Table containing a single variable:

* &nbsp;Variable 1 = 0.75

By using the *Conversion Type*: *0-1 Float to Percentage* the value for variable 1 is converted from 0.75 to 75 (%).

The *Convert Value* Condition appends the converted value to the end of the Trigger Variable Table to be passed onto the Action. The Trigger Variable Table now has 2 variables:

* &nbsp;Variable 1 = 0.75
* &nbsp;Variable 2 = 75

### Actions

The two Actions available are both for outputting OSC messages.

#### Output Using Variables

This Action takes all the trigger variables, and adds them to the OSC message being output as arguments.

Use the *Hostname* to specify the network address (IP or web domain) to which the OSC message will be delivered.

Use the *Address* to specify the OSC address to which the OSC message's arguments will be delivered.

#### Output Using Values

This Action, compared to Output Using Variables, allows both the use of trigger variables, and user-specified values to be used and passed on as an output OSC message.

Use the *Hostname* to specify the network address (IP or web domain) to which the OSC message will be delivered.

Use the *Address* to specify the OSC address to which the OSC message's arguments will be delivered.

There are two types of *Format* available: *Comma Separated Values* and *Type Value Pairs*, see below for more details as the choice of *Format* dictates how the *Values* should be written.

**NOTE** that *Comma Separated Values* is more forgiving as it will assume any value that does not fit its expected type is a string value and still send the OSC message; whereas the *Type Value Pairs* format, being more explicit, will not send if the value does not fit its stated type.

Below is a summary of how values must be written to fit a given value type (for both *Formats*):

<table>
    <thead>
        <tr>
            <th>Value Type</th>
            <th>Syntax</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;"><code>string</code></td>
            <td>
                <ul>
                    <li>Value must be surrounded by quotation marks (<code>" "</code>)</li>
                    <li><em>Examples</em>: <code>"Word"</code>, <code>"12 Smith Street"</code></li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;"><code>integer</code></td>
            <td>
                <ul>
                    <li>Value is a number</li>
                    <li>Value has no decimal</li>
                    <li>Value is NOT surrounded by quotation marks (<code>" "</code>)</li>
                    <li><em>Examples</em>: <code>1</code>, <code>15000</code></li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;"><code>float</code></td>
            <td>
                <ul>
                    <li>Value is a number</li>
                    <li>Value HAS a decimal</li>
                    <li>Value is NOT surrounded by quotation marks (<code>" "</code>)</li>
                    <li><em>Examples</em>: <code>0.5</code>, <code>3.14</code></li>
                </ul>
            </td>
        </tr>
        <tr>
            <td colspan=2>
                <p><code>variables</code> are specified using a number surrounded by angle brackets <code>&lt;NUM&gt;</code> <em>Examples</em>: <code>&lt;1&gt;</code>, <code>&lt;4&gt;</code></p>
            </td>
        </tr>
    </tbody>
</table>

##### Comma Separated Values

The comma separated syntax is a simpler *Format* that allows the insertion of both user-specified values and variables to the OSC message. The value type for variables are already known when using this *Format*, so only user-entered values must have their type specified using the above explained syntax.

Values need to be comma separated. Any value that does not fit the abovementioned value type criteria is automatically assumed to be a string. See the following examples:

<table>
    <thead>
        <tr>
            <th>Value String</th>
            <th>Interpreted Value Types</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>1,2.7,"hello",world,"123"</code></td>
            <td>
                <ul>
                    <li><code>1</code> : <code>integer</code></li>
                    <li><code>2.7</code> : <code>float</code></li>
                    <li><code>"hello"</code> : <code>string</code></li>
                    <li><code>world</code> : <code>string</code> (<em>assumed</em>)</li>
                    <li><code>"123"</code> : <code>string</code></li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><code>1,4.5,&lt;1&gt;,"hello",&lt;3&gt;</code></td>
            <td>
                <ul>
                    <li><code>1</code> : <code>integer</code></li>
                    <li><code>4.5</code> : <code>float</code></li>
                    <li><code>&lt;1&gt;</code> : <code>variable 1</code></li>
                    <li><code>"hello"</code> : <code>string</code></li>
                    <li><code>&lt;3&gt;</code> : <code>variable 3</code></li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

##### Type Value Pairs

This *Format* uses a JSON type syntax to explicitly define the value type and value, and allows the insertion of both user-specified values and variables to the OSC message.

Each value is described using a type-value pair surrounded by curly brackets, all values are comma separated. The basic structure is as follows: <code>{"type":"&lt;type&gt;","value":&lt;value&gt;}</code>, where <code>"&lt;type&gt;"</code> can either be:

* &nbsp;<code>"s"</code> to specify a <code>string</code> value type
* &nbsp;<code>"i"</code> to specify an <code>integer</code> value type
* &nbsp;<code>"f"</code> to specify a <code>float</code> value type

The <code>&lt;value&gt;</code> syntax must match the abovementioned format (see 2 tables up).

**Note** this *Format* will NOT SEND if there is a mismatch between the stated value type, and the value syntax. See the following examples for more details:

<table>
    <thead>
        <tr>
            <th>Value String</th>
            <th>Interpreted Value Types</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center;"><code>{"type":"s","value":"hello world"},<br />{"type":"i","value":3},<br />{"type":"f","value":55.2}</code></td>
            <td>
                <ul>
                    <li><code>"hello world"</code> : <code>string</code></li>
                    <li><code>3</code> : <code>integer</code></li>
                    <li><code>55.2</code> : <code>float</code></li>
                    <li><em>No error</em>, OSC message will send</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="text-align: center;"><code>{"type":"i","value":3.7},<br />{"type":"f","value":&lt;2&gt;},<br />{"type":"s","value":Smith}</code></td>
            <td>
                <ul>
                    <li><code>3.7</code> : ERROR: value does not have the correct integer syntax</li>
                    <li><code>&lt;2&gt;</code> : <code>variable 2</code> as a <code>string</code> provided it is a string value</li>
                    <li><code>Smith</code> : ERROR: no quotation marks around value</li>
                    <li><em>Errors found</em>, OSC message will NOT send</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

[//]: # (#### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (#### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (#### Further Notes)
[//]: # (Possible location for further notes, may not be used)
