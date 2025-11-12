# Pirate Weather - Version 2.0.0.BETA1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

[//]: # (Brief description of the module; usually the same as the description in the package)

Receives weather conditions and forecasts for the project location from Pirate Weather.

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

* &nbsp;Initial release.

[//]: # (Always required)
*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

## Requirements
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)
The module requires the use of an API key, this can be obtained from https://pirate-weather.apiable.io/

## Configuration
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

The module uses the project's location, this should be appropriately set in the Designer Project Properties.

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

[//]: # (### List instance properties and their function)

Set the *API Key* to that obtained from Pirate Weather.

Set *Units* to either *Metric*, *Imperial* or *Mixed (UK)* to set the desired returned units.
<table border="1">
  <thead>
    <tr>
      <th></th>
      <th>Metric</th>
      <th>Imperial</th>
      <th>Mixed (UK)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Precipitation Intensity</td>
      <td><i>mm/hour</i></td>
      <td><i>Inch/hour</i></td>
      <td><i>mm/hour</i></td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td><i>Degrees Celsius</i></td>
      <td><i>Degrees Fahrenheit</i></td>
      <td><i>Degrees Celsius</i></td>
    </tr>
    <tr>
      <td>Pressure</td>
      <td><i>Hectopascals</i></td>
      <td><i>Millibars</i></td>
      <td><i>Hectopascals</i></td>
    </tr>
    <tr>
      <td>Wind Speed</td>
      <td><i>Meters/second</i></td>
      <td><i>Miles/Hour</i></td>
      <td><i>Miles/Hour</i></td>
    </tr>
  </tbody>
</table>

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

### Triggers

[//]: # (Start with a verb such as "Fires when..." or "Receives...")

#### Receive Current Conditions

Fires when a requested report for the current weather matches the selected *summary* item(s).

Trigger variables:

* *Variable 1*: Short summary ('clear-day'|'clear-night'|'rain'|'snow'|'sleet'|'wind'|'fog'|'cloudy'|'partly-cloudy-day'|'partly-cloudy-night').
* *Variable 2*: Precipitation Intensity (*number*).
* *Variable 3*: Temperature (*integer*).
* *Variable 4*: Apparent Temperature
* *Variable 5*: Humidity
* *Variable 6*: Pressure
* *Variable 7*: Wind Speed

#### Receive Hourly Forecast

Fires when a requested weather forecast report for *Time Offset* hour(s), matches the selected *summary* item(s).

Trigger variables:

* *Variable 1*: Short summary ('clear-day'|'clear-night'|'rain'|'snow'|'sleet'|'wind'|'fog'|'cloudy'|'partly-cloudy-day'|'partly-cloudy-night').
* *Variable 2*: Precipitation Intensity (*number*).
* *Variable 3*: Temperature (*integer*).
* *Variable 4*: Apparent Temperature
* *Variable 5*: Humidity
* *Variable 6*: Pressure
* *Variable 7*: Wind Speed

#### Receive Daily Forecast

Fires when a requested weather forecast report for *Time Offset* day(s), matches the selected *summary* item(s).

Trigger variables:

* *Variable 1*: Short summary ('clear-day'|'clear-night'|'rain'|'snow'|'sleet'|'wind'|'fog'|'cloudy'|'partly-cloudy-day'|'partly-cloudy-night').
* *Variable 2*: Precipitation Intensity (*number*).
* *Variable 3*: Temperature (*integer*).
* *Variable 4*: Apparent Temperature
* *Variable 5*: Humidity
* *Variable 6*: Pressure
* *Variable 7*: Wind Speed

### Actions

#### Request Weather Data

[//]: # (Start with a verb such as "Requests..." or "Starts...")

Sends a request for weather data, the results of which will be returned by triggers.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
