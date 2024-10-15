# Accuweather - Version 2.2.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Receive AccuWeather data for a specified location and fire Triggers based on the received atmospheric, weather, wind, and temperature conditions.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.1

* &nbsp;Added *Now +* and *Weather Condition* properties to *Receive Forecast* Trigger.
* &nbsp;Updated *Extended Logging* instance option.

#### Version 2.1

* &nbsp;Updated module documentation.

#### Version 2.0

* &nbsp;Updated module documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

## Requirements

This IO Module requires an API key from the [AccuWeather Developer Website](https://developer.accuweather.com/). This can be obtained by creating an account, please see the [AccuWeather Packages](https://developer.accuweather.com/packages) as well as their Terms of Service for more information.

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

Each instance of this IO Module will be able to obtain weather information for one location around the world. This is set within the Instance Properties. The API key is required in order for the IO Module to be able to request and receive information about any location.

Using the *Request Current Conditions* and *Request Forecast* Actions allows this IO Module to receive information about current and forecast wind, temperature, and atmospheric conditions.

The dedicated Triggers for receiving current wind, temperature, and atmospheric conditions can be used to pass on weather conditions if they meet specific range criteria for the conditions. Conversely the *Receive Current Conditions* Trigger (that fires after the *Request Current Conditions* Action) receives and passes on all current conditions as Trigger variables.

The *Receive Forecast* Trigger fires in response to the *Request Forecast* Action and will receive (and passes on as Trigger variables) data sets for each future hour. The number of hours / datasets it will receive is set within the Instance Properties by the *Forecast Time frame*.
Alternatively, if *Now +* property is specified, only a single data set will be returned.

### Instance Properties

Paste the your *API Key* obtained after having created an account on the [AccuWeather Developer Website](https://developer.accuweather.com/).

Each instance of this IO Module will be able to retrieve data for one geographic location which is specified in the *Location* field. The *Location* field accepts city names

Select the *Unit* system you wish the received data to use; this can be either Metric or Imperial.

The *Forecast Time frame* specifies the amount of hours into the future that the *Request Forecast* Action and *Receive Forecast* Trigger will request/receive. The maximum that can be requested is 120 hours.

**Note** the maximum forecast hours you can request will depend on the service package you have selected to purchase from the [AccuWeather Packages](https://developer.accuweather.com/packages) page.

Checking the *Extended Logging* checkbox will provide more detailed log messages for fired Triggers and Actions as well as responses from the AccuWeather API.

### Triggers

#### Receive Atmospheric Conditions

Fires in response to receiving AccuWeather data following the *Request Current Conditions* Action. The received parameters must fall within the value ranges specified within the Trigger options.

Set the location to which this Trigger relates by selecting the appropriate *IO module instance*.

The available Trigger options allow the definition a value range within which the following atmospheric condition parameters must fall for the Trigger to proceed:

* &nbsp;*Visibility* as the distance at which an object (or light) can clearly be seen; in <code>meters</code> or <code>miles</code>.
* &nbsp;*Humidity* expressed as a <code>percentage</code>.
* &nbsp;*Pressure* in <code>mbar</code> or <code>inHg</code> (inches of Mercury).
* &nbsp;*Pressure Tendency* that can be either <code>Rising</code>, <code>Steady</code>, or <code>Falling</code>. Setting the value <code>Any</code> will accept any *Pressure Tendency*.

#### Receive Wind Conditions

Fires in response to receiving AccuWeather data following the *Request Current Conditions* Action. The received parameters must fall within the value ranges specified within the Trigger options.

Set the location to which this Trigger relates by selecting the appropriate *IO module instance*.

The available Trigger options allow the definition a value range within which the following wind condition parameters must fall for the Trigger to proceed:

* &nbsp;*Wind Chill* as a <code>numeric factor</code>.
* &nbsp;*Direction* (of wind) as <code>degrees</code> (clockwise from the North Pole being 0 degrees).
* &nbsp;*Wind Speed* in <code>km/h</code> or <code>mph</code>.
* &nbsp;*Wind Gust* (speed) in <code>km/h</code> or <code>mph</code>.

#### Receive Current Conditions

Fires in response to receiving AccuWeather data following the *Request Current Conditions* Action. The received parameters must fall within the value ranges specified within the Trigger options.

Set the location to which this Trigger relates by selecting the appropriate *IO module instance*.

Within the Trigger options specify the *Weather Conditions* that need to be met to fire this Trigger. Specifying *Any* will always fire this Trigger when receiving information after having executed the *Request Current Conditions* Action.

#### Receive Temperature Conditions

Fires in response to receiving AccuWeather data following the *Request Current Conditions* Action. The received parameters must fall within the value ranges specified within the Trigger options.

Set the location to which this Trigger relates by selecting the appropriate *IO module instance*.

The available Trigger options allow the definition a *Temperature Min* to *Temperature Max* value range, in <code>&deg;C</code> or <code>&deg;F</code>, within which the temperature parameter must fall for the Trigger to proceed.

#### Receive Forecast

Fires in response to receiving AccuWeather data following the *Request Forecast* Action.

If *Now +* hours is set to <code>All</code> then forecast information is received as hourly datasets,
for as many hours in the future as specified by the *Forecast Time frame* in the Instance Properties.

Each hour is a single data set and includes the following 3 Trigger variables:

* &nbsp;*Date and Time* as a <code>string</code> for when the forecast is due.
* &nbsp;Description of *Weather Conditions* as a <code>string</code>.
* &nbsp;*Temperature* received as either <code>&deg;C</code> or <code>&deg;F</code>.

If *Now +* hours is set to between <code>1</code> hour and <code>120</code> hours,
then the above three Trigger variables will be passed only for the time specified in *Now +*.
If the *Now +* time is out of range of the *Forecast Time Frame* an error will be displayed in the log and the Trigger will not fire.

The Trigger will match and fire if the *Weather Condition* property is set to <code>Any</code> or the specific *Weather Condition* matches the received condition.
In the case where *Now +* is set to <code>All</code>, only those hour data sets which match the *Weather Condition* will be passed as Trigger variables.

 **Note:** The amount of hours that can be requested for forecast data depends on the package that has been purchased from the [AccuWeather Packages](https://developer.accuweather.com/packages) page.

Set the location to which this Trigger relates by selecting the appropriate *IO module instance*.

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

### Actions

#### Request Current Conditions

Requests the current conditions from AccuWeather for the location specified within the chosen *IO module instance*. The received data is captured by the corresponding *Receive Atmospheric Conditions*, *Receive Wind Conditions*, *Receive Current Conditions*, and *Receive Temperature Conditions* Triggers and can then be passed on as Trigger variables.

#### Request Forecast

Requests a forecast of conditions from AccuWeather for the location specified within the chosen *IO module instance*. Based on the *Forecast Time frame* in the Instance Properties and the purchased package with AccuWeather, it is possible to request forecasts from 1 hour up to 120 hours. The forecast is sent as hourly datasets for as many hours as requested by the *Forecast Time frame*. Each hour is a single data set which includes the following 3 Trigger variables:

* &nbsp;*Date and Time* as a <code>string</code> for when the forecast is due.
* &nbsp;Description of *Weather Conditions* as a <code>string</code>.
* &nbsp;*Temperature* received as either <code>&deg;C</code> or <code>&deg;F</code>.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
