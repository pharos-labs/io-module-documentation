# Color Kinetics Ethernet Keypad - Version 2.1.1

## Module Summary

Integrates a Philips Color Kinetics Ethernet and Antumbra Ethernet Keypads.

## Module Status

This IO Module is stable and has been tested internally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope

Compatible Hardware:
* &nbsp;Philips Antumbra 6 Button Keypad with the "Ethernet Communication Module"
* &nbsp;Philips Color Kinetics 11 Button "Ethernet Controller Keypad"
* &nbsp;Philips Color Kinetics iOS "Remote Kpad App" (Always serial number "00000000")

### Release Notes

#### Version 2.1

* &nbsp;Added extra logging.
* &nbsp;Added extra error checking.
* &nbsp;Added *Extended Logging* option.

#### Version 2.0

* &nbsp;Updated documentation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

## Configuration

By default, Keypads have an IP address of 10.x.x.x/8. To configure and communicate with the Keypad, your machine must be in the same range.

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

Specify the Keypad's *IP Address* or set the *IP Address* to <code>255.255.255.255</code> to match any Keypad on the network.

### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Last Button Pressed&nbsp;&nbsp;&nbsp;</td>
        <td>Button number or type</td>
        <td></td>
    </tr>
    <tr>
        <td>Serial Number</td>
        <td>Last received serial number</td>
        <td></td>
    </tr>
    <tr>
        <td>IP Address</td>
        <td>Last IP address received</td>
        <td></td>
    </tr>
        <tr>
        <td>Last Action</td>
        <td>Last outbound command</td>
        <td></td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Button Press

Fires when a specified *Button* <code>Any</code> (or any) is pressed on the keypad of a given instance.

##### Trigger Variables

1. Button ID (*integer*)
2. Serial number (*string*)
3. IP address (*string*)
4. Button description (*string*)

[//]: # (### Conditions)

[//]: # (#### Conditions Name)
[//]: # (#### Start with a verb such as "Is met when..." or "Returns true if...")

### Actions

#### Set LED

Sends a command to Keypad to set an *Effect* on an *LED*.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
