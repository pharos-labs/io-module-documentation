# Colour tools - Version 2.1.0.BETA1

<head>
    <style type="text/css">
    td {
        padding: 3 10px;
    }
    </style>
</head>

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Colour helper tools, used to convert between colour spaces.

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

* **Important** Improvements with Designer allow for inputs to be values or variables. Variable indexes have been replaced<sup>[1]</sup>.
**Updated projects will need to be modified accordingly.**
* Added conversions between RGB and HSI.
* Added conversions between RGB and HSV.

[1] Requires that *Trigger Variables* is enabled within Designer's *Project Features*

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

All functions are implemented as Conditions, allowing the variables captured by the Trigger to be adjusted before being passed to the Action. As such, if the Condition is set to negate, the Trigger will not fire.

In all modification Conditions, the modified value does not replace the existing variable; it will be added to the end of the Trigger table. In order to confirm the captured and modified variables, check Controllers logs. Multiple Conditions can be used to perform multiple modifications, but a new variable is created each time, so care must be taken with the variable numbers being used.

<b>Note:</b> If you are using multiple Controllers in a project, you will need to ensure that the Trigger has been set to Test Conditions on the Controllers that has been set to be the Network Primary in your project.

### Conditions

#### CCT to Byte

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>Correlated color temperature (CCT)</td>
            <td>1000-25000 kelvin</td>
        </tr>
        <tr>
            <td>Output</td>
            <td>Normalised from *Maximum* and *Minimum* and scaled using *Scaling*</td>
            <td>0-255</td>
        </tr>
    </tbody>
</table>

#### CCT to DALI DT8(Tc)

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>Correlated color temperature (CCT)</td>
            <td>1000-25000 kelvin</td>
        </tr>
        <tr>
            <td>Output</td>
            <td>Suitable for passing to action <code>Set DALI Output</code></td>
            <td>0-255</td>
        </tr>
    </tbody>
</table>


#### CCT to Mired

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>Correlated color temperature (CCT)</td>
            <td>1000-25000 kelvin</td>
        </tr>
        <tr>
            <td>Output</td>
            <td>Micro reciprocal degree (Mired)</td>
            <td>Reciprocal megakelvin (MK<sup>−1</sup>)</td>
        </tr>
    </tbody>
</table>


#### CCT to RGB

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>Correlated color temperature (CCT)</td>
            <td>1000-25000 kelvin</td>
        </tr>
        <tr>
            <td>Output</td>
            <td>RGB in the selected <code>Model</code> and applied <code>Gamma</code></td>
            <td>0-255<sup>a</sup>, 0-255<sup>a</sup>, 0-255<sup>a</sup></td>
        </tr>
    </tbody>
</table>

<i><sup>a</sup>Scaled to fit 0-255</i>

#### CCT to XYZ

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>Correlated color temperature (CCT)</td>
            <td>1000-25000 kelvin</td>
        </tr>
        <tr>
            <td>Output</td>
            <td>CIE 1931 XYZ</td>
            <td>0.0-1.0, 0.0-1.0, 0.0-1.0</td>
        </tr>
    </tbody>
</table>

#### CCT to xyY

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>Correlated color temperature (CCT)</td>
            <td>4000-25000 kelvin</td>
        </tr>
        <tr>
            <td>Output</td>
            <td>CIE 1931 xyY</td>
            <td>0.0-1.0, 0.0-1.0, 0.0-1.0</td>
        </tr>
    </tbody>
</table>

#### HSI to RGB

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>Hue, Saturation, Intensity (HSI)</td>
            <td>0.0-360.0, 0.0-1.0, 0-255</td>
        </tr>
        <tr>
            <td>Output</td>
            <td>RGB</td>
            <td>0-255, 0-255, 0-255</td>
        </tr>
    </tbody>
</table>

#### HSV to RGB

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>Hue, Saturation, Value<sup>a</sup> (HSV)</td>
            <td>0.0-360.0, 0.0-1.0, 0-255</td>
        </tr>
        <tr>
            <td>Output</td>
            <td>RGB</td>
            <td>0-255, 0-255, 0-255</td>
        </tr>
    </tbody>
</table>

<i><sup>a</sup>Also referred to as Brightness (HSB).</i>

#### Mired to CCT

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>Micro reciprocal degree (Mired)</td>
            <td>Reciprocal megakelvin (MK<sup>−1</sup>)</td>
        </tr>
        <tr>
            <td>Output</td>
            <td>Correlated color temperature (CCT)</td>
            <td>kelvin</td>
        </tr>
    </tbody>
</table>

#### RGB to HSI

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>RGB</td>
            <td>0-255, 0-255, 0-255</td>
        </tr>
        <tr>
            <td>Output</td>
            <td>Hue, Saturation, Intensity (HSI)</td>
            <td>0.0-360.0, 0.0-1.0, 0-255</td>
        </tr>
    </tbody>
</table>

#### RGB to HSV

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>RGB</td>
            <td>0-255, 0-255, 0-255</td>
        </tr>
        <tr>
            <td>Output</td>
            <td>Hue, Saturation, Value<sup>a</sup> (HSV)</td>
            <td>0.0-360.0, 0.0-1.0, 0-255</td>
        </tr>
    </tbody>
</table>

<i><sup>a</sup>Also referred to as Brightness (HSB).</i>

#### RGB to XYZ

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>RGB in the selected <code>Model</code> and applied <code>Gamma</code></td>
            <td>0-255, 0-255, 0-255</td>
        </tr>
        <tr>
            <td>Output</td>
            <td>CIE 1931 XYZ in the selected <code>White point</code></td>
            <td>0.0-1.0, 0.0-1.0, 0.0-1.0</td>
        </tr>
    </tbody>
</table>

#### RGB to xyY

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>RGB in the selected <code>Model</code> and applied <code>Gamma</code></td>
            <td>0-255, 0-255, 0-255</td>
        </tr>
        <tr>
            <td>Output</td>
            <td>CIE 1931 xyY in the selected <code>White point</code></td>
            <td>0.0-1.0, 0.0-1.0, 0.0-1.0</td>
        </tr>
    </tbody>
</table>

#### XYZ to RGB

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>CIE 1931 XYZ in the selected <code>White point</code></td>
            <td>0.0-1.0, 0.0-1.0, 0.0-1.0</td>
        </tr>
        <tr>
            <td>Output</td>
            <td>RGB in the selected <code>Model</code> and applied <code>Gamma</code></td>
            <td>0-255<sup>a</sup>, 0-255<sup>a</sup>, 0-255<sup>a</sup></td>
        </tr>
    </tbody>
</table>

<i><sup>a</sup>Range can be exceeded if the input is outside of the selected RGB model gamut.</i>

#### XYZ to xyY

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>CIE 1931 XYZ</td>
            <td>0.0-1.0, 0.0-1.0, 0.0-1.0</td>
        </tr>
        <tr>
            <td>Output</td>
            <td>CIE 1931 xyY</td>
            <td>0.0-1.0, 0.0-1.0, 0.0-1.0</td>
        </tr>
    </tbody>
</table>

#### xyY to RGB

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>CIE 1931 xyY in the selected <code>White point</code></td>
            <td>0.0-1.0, 0.0-1.0, 0.0-1.0<sup>a</sup></td>
        </tr>
        <tr>
            <td>Output</td>
            <td>RGB in the selected <code>Model</code> and applied <code>Gamma</code></td>
            <td>0-255<sup>b</sup>, 0-255<sup>b</sup>, 0-255<sup>b</sup></td>
        </tr>
    </tbody>
</table>

<i><sup>a</sup>Defaults to 1.0 (aka 100%)</i><br>
<i><sup>b</sup>Range can be exceeded if the input is outside of the selected RGB model gamut.</i>

#### xyY to XYZ

<table>
    <tbody>
        <tr>
            <td>Input</td>
            <td>CIE 1931 xyY</td>
            <td>0.0-1.0, 0.0-1.0, 0.0-1.0<sup>a</sup></td>
        </tr>
        <tr>
            <td>Output</td>
            <td>CIE 1931 XYZ</td>
            <td>0.0-1.0, 0.0-1.0, 0.0-1.0</td>
        </tr>
    </tbody>
</table>

<i><sup>a</sup>Defaults to 1.0 (aka 100%)</i>

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
