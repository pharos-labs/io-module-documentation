# BACnet Server - Version 2.3.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Integrates with a BACnet system by behaving as a BACnet server, to be discovered and controlled by BACnet devices.

## Module Status

**Important Note:**  As BACnet is an extensive and complex protocol, thorough testing is highly recommend testing before use.

This module allows the controller to integrate with a BACNet system by acting as a BACnet Server, supporting a subset of BACnet commands as described in the *Module Scope*, *Supported Service Requests*, and *Operation* sections. The controller is intended to be used as a light-weight BACnet Server. The functionality the module supports should suite the needs of projects requiring BACnet integration. Whilst we don't anticipate extending the functionality mentioned outside of this documentation, we understand that some projects may require additional support. Please contact us if this is the case.

You can refer to the Protocol Implementation Conformance Statement (PICS) below for more information on this IO Module's implementation specification.

This IO Module was developed and extensively tested using a *Siemens PXC100-E.D - Automation station BACnet/IP*. We expect this module to work effectively with other BACNet devices that support the service request commands described below. Please ensure you test for compatibility with your system well in advance of any handover date.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

## Module Scope

#### Supported Objects

This module supports 6 Object Types: *Analog Input*, *Analog Output*, *Analog Value*, *Binary Input*, *Binary Output* and *Binary Values*, and a subset of commands (see below).

#### Supported Service Requests

This module supports and operates using the following Service Requests:

* &nbsp;Read property.
* &nbsp;Read property multiple.
* &nbsp;Write property.
* &nbsp;Subscribe COV.

Read Range Protocol Service is not supported.

Segmented requests and responses, when a message is longer than a device's maximum supported length, are not supported. This will return a valid message-too-long error.

### PICS

The PICS for this BACnet Module is available on request, by contacting support.

### Release Notes

#### Version 2.3.1
* &nbsp;Resolves controller crash on project re-upload

#### Version 2.3

* &nbsp;Fixes and internal improvements.
* &nbsp;Enabling controller security no longer impacts *Auto-Create Input Objects*
* &nbsp;Allow COV subscriptions to operate on ports other than BAC0 (UDP Port 47808)
* &nbsp;Correctly handles 'who-is' with no source specifier bit
* &nbsp;Added support for ReadProperty 'property-list'
* &nbsp;Added command priority support
* &nbsp;Correctly pack arrays in readPropertyMultiple response
* &nbsp;Fully decodes all context tags
* &nbsp;Adds support for 'who-has'

[//]: # (### Also adds support for BBMD but we don't publicise that. It is on request only)

#### Version 2.2

* &nbsp;Fixes and improvements.
* &nbsp;Updated documentation.

#### Version 2.1

* &nbsp;Performance improvements.
* &nbsp;Basic support for routed BACnet systems.
* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;Implemented reading multiple properties from multiple objects and devices.
* &nbsp;Improved error responses.
* &nbsp;Added *Extended Logging*.
* &nbsp;Status variables show current object values and inbound and outbound commands.
* &nbsp;BACNet Change Of Value (COV) subscription and notifications are now supported.
* &nbsp;Added *Execute change triggers* to Set Object Value action.

[//]: # (### Requirements)
[//]: # (This section covers any required items for this module to be able to operate eg subscriptions or API keys.)

### Configuration

This module implements BACNet over IP (BACNet/IP) network communication, consequently all requirements for such a network must be met for successful operation.

[//]: # (Useful brandless documentation that covers BACNet/IP networks if ever it is needed in future http://www.bacnet.org/Tutorial/BACnetIP/default.html)

## Operation

The controller running this module can store values within BACNet objects and allows trigger firing if these values change according to user specified criteria. Through COV notification the controller becomes a server capable of informing subscribed BACNet devices of any value changes.

This module supports Change Of Value (COV) notification; any BACNet device that wishes to receive COV notifications needs to send a subscription request to the controller. This establishes a BACNet Client-Server relationship between the BACNet device (client) and controller (server).

Please note that for the controller to interact with a BACNet network it must initialise the desired objects using the *Initialise Object* action every time the controller is restarted (see below for details). We thus recommend using the *Initialise Object* action for all required objects using a *Startup* trigger.

**Note:** that the *Auto-Create Input Objects* *Instance Property* works like the *Initialise Object* action and, if checked, will automatically create objects for controllers that have physical inputs on start-up.

Status variables in the IO Modules tab of the web interface will show up-to-date system information such as object values, COV subscriptions and inbound and outbound commands.

Yet Another BACnet Explorer (YABE) is a useful tool for testing controller discovery and viewing BACnet object values remotely. This application can be installed from the [Source Forge Website](https://sourceforge.net/projects/yetanotherbacnetexplorer/)

### Instance Properties

The Instance Properties cover all the required properties for setting up the controller as a BACNet device.

Setting the *Instance Number* defines the BACNet Instance Number for the controller. This is its global ID and needs to be unique compared to all other BACNet devices on the same network; it can be any value between 0 and 4,194,302.

The *Local Port* field sets the port for BACNet communication. The default port used for the BACNet/IP protocol is 47808.

Checking the *Auto-Create Input Objects* checkbox will automatically create BACNet input objects for the controller's available physical inputs; this command will not work for any Remote Devices connected to the controller. Additional triggering will be required to keep the Object's Present-Value in sync with the inputs on the controller. **Note** that this command will create objects for all available inputs and only work for controllers possessing physical inputs.

Providing a description within the *Device Location* field will populate the Device Location property for the controller that can be read by the BACNet System. This is optional.

Similarly, providing information within the *Device Description* field will populate the Device Description property for the controller that can then be read by the BACNet System. If this is left blank the Device Description property will be set to the controller's model name and serial number.

Checking the *Extended Logging* checkbox will provide more detailed log messages for fired Triggers and Actions as well as responses from the Xicato network.

Running multiple instances of this module is supported. Each instance of the module will create a new BACNet device with its own *Instance Number*.

Status variables in the IO Modules tab of the web interface will show up-to-date system information such as object values, COV subscriptions and inbound and outbound commands.

### Triggers

#### Object Present-Value Changed

When the controller receives an Object Present Value change, this trigger will be fired.

*Object Type* allows the trigger to be configured to work off either Any of the available Object Types, or a specific one.

*Instance Number* refers to the Object Instance Number and can also take a value of Any; this can be used to restrict the trigger to listen for a value change on a single object.

*Type* is used to define the value change the trigger will respond to, this can be set to the following criteria:

* &nbsp;Any value (*Type: Any*) where the Minimum, Maximum and Exact properties are ignored.
* &nbsp;To an exact value (*Type: Exactly*): using the Exact property and Minimum and Maximum properties are ignored.
* &nbsp;Within a range (*Type: Range*): using the Minimum and Maximum properties (Exact will be ignored).

If all criteria are matched, the fired trigger will pass the variables of *Object Type*, *Instance Number*, and changed value itself.

[//]: # (#### Conditions)

### Actions

#### Initialise Object

Creates a new BACnet Object on the controller. Upon controller restart any and all Objects will be forgotten by the controller. It is thus crucial to initialise/create the required Objects upon start-up for them to be discoverable by external BACnet devices.

#### Set Object Value

Sets a new value for a specified Object (if it exists). Enabling the *Execute change triggers* checkbox allows for values changed by this action on the controller to fire any relevant *Object Present-Value Changed* triggers listening. If disabled (unchecked) values changed on the controller by this action will not fire any triggers, meaning triggers listening to will only trigger when the controller receives a new value from an external source.

#### Destroy Object

Deletes the BACnet Object from the controller.

### PICS

The Protocol Implementation Conformance Statement (PICS) for this BACnet Module is available to download
[here if used icw a Pharos controller](http://dl.pharoscontrols.com/resources/io_modules/BACnet_Server_IO_Module_PICS.pdf) or
[here if used icw a Mosaic controller](https://www.etcconnect.com/WorkArea/DownloadAsset.aspx?id=10737506276).

[//]: # (#### Variables)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (#### Module Use Example)
[//]: # (#### Further Notes)
