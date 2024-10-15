# IFTTT - Version 2.2.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Integrates with IFTTT to send and receive events using their Webhooks Service.

## Module Status

**Note:** This is a beta version, due to changes in the working of the module and bug fixes. Testing is highly recommended before being used on a project and feedback is appreciated.

**Note:** Due to some changes in the way the module is configured in Designer, updating to this module from an older version may require reconfiguration of your show file. Keep a backup of your previous file, should you need to revert to, or reference it. If you have already updated and confirmed the warning, you can undo the change and update when you are in a position to do so.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)
### Release Notes

#### Version 2.2

* &nbsp;Updated documentation.

#### Version 2.1

* &nbsp;Bug fixes.
* &nbsp;Updated action and trigger names.
* &nbsp;Updated action and trigger descriptions.
* &nbsp;Added *Extended Logging* property for detailed diagnostic logging.
* &nbsp;Updated documentation.

#### Version 2.0
* &nbsp;Added status variables to display outgoing and incoming messages.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

## Configuration

The example in this documentation will send an event to IFTTT (the *Send IFTTT Event* action in Designer) and then receive an event from IFTTT (the *IFTTT Event Received* trigger in Designer). This is purely for demonstrational purposes and the if-this and the then-thats can be configured to use any of the other IFTTT applets.

##### Set up of an IFFTT event trigger:

1. Go to IFTTT.com.
2. Login (or create an account).
4. Click *Create* in the top right of the page.
5. Click the *If This [Add]* button.
6. Search for and select *Webhooks*.
7. Click *Receive a web request*.
8. Give the event a name. This name must match the *Event to Trigger* in Designer and should be descriptive of the event, in this example, "action_from_controller_to_ifttt". Click *Create trigger*.

##### Setup of an IFTTT event:

9. Click *Then That [Add]* button.
10. Search for and select *Webhooks*.
11. Click *Make a web request*.
12. Configure the request properties as follows:

* URL: http://public_ip_address:8000
* Method: POST
* Content Type: application/json
* Body: {"event":trigger_from_ifttt_to_controller,"1":value1, "2":value2, "3":myvalue3}

**Note:** The *public_ip_address* is the address your router uses to connect to the Internet and not the controller's local IP address. The default port and the port in this example is 8000. This must be set in the *Incoming Port* in the instance properties. You may need to set up a port forwarding rule on your router to direct the IFTTT messages to the controller.

The first *key:value* pair must always be the event name. When setting the data variables, the keys must be in number format and must match the trigger variable indexes you'd expect to see on the controller. Keys and values can be surrounded by quotation marks, but these will be removed when converted to trigger variables.

**Note:** Colons, semi-colons, square brackets and slashes are not supported.
Non-alpha-numeric characters allowed in the event name and values are spaces and _ - . , + % ! @ £ $ ^ & * ? ( ) < >


13. Click *Create Action* and *Continue*.
14. You may want to specify an Applet Title (just a description) or you can leave it as the default.
15. Click *Finish*.

##### To obtain the key:

16. Click your user in the top right hand corner.
17. Choose *My Services* and click *Webhooks*
18. Select the *Webhooks* service
19. Click *Documentation*
20. Your key will be displayed at the top of the page. Copy this to the *Key* and paste it to the *Key* text box in instance properties.

## Operation

Create a *Send IFTTT Event* and *IFTTT Event Received* trigger (see below). If configured correctly, once the *Send IFTTT Event* action has been called (for example, from a Startup trigger), IFTTT will receive the event and then send another Webhook event back to the controller to fire the *IFTTT Event Received* trigger.

### Instance Properties

[//]: # (Describe relevant instance properties if there are any beyond the name)

Enter the *Key* retrieved from the setup steps above.

The *Incoming Port* is used for receiving events and should match the port specified when creating the webhook event. You may need to set up a port forwarding rule on your router to direct the IFTTT messages to the controller.

Checking the *Extended Logging* checkbox will provide more detailed log messages for IFTTT messages, triggers and actions.

### Triggers

#### IFTTT Event Received

Fires when a Webhook event is received from IFTTT and the *Event* property  matches the received event name. Any variables included in the Webhook message will be passed into the trigger as variables, where the numerical key is the variable number.

Using the example above, create and *IFTTT Event Received* trigger and set the *Event* name to "trigger_from_ifttt_to_controller" (without the quotation marks).

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

### Actions

#### Send IFTTT Event

Sends a Webhook event to IFTTT to trigger an IFTTT event.

Set the *Event to Trigger* property that will match the event name in the IFTTT trigger. In the example above, "action_from_controller_to_ifttt" (without the quotation marks).

*Data 1*, *Data 2*, and *Data 3*are optional fields should you wish to send variables along with the event.

### Trigger Variables

The keys received from the IFTTT event must be in number format and must match the trigger variable indexes you'd expect to see on the controller. Keys and values can be surrounded by quotation marks, but these will be removed when converted to trigger variables.
## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
