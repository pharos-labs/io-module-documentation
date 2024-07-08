# MET Norway - Version 2.0.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Receives current weather conditions from Norwegian Meteorological Institute using their HTTP API.

## Module Status

This IO Module is stable and has been tested internally, and externally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0.1

* &nbsp;Reply parsing bug fix

#### Version 2.0

* &nbsp;Initial release.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

Using the Norwegian Meteorological Institute HTTP API, the most recent weather information is requested.

A single *Request Conditions* Actions sends a request to receive _all_ of the parameters defined in this module and all Triggers will be fired and matched from this one response.

Requests can be made at any point ie. multiple times per hours but overuse may result in the request being rejected.

### Instance Properties

*Latitude* and *Longitude* define the geographical location on which to retrieve weather data. If this location is not supported, an error will be logged.

*Device Description* is a string that is sent with the HTTP request that identifies the API caller.
Although this is a free-form property, the server may reject the request if it deems the description as invalid, such as a random string characters.

Checking the *Log Comms* checkbox will provide more detailed information on communication with MET server such as errors and raw response. This is intended for diagnostic purposes and should ideally be disabled during normal operation.

Checking the *Log Triggers and Actions* checkbox will provide more detailed log messages when calling Actions and matching Triggers.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Latitude&nbsp;&nbsp;&nbsp;</td>
        <td>Latitude from the instance properties in degrees.</td>
    </tr><tr>
        <td>Longitude&nbsp;&nbsp;&nbsp;</td>
        <td>Longitude from the instance properties in degrees.</td>
    </tr>
    <tr>
        <td>Current Condition&nbsp;&nbsp;&nbsp;</td>
        <td>Description of the current condition. This is the "icon" property in the JSON response.</td>
    </tr>
    <tr>
        <td>Relative Humidity&nbsp;&nbsp;&nbsp;</td>
        <td>In percent.</td>
    </tr>
    <tr>
        <td>Precipitation Amount&nbsp;&nbsp;&nbsp;</td>
        <td>In millimetres.</td>
    </tr>
    <tr>
        <td>Wind Speed&nbsp;&nbsp;&nbsp;</td>
        <td>In meters/second.</td>
    </tr>
    <tr>
        <td>Air Temperature&nbsp;&nbsp;&nbsp;</td>
        <td>In degrees Celsius.</td>
    </tr>
    <tr>
        <td>Air Pressure At Sea Level&nbsp;&nbsp;&nbsp;</td>
        <td>In hPa (Hectopascal).</td>
    </tr>
    <tr>
        <td>Cloud Area FrAction&nbsp;&nbsp;&nbsp;</td>
        <td>In percent.</td>
    </tr>
    <tr>
        <td>Wind Direction&nbsp;&nbsp;&nbsp;</td>
        <td>In degrees.</td>
    </tr>
    <tr>
        <td>Last Data Point&nbsp;&nbsp;&nbsp;</td>
        <td>Time stamp of last data point.</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Current Condition Received

Fires in response to a *Request Condition* Action. If present, this Trigger will always match with a description of the current condition.
This string is the "icon" property of the JSON response.

Trigger variables:

* &nbsp;*Variable 1*: Current condition (*"icon" property as string*).

#### Relative Humidity Received

Fires in response to a *Request Condition* Action.
If the relative humidity value is greater than or request to the *Minimum* value and less than or equal to the *Maximum* value,
the Trigger will match, passing the value as a Trigger variable.

Trigger variables:

* &nbsp;*Variable 1*: Value (*Percent as real number*).
* &nbsp;*Variable 1*: Description (*value and units as string*).

#### Precipitation Amount Received

Fires in response to a *Request Condition* Action.
If the precipitation amount value is greater than or request to the *Minimum* value and less than or equal to the *Maximum* value,
the Trigger will match, passing the value as a Trigger variable.

Trigger variables:

* &nbsp;*Variable 1*: Value (*Millimetres as real number*).
* &nbsp;*Variable 1*: Description (*value and units as string*).

#### Wind Speed Received

Fires in response to a *Request Condition* Action.
If the wind speed value is greater than or request to the *Minimum* value and less than or equal to the *Maximum* value,
the Trigger will match, passing the value as a Trigger variable.

Trigger variables:

* &nbsp;*Variable 1*: Value (*meters/second as real number*).
* &nbsp;*Variable 1*: Description (*value and units as string*).

#### Air Temperature Received

Fires in response to a *Request Condition* Action.
If the air temperature value is greater than or request to the *Minimum* value and less than or equal to the *Maximum* value,
the Trigger will match, passing the value as a Trigger variable.

Trigger variables:

* &nbsp;*Variable 1*: Value (*degrees Celsius as real number*).
* &nbsp;*Variable 1*: Description (*value and units as string*).

#### Air Pressure At Sea Level Received

Fires in response to a *Request Condition* Action.
If the air pressure value is greater than or request to the *Minimum* value and less than or equal to the *Maximum* value,
the Trigger will match, passing the value as a Trigger variable.

Trigger variables:

* &nbsp;*Variable 1*: Value (*hPa (Hectopascal) as real number*).
* &nbsp;*Variable 1*: Description (*value and units as string*).

#### Cloud Area Fraction Received

Fires in response to a *Request Condition* Action.
If the air pressure value is greater than or request to the *Minimum* value and less than or equal to the *Maximum* value,
the Trigger will match, passing the value as a Trigger variable.

Trigger variables:

* &nbsp;*Variable 1*: Value (*fraction as real number*).
* &nbsp;*Variable 1*: Description (*value and units as string*).

#### Wind Direction Received

Fires in response to a *Request Condition* Action.
If the wind direction value is greater than or request to the *Minimum* value and less than or equal to the *Maximum* value,
the Trigger will match, passing the value as a Trigger variable.

Trigger variables:

* &nbsp;*Variable 1*: Value (*degrees as real number*).
* &nbsp;*Variable 1*: Description (*value and units as string*).

[//]: # (### Conditions)

[//]: # (#### Conditions Name)
[//]: # (#### Start with a verb such as "Is met when..." or "Returns true if...")

### Actions

#### Request Conditions

Sends a HTTP API request to the MET server to retrieve data on the last recent data point (past hour).
Requests can be made at any point ie. multiple times per hours but overuse may result in the request being rejected.

The JSON response containing data will contain data on the parameters defined in this module and the respective Trigger will fire for each value.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
