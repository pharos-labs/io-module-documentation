# Ping - Version 2.0.1

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

[//]: # (Brief description of the module; usually the same as the description in the package)

Send an ICMP ping to monitor the online status of a remote peer.

## Module Status

[//]: # (UNCOMMENT AND DELETE AS APPROPRIATE)
[//]: # (**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.)
This IO Module is stable and has been tested internally.

[//]: # (Always required)
If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Initial release.

[//]: # (Always required)
*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

[//]: # (Give operational details linked to using Instance Properties, Triggers, Conditions, Actions, Variables associated with the module's operation)

### Instance Properties

[//]: # (### List instance properties and their function)

Set the *Host* to the hostname or IP address of the remote peer to monitor.

Enabling *Auto Ping?* will automatically send a ping every *Auto Ping Interval* with a reply timeout of *Auto Ping Timeout*.

*TTL* can be used to alter the Time To Live.\
Every device (such as an intermediate router) forwarding an IP datagram first decrements the time to live (*TTL*) field in the IP header by one. If the resulting *TTL* is 0, the packet is discarded.\
In most cases this should remain as the default value.

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <style type="text/css">
    td {
        padding: 3 10px;
    }
    </style>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Status</td>
        <td>The current peer status
            <ul style="margin-top:0px;">
                <li><code>Online</code></li>
                <li><code>Offline</code></li>
                <li><code>Unknown</code></li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>Average time</td>
        <td>Average round trip time</td>
    </tr>
    <tr>
        <td>Packet loss</td>
        <td>Percentage of pings with no response</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Ping Reply

[//]: # (Start with a verb such as "Fires when..." or "Receives...")
Fires when the Controller receives a ping reply.

Trigger variables:

* &nbsp;*Variable 1*: IP Address of responder.
* &nbsp;*Variable 2*: Round trip response time (ms).
* &nbsp;*Variable 3*: TTL of response.

#### Ping Timeout

[//]: # (Start with a verb such as "Fires when..." or "Receives...")
Fires when the Controller times out waiting for a ping reply.

### Conditions

#### Online

[//]: # (Start with a verb such as "Matches if...")
Returns true if the remote peer responded to the last ping request.

### Actions

#### Send Ping

[//]: # (Start with a verb such as "Requests..." or "Starts...")

Sends one ping only to the remote peer, expecting a reply withing *Timeout* milliseconds.

n.b. This cancels any other pending timeouts for this module instance.

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
