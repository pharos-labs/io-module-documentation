# Controller HTTP API Over... - Version 2.1.0.BETA1

## Module Summary

Send the controller(s) a message containing the equivalent message as would normally be sent as a HTTP request, as shown in the API documentation.

## Module Status

[//]: # (This IO Module is stable and has been tested internally.)
**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope

This module replaces 4 previous separate modules:
* Controller HTTP API Over Serial
* Controller HTTP API Over UDP
* Controller HTTP API Over TCP
* Controller HTTP API Rebroadcast

**Note** This module exposes the internal web interface over unsecured lines, as such will not function if controller security is enabled.

### Release Notes

#### Version 2.1

* Consolidated module, replacing previously separate modules

## Operation

Received messages are processed, and passed on to the appropriate controller(s) HTTP web interface.\
The HTTP response will then be passed back to the the caller.\
**Note** Responses will *only* be from the Network Primary.

The message format is: `{HTTP METHOD} {PATH} {PAYLOAD or QUERY}`

E.g. *Start timeline 1* API call:
> Desired HTTP API call:
>> Method - `POST`\
>> Path - `/api/timeline`\
>> Payload - `{"action":"start", "num": 1}`\
>
> Request message to send over transport link:
>> `POST /api/timeline {"action":"start", "num":1}`
>
> Example response passed to the caller:
>> `204 OK\r\n\r\n`
>


E.g. *Query output DMX 1* API call:
> Desired HTTP API call:
>> Method - `GET`\
>> Path - `/api/output`\
>> Query - `?universe=dmx:1`\
>
> Request message to send over transport link:
>> `GET /api/output ?universe=dmx:1`
>
> Example response passed to the caller:
>> `200 OK\r\n{"channels":[],"disabled":true}\r\n`
>

If the selected transport is Serial, then the message *must* be terminated with either a <code>\r\n</code> or <code>\n</code>.\
e.g. `POST /api/timeline {"action":"start", "num":1}\r\n`

### Instance Properties

The message transport interface is selected with *Transport*, other options dependent on this selection.

*Target* selects if the message is processed only by the <code>Network primary</code>, or <code>All controllers</code>

Checking the *Extended Logging* checkbox will provide more detailed log messages. This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.

#### <code>Serial</code>

*Interface* selects the local or remote serial interface.

#### <code>TCP/IP</code>

*Local Port* sets the local TCP listener port for the remote peer to connect to.

#### <code>UDP/IP</code>

*Local Port* sets the local UDP listener port for the remote peer to send to.\
*Remote Ports* sets the remote peers' UDP port for responses.

## Support

If you encounter any issues with this module, please contact our support team.
