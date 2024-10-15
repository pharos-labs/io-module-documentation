# Internet Host Connection Status - Version 2.0.0

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Sends a HTTP GET request to a server to check the connection and retrieves the WAN address.

## Module Status

This IO Module is stable and has been tested internally, and externally.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

### Release Notes

#### Version 2.0

* &nbsp;Initial implementation.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

The module uses the API <code>api.ipify.org</code> to retrieve the public IP address (WAN address) of the router the Controller uses to connect to the Internet.

**A HTTP GET request is sent to a server and if a response is received, it can be assumed there is not an Internet connection, however this could be that the server is down or unreachable. By default, the module uses Google's DNS server at <code>dns.google/resolve?name=8.8.8.8.in-addr.arpa&type=PTR&cd=true</code> to check for a connection.**

**To check the status of the Pharos Cloud server, the URL is <code>https://primary.sixeye-api.com/version</code>.**

### Instance Properties

*Host URL* is the URL of the remote server to check the connection status of. It must contain either <code>http://</code> or <code>https://</code> and a domain name, with optional path and query.

**If left blank, the module uses the default Google's DNS server at <code>dns.google/resolve?name=8.8.8.8.in-addr.arpa&type=PTR&cd=true</code> to check if an Internet connection is established.**

If *Check On Startup* is checked, a request is made to get the WAN address and another to check the connection to the server at the *Host URL*.

The *Poll Interval* in seconds determines how often to send a request or a value of <code>9</code> will disable polling.

**Note: If a request is already being processed, another request, either from an Action or a poll cycle, the new request will be ignored until a response or an error is received. This is to prevent multiple Triggers firing/false positive results.**

Checking the *Extended Logging* checkbox will provide more detailed log messages for fired Triggers and HTTP responses.

#### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>WAN Address&nbsp;&nbsp;&nbsp;</td>
        <td>The public IP address retrieved from the API at <code>api.ipify.org</code>.</td>
    </tr>
    <tr>
        <td>Host&nbsp;&nbsp;&nbsp;</td>
        <td>Either Google's DNS server or the Host URL.</code></td>
    </tr>
    <tr>
        <td>Last Host Status&nbsp;&nbsp;&nbsp;</td>
        <td>Whether the last HTTP GET request received a response or not.</code></td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### WAN Address Received

Fires in response to a *Get WAN Address* Action.

Trigger variables:

* &nbsp;*Variable 1*: WAN address (*string e.g. "5.2.126.76"*).

#### Host Connection Status

Fires in response to a *Check Host Connection* Action. If the response status matched the *Status* option, the trigger will be matched.

Trigger variables:

* &nbsp;*Variable 1*: Status (*string* "Response Received" or "No Response").

### Conditions

#### Last Connection Status

Returns true if the last connection status matches the *Status* property. The Condition does not send a request but uses the response status from a *Check Host Connection* Action or a poll cycle.

### Actions

#### Get WAN Address

Sends a HTTP GET request to the API at <code>api.ipify.org</code>. The response from the server contains the IP address and fires a *WAN Address Received* Trigger.

#### Check Host Connection

Sends a HTTP GET request to the server at the *Host URL*. The response or lack of will fire a *Host Connection Status* Trigger.

## Support

If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
