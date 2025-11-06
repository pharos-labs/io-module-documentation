# Philips Hue - Version 2.3.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Controls a Philips Hue system.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope

This IO module can only be used to control lights within a configured system. - it does not support configuring a system from scratch.

### Release Notes

#### Version 2.3

* &nbsp;Adds support for Philips Hue Pro bridges by adding support for HTTPs.

#### Version 2.2

* &nbsp;Added *Transition Time* to *Recall Scene* Action.

#### Version 2.1

* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;General updates and improvements.
* &nbsp;Added status variables.
* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

## Configuration

Firstly, set up and configure our Philips Hue system using one of the standard apps. This IO module can only be used to control lights within a configured system. - it does not support configuring a system from scratch.

1. Ensure the Hue bridge and your Controller (time server) are both connected to the same network, and that the Hue lights can be controlled from your smartphone app.

2. Go to the settings menu in the Hue app. Select the bridge to view its settings. Go to network settings. Switch off the DHCP toggle. It is recommended setting a static IP for your hue bridge so that its IP address will never change - but alternatively just make a note of the IP address shown (which is the one assigned by DHCP) and then switch DHCP back on again.

3. In Designer fill in Bridge IP field within the instance settings with the IP address of the bridge.

4. Next go to a web browser (on the same network as the hue bridge). Go to the address http://\<bridge ip address>/debug/clip.html to access the CLIP API Debugger of the Hue Bridge.

5. In the URL box enter: /api

6. In the Message Body box enter: {"devicetype":"Controller"}

7. Click on the POST button. You will see a response on the Command Response box that starts with "error". That is expected. Now press the button on the top of the Hue Bridge and then press the POST button again. This time you should get a success response that includes a username that is an unintelligible string of characters within double quotes. Copy that string (without the double quotes) and paste it into the Username field within the instance settings in Designer. You have now set everything that is required for your Controller to control the Hue Bridge.

8. Finally it is helpful to export the configuration of your Hue bridge, as it contains ID numbers that will be needed to control it from your Controller. In the CLIP API Debugger modify the URL to be: /api/\<username> where username is the string previously copied in step 6. Click on the GET button and a lengthy text response will be displayed in the Command Response box. Copy that response text and paste it into a text editor so it can later be referred to. The file is in clearly marked sections - "lights" lists all the Hue lights in your system; "groups" shows how these lights are grouped (in rooms); further down "scenes" shows any scenes that have been created or have been auto-created. Scenes are identified by automatically generated character strings that will need to be copied from this file into Designer, to recall a scene in the Hue system from your Controller.

Where appropriate the Controller Actions for controlling Hue can be targeted at individual lights or groups. Note that group number 0 means the entire Hue system.

Please note, it is recommended that "lights" commands are limited to 10 per second and that "groups" commands are limited to 1 per second.

## Operation

[//]: # (Give all the operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

One module instance must be created for each Hue bridge in a system.

### Instance Properties

[//]: # (Describe relevant instance properties if there are any beyond the name)

*Bridge IP* is the IPv4 address of the Hue bridge.

Enter the *Username* retrieved from step 7. of the *Configuration above*, above

Check *Use HTTPS* to enable the use of secure HTTP as required by the bridge.

[//]: # (### Triggers)
[//]: # (An event received by the Controller that can be acted upon to create a reAction)

[//]: # (### Conditions)
[//]: # (Conditions are other criteria that need to be met after a trigger to activate an Action)

### Actions

#### Set Brightness

Set the *Target* type and *Number* of the <code>Group</code> or <code>Light</code> to be controlled. A list of groups and lights can be retrieved using step 8. in Configuration above.

Set the eight-bit *Brightness* and specify the *Fade Time* in seconds. This is the transition time between the current lighting state and the target brightness.

#### Set RGB

Set the *Target* type and *Number* of the <code>Group</code> or <code>Light</code> to be controlled. A list of groups and lights can be retrieved using step 8. in Configuration above.

Set the eight-bit *Red*, *Green* and *Blue* values and specify the *Fade Time* in seconds. This is the transition time between the current lighting state and the target colour.

#### Set HSB

Set the *Target* type and *Number* of the <code>Group</code> or <code>Light</code> to be controlled. A list of groups and lights can be retrieved using step 8. in Configuration above.

Set the 16-bit *Hue* and 8-bit *Saturation* and *Brightness* values and specify the *Fade Time* in seconds. This is the transition time between the current lighting state and the target colour.

#### Set XY

Set the *Target* type and *Number* of the <code>Group</code> or <code>Light</code> to be controlled. A list of groups and lights can be retrieved using step 8. in Configuration above.

Set the CIE 0-1 *X* and *Y* values and specify the *Fade Time* in seconds. This is the transition time between the current lighting state and the target colour.

#### Set Colour Temperature

Set the *Target* type and *Number* of the <code>Group</code> or <code>Light</code> to be controlled. A list of groups and lights can be retrieved using step 8. in Configuration above.

Set the *Colour Temperature* value (153 (6500K) to 500 (2000K)) and specify the *Fade Time* in seconds. This is the transition time between the current lighting state and the target colour temperature.

#### Recall Scene

Set the *Scene Number* and the *Group* on which to apply the scene and specify the *Fade Time* in seconds. A list of scenes and groups these can be retrieved using step 8. in Configuration above.

#### Set Effect

Set the *Target* type and *Number* of the <code>Group</code> or <code>Light</code> on which to apply the effect. A list of groups and lights can be retrieved using step 8. in Configuration above.

The *Effect* can be started by selecting *Colour Loop* or stopped by selecting *None*.

#### Increment Brightness

Set the *Target* type and *Number* of the <code>Group</code> or <code>Light</code> to be controlled. A list of groups and lights can be retrieved using step 8. in Configuration above.

Set the percentage brightness *Increment* and specify the *Fade Time* in seconds. This is the transition time between the current lighting state and the target brightness. If lights are at different level, each will change proportionally to the *Increment* value.

#### Increment Hue

Set the *Target* type and *Number* of the <code>Group</code> or <code>Light</code> to be controlled. A list of groups and lights can be retrieved using step 8. in Configuration above.

Set the percentage hue *Increment* and specify the *Fade Time* in seconds. This is the transition time between the current lighting state and the target brightness. If lights are at different level, each will change proportionally to the *Increment* value.

#### Increment Saturation

Set the *Target* type and *Number* of the <code>Group</code> or <code>Light</code> to be controlled. A list of groups and lights can be retrieved using step 8. in Configuration above.

Set the percentage saturation *Saturation* and specify the *Fade Time* in seconds. This is the transition time between the current lighting state and the target brightness. If lights are at different level, each will change proportionally to the *Saturation* value.

#### Increment Colour Temperature

Set the *Target* type and *Number* of the <code>Group</code> or <code>Light</code> to be controlled. A list of groups and lights can be retrieved using step 8. in Configuration above.

Set the percentage colour temperature *Increment* and specify the *Fade Time* in seconds. This is the transition time between the current lighting state and the target brightness. If lights are at different level, each will change proportionally to the *Increment* value.

#### Alert

The alert effect is a temporary change to the bulb’s state.

Set the *Target* type and *Number* of the <code>Group</code> or <code>Light</code> to be controlled. A list of groups and lights can be retrieved using step 8. in Configuration above.

*State* *None* will stop the alert, *Single* will perform one "breath cycle" and *Continuous* will perform the "breathe cycle" for 15 seconds unless the *None* Action is called.

[//]: # (### Variables)
[//]: # (Variables are a way of collecting numbers from inputs and using them in Actions)

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
