# Color Kinetics KiNET Power/Data Supply Status - Version 2.2.0


## Module Summary

Monitors the status of KiNet power/data supplies by sending and receiving KiNET discovery packets. A trigger will fire if the status is different from previous time the discovery request was sent.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope

**Note: This module is intended for use with 20 or less devices. Whilst this may work on larger installations,**
**we can not guarantee that a Controller will be able to successfully discover all devices and this may also impact on Controller performance.**

If you have any queries about this, please contact or support team.

### Release Notes

#### Version 2.2

* &nbsp;Added option to select *Network Interface*.
* &nbsp;Updated documentation.

#### Version 2.1

* &nbsp;Added *Add Static Device* Action.
* &nbsp;Added *Elide for Cloud* option.

#### Version 2.0

* &nbsp;Initial release.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

### Instance Properties

Select on which *Network Interface* the discovery message should be sent from.
<code>Management Only</code> refers to the main network interface of the Controller and the data interface is either a physical data port or,
in the case of a TPC or LPC, when used with the <code>Use alternate IP address for eDMX output</code>*. If this is not configured and <code>Data (Network 2)</code> is selected, the
main network interface will be used.

If *Use Both* is selected, the broadcast message will be sent over both the management and data port and will result in two discovery replies being received.
This does not affect how the modules functions but may result in duplicate replies.

The *Poll Interval* determines how often to send discovery messages. The minimum time is <code>5</code> seconds and the maximum is <code>86400</code> seconds (24 hours). Polling can be disabled by setting the *Poll Interval* to 1 (or scrolling below 2).

If *Poll at Startup* is enabled then polling will automatically start once the controller's NIC is up.

If a previously seen device has not been heard of within the given *Timeout* period, the *Discovery Reply* trigger will fire with the offline status. The trigger will only fire on a poll interval so, if for example, the *Poll Interval* is set to 10 seconds and the *Timeout* is set to 5 seconds, then the trigger will only fire after the 10 second interval. Although it won't affect the working of the module, it is sensible to set the *Timeout* to greater than the *Poll Interval*.

If *Include Serial Number* is checked, the serial number will appear in the status variables in the web UI, the controller log. The serial number is always passed as the first trigger variable.

If *Include IP Address* is checked, the IP address will appear in the status variables in the web UI, the controller log and will be passed as a status variable.

If *Include Device Type* is checked, if the device type is matched against a pre-defined list of device types, the type will appear in the status variables in the web UI, the controller log and will be passed as a status variable.

As Cloud only allows for 120 characters in the status variables, if *Elide for Cloud* is checked, the status variable strings will be trimmed at 120 characters to display correctly in Cloud, otherwise all information will be displayed in the controller's web interface.

If none of the above three options are checked, the status variables will default to the serial number.

The *Extended Logging* function will give you detailed communication logs. This is intended for diagnostics purposes only and it is strongly advised that it is disabled on a live project. This option does not affect the view in the web interface.

### Triggers

#### Discovery Reply

The *Discovery Reply* trigger can be fired when a KiNet power/data supply status is noticed to have changed; one trigger fired for each reply received. The trigger properties allow each trigger to monitor *Online*, *Offline* or *Any* status and a specific *Serial Number* or any *Serial Number* by typing the string <code>any</code> in to the text box.  Online and offline statuses will appear in the IO module tab of the web interface.

Trigger Variables:

Variable 1 and 2 will always be passed as variables:

* &nbsp;*Variable 1*: Serial Number (*string*).
* &nbsp;*Variable 2*: Online Status: 0 is offline, 1 is online (*integer*).

The existence of variable 3 and 4 is dependant on the options selected for *Include IP Address* and *Include Device Type* in the instance properties.

* &nbsp;*Variable 3*: IP Address (*if included*) (*string*).
* &nbsp;*Variable 3/4*: Device Type (*if included*) (*string*).

### Conditions

#### Device Online

The *Device Online* condition will allow a trigger to fire if the currently stored status of the KiNet power/data supply, specified by the *Serial Number* is online.

### Actions

#### Send Discovery

The *Send Discovery* action will send a broadcast discovery request for any KiNet power/data supply to respond to. This can be used any time, whether polling is enabled or disabled, but will send the request immediately. If a status is noticed for a given device to have changed, the *Discovery Reply* will fire.

#### Start Polling

*Poll at Startup* is disabled or the *Stop Polling* action has been called, this will restart the discovery poll at the *Poll Interval* time, If *Poll Interval* is disabled, calling this action will be ignored.

#### Stop Polling

If polling is active, the *Stop Polling* action will cease this. Polling can be restarted by calling the *Start Polling* action.

#### Add Static Device

Manually adds a device to the discovery table in the case of a known device. The *IP Address* and *Serial Number* are required but *Device Type* is optional.
The *Initial Status* defines how the device should be shown at startup but will be overridden after a poll cycle.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
