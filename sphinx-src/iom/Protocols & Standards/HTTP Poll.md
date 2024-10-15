# HTTP Poll - Version 2.2.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Polls a remote host or device's web server to test its availability.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.2

* &nbsp;Added *Log Triggers, Conditions and Actions* Instance option.
* &nbsp;Added more *Extended Logging* log messages.
* &nbsp;Added more *Last Error* status variable.
* &nbsp;Added more *Last Local Network Status* status variable.
* &nbsp;Fixed bug that would prevent online status after an error.

#### Version 2.1

* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;Updated documentation.
* &nbsp;Added *Extended Logging* instance property.
* &nbsp;Added *Only Trigger on Change* instance property.
* &nbsp;Added *Device Online* condition.
* &nbsp;Added detailed status variables for online status and last received status code.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

The target device/host must be hosting a web server to be able to return a HTTP response from a GET request.

### Instance Properties

*Hostname* and *Port* must be set to match the remote device's HTTP web server settings.

*Path* defines the endpoint which will instigate a HTTP reply. This can be an arbitrary path, providing the remote device will respond to the GET request. As an example, a Controller will always reply to an API call, eg. "/api/timeline".

*Poll Interval* defines how often to send the HTTP request and *Offline Timeout* is used to determine after how long to declare the device offline, if no response is received. If the *Poll Interval* is set to *Disabled* (value 0), then the HTTP request must be made with a *Poll Device* action.

If *Only Trigger on Change* is checked, the *Device Online* and *Device Offline* triggers will only fire when the device status changes, ie. from undiscovered to online, online to offline or offline to online. The *Response Status Code* trigger will also fire if the most recent received code is different from the previously received. If *Only Trigger on Change* is unchecked, triggers will fire on every poll cycle, whether there has been a change in status or not.

Checking the *Extended Logging* checkbox will provide more detailed log messages for triggers, actions and communication. This is intended for diagnostics and problem solving and should be ideally be disabled during normal operation.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Host Name</td>
        <td>Static name set in the Instance properties</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Poll Interval</td>
        <td>Static value set in the Instance properties</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Poll Status</td>
        <td>The uptime or downtime of the polling host</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
        <tr>
        <td>Poll Status</td>
        <td>The uptime or downtime of the polling host</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Last Status Code</td>
        <td>The last status code received from polling the host</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Last Error</td>
        <td>The last error received/detected</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>Last Local Network Status&nbsp;&nbsp;&nbsp;</td>
        <td>The last time the Controller's network interface came up and down</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Device Online

Fires when the Controller receives a response from the remote device, whatever the response code is. If *Only Trigger on Change* instance property is checked, the *Device Online* trigger will only fire when the device status changes from undiscovered to online, or from offline to online. If unchecked, a *Device Online* trigger will fire for any response received on every poll cycle.

#### Device Offline

Fires when the Controller either received a status code 0 (device offline) or a response is not received in the *Offline Timeout* time and therefore the device is declared as offline. If *Only Trigger on Change* instance property is checked, the *Device Offline* trigger will only fire when the device status changes from online to offline. If unchecked, a *Device Offline* trigger will fire for any status code 0 or a non-response on every poll cycle, but only if the device has previously been seen online. The status code and status code description as passed as trigger variables 1 and 2 respectively.

#### Response Status Code

Fires when any response. If *Only Trigger on Change* instance property is checked, the *Response Status Code* trigger will only fire when the received status code is different to the previously received code. If unchecked, a *Device Offline* trigger will fire for any status code received on every poll cycle. The status code and status code description as passed as trigger variables 1 and 2 respectively.

#### Conditions

#### Device Online

Returns true if the current known status of the remote device is online.

### Actions

#### Poll Device

Manually sends a poll command. This can either be used whilst polling or, if polling is disabled in the *Poll Interval* instance property, this action must be used to retrieve the status of the remote device.

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

[//]: # (### Actions)
[//]: # (This is the end result started by a trigger)

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
