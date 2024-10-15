# Modbus - Version 2.2.0.BETA6

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

[//]: # (Properties should be surrounded by eg. *Property Name*)
[//]: # (Values and options should be surrounded by eg. <code>Value</code>)

## Module Summary

Integrate with Modbus serial and/or ethernet systems as client and/or server

[//]: # (Brief description of the module; usually the same as the description in the package)

## Module Status

[//]: # (This IO Module is stable and has been tested internally.)
**Note:** Please be aware that this is a beta version of this IO Module which has not yet been fully tested. We recommend testing before use.

Version 2.2 is a consolidation of all previous modules, as such previous modules can not be directly updated.\
This module is intended for customers starting a new configuration, or require new features provided.

[//]: # (Always required)
If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

### Module Scope
Supports Client/Server (nee Master/Slave) operation for the following protocols and function codes:
#### Serial:
* RTU
* ASCII

#### Ethernet:
* TCP
* UDP *Un-official standard, uses TCP framing over UDP*
* RTU over TCP *Un-official standard, uses RTU framing over TCP*
* RTU over UDP *Un-official standard, uses RTU framing over UDP*

#### Function codes:
* 01 - Read Coils
* 02 - Read Discrete Inputs
* 03 - Read Holding Registers
* 04 - Read Input Register
* 05 - Write Single Coil
* 06 - Write Single Register
* 15 - Write Multiple Coils *(Server only)*
* 16 - Write Multiple Registers *(Server only)*

### Release Notes

#### Version 2.2 Beta 6
* Single consolidated module
* Added support for RTU Client
* Added support for ASCII Client/Server
* Added support for RTU over TCP Client/Server
* Added support for RTU over UDP Client/Server
* Added support for read/write of single registers as signed 16 bit integers
* Added support for read/write of single registers as half precision floating point numbers
* Fixed allowed *value* range for triggers "Read input registers" and "Read holding registers"
* Allow Unit Identifier 255
* Improved serial framing

[//]: # (Always required)
*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

## Configuration
When using serial protocols, the serial mode and settings must match.
### "Typical" configuration
#### RTU
* Mode: *RS485*
* Baud: *9600* or *19200*
* Data bits: *8*
* Parity: *None*
* Stop bits: *1*

#### ASCII
* Mode: *RS232*
* Baud: *9600* or *19200* <sup>[1]</sup>
* Data bits: *7*
* Parity: *Even*
* Stop bits: *1*

[1] **Note:** Baud rates lower than 19200 are not *currently* recommend.

## Operation

Modbus registers, in this module, are address by physical address, expressed as a base-16 (hex) number.\
Logical address are displayed, for reference, in the Action/Trigger descriptions.

Responses to requests are automatically sent, triggers are only fired to indicate value changes or other events.

Function codes "Read Discrete Inputs" and "Read Input Register" are linked directly to the Controllers local physical inputs.\
"Read Discrete Inputs" offers only a binary value, analog inputs are set at a threshold of 50%.
"Read Input Register" should be used for precise reporting of analog inputs.

Action/trigger functionality may change between operating *Mode*, please note the Action/Trigger descriptions and details below.

**Note:** Modbus registers are defined as an unsigned 16 bit value, which allows for a range of <code>0</code> to <code>65535</code>.\
Some manufactures will use that value to represent a different number type, which should be documented by the manufacturer\
e.g. To allow for negative values, it could be interpreted as a signed 16 bit value, which then allows for the range <code>-32767</code> to <code>+32767</code>.\
This module will return, for registers, a few common and relevant conversions. Please read the Action/Trigger details for specifics.

### Instance Properties

Properties are dependent on operating *Mode* (<code>Client</code> or <code>Server</code>) and the *Protocol*.

Checking the *Extended Logging* checkbox will provide more detailed log messages.\
Checking the *Log Comms* checkbox will provide raw I/O log messages.\
These are intended for diagnostics and problem solving and should ideally be disabled during normal operation.

#### Server

*Server ID* is the local unit ID, the Controller will only accept requests directed to this or the broadcast address (0). A value of <code>ANY</code> will accept all requests.

#### Serial protocols

*Interface* selects the local or remote serial interface to use for this instance.

#### Ethernet protocols

*Port* selects the IP port the instance operates with (default 502). **Care should be taken to ensure that multiple server instances are not using the same *Port*.**\
When operating as a *Client*, *IP Address* is used to set the address of the remote server.

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
        <td>Mode</td>
        <td>Operating mode</td>
            <ul style="margin-top:0px;">
                <li><code>Client</code></li>
                <li><code>Server</code></li>
            </ul>
    </tr>
    <tr>
        <td>Protocol</td>
        <td>Framing protocol</td>
            <ul style="margin-top:0px;">
                <li><code>RTU</code></li>
                <li><code>ASCII</code></li>
                <li><code>TCP</code></li>
                <li><code>UDP</code></li>
                <li><code>RTU over TCP</code></li>
                <li><code>RTU over UDP</code></li>
            </ul>
    </tr>
        <tr>
        <td>Connection</td>
        <td>Connection status</td>
            <ul style="margin-top:0px;">
                <li><code>Disconnected</code></li>
                <li><code>Connecting</code></li>
                <li><code>Connected</code></li>
            </ul>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>

### Triggers

#### Connected

Fires when the controller is connected to the bus/remote peer.\
**Note:** This has little meaning in stateless protocols like UDP and serial.

Trigger variables:

* *Variable 1*: Peer address (*IPAddress*).

#### Disconnected

Fires when the controller is disconnected from the bus/remote peer.\
**Note:** This will not fire with serial protocols.

Trigger variables:

* *Variable 1*: Peer address (*IPAddress*).

#### Exception

##### Client

Fires when a matching exception is received from a remote server.

##### Server

Fires when a matching exception is sent to a remote client.

##### Client/Server

Trigger variables:

* *Variable 1*: Exception code (*integer*).
* *Variable 2*: Exception code description (*string*).

#### Read coils

##### Client

Fires for each coil when Controller receives a matching "Read coils" response frame from the remote server.

##### Server

Fires for each coil when Controller receives a matching "Read coils" request frame from the local server.
*Server ID* is ignored, server is local

##### Client/Server

Trigger variables:

* *Variable 1*: Server ID (*integer*).
* *Variable 2*: Coil physical address (*integer*).
* *Variable 3*: Coil value (*0* or *1*).

#### Read discrete inputs

##### Client

Fires for each discrete input when Controller receives a matching "Read discrete inputs" response frame from the remote server.

##### Server

Fires for each discrete input when Controller receives a matching "Read discrete inputs" request frame from the local server.
*Server ID* is ignored, server is local

##### Client/Server

Trigger variables:

* *Variable 1*: Server ID (*integer*).
* *Variable 2*: Discrete input physical address (*integer*).
* *Variable 3*: Discrete input value (*0* or *1*).

#### Read Holding Registers

##### Client

Fires for each holding register when Controller receives a matching "Read holding registers" response frame from the remote server.

##### Server

Fires for each holding register when Controller receives a matching "Read holding registers" request frame from the local server.
*Server ID* is ignored, server is local

##### Client/Server

Trigger variables:

* *Variable 1*: Server ID (*integer*).
* *Variable 2*: Holding register physical address (*integer*).
* *Variable 3*: Holding register value (*unsigned integer*).
* *Variable 4*: Holding register value (*signed integer*).
* *Variable 5*: Holding register value (*float*).

#### Read input registers

##### Client

Fires for each input register when Controller receives a matching "Read input registers" response frame from the remote server.

Trigger variables:

* *Variable 1*: Server ID (*integer*).
* *Variable 2*: Input register physical address (*integer*).
* *Variable 3*: Input register value (*unsigned integer*).
* *Variable 4*: Input register value (*signed integer*).
* *Variable 5*: Input register value (*float*).

##### Server

Fires for each input register when Controller receives a matching "Read input registers" request frame from the local server.
*Server ID* is ignored, server is local

Trigger variables:

* *Variable 1*: Server ID (*integer*).
* *Variable 2*: Input register physical address (*integer*).
* *Variable 3*: Input register value (*integer*).

#### Write single coil

##### Client

Fires when the Controller receives a matching "Write single coil" success response frame from a remote server.

##### Server

Fires when the Controller receives a matching "Write single coil", or matching part of "Write multiple coils", request frame from a remote client.

##### Client/Server

Trigger variables:

* *Variable 1*: Coil physical address (*integer*).
* *Variable 2*: Coil value (*0* or *1*).

#### Write single register

##### Client

Fires when the Controller receives a matching "Write single register" success response frame from a remote server.

##### Server

Fires when the Controller receives a matching "Write single register", or matching part of "Write multiple registers", request frame from a remote client.

##### Client/Server

Trigger variables:

* *Variable 1*: Holding register physical address (*integer*).
* *Variable 2*: Holding register value (*integer*).

### Conditions

#### Connected

Returns true if connected to bus/remote peer.\
**Note:** This has little meaning in stateless protocols like UDP and serial.

### Actions

#### Read coils

##### Client

Sends a request to the remote server at the address of *Server ID* requesting the value of *Quantity* coil(s) starting at *Physical address*.

##### Server

Fires trigger *Read coils* with coil values of local module instance. *Server ID* is ignored

#### Read discrete inputs

##### Client

Sends a request to the remote server at the address of *Server ID* requesting the value of *Quantity* discrete input(s) starting at *Physical address*.

##### Server

Fires trigger *Read Input Registers* with discrete input values of local module instance. *Server ID* is ignored

#### Read Holding Registers

##### Client

Sends a request to the remote server at the address of *Server ID* requesting the value of *Quantity* holding register(s) starting at *Physical address*.

##### Server

Fires trigger *Read Holding Registers* with holding register values of local module instance. *Server ID* is ignored

#### Read input registers

##### Client

Sends a request to the remote server at the address of *Server ID* requesting the value of *Quantity* input register(s) starting at *Physical address*.

##### Server

Fires trigger *Read Input Registers* with input register values of local module instance. *Server ID* is ignored

#### Write single coil

##### Client

Sends a request to the remote server at the address of *Server ID* to set the *Value* of coil at *Physical address*.

##### Server

Sets the *Value* of the local coil at *Physical address*. *Server ID* is ignored

#### Write single register

##### *Write single register (signed)*
Interprets the register as 16bit signed integer.

##### *Write single register (float)*
Interprets the register as a half precision floating point number.

##### Client

Sends a request to the remote server at the address of *Server ID* to set the *Value* of holding register at *Physical address*.

##### Server

Sets the *Value* of the local holding register at *Physical address*. *Server ID* is ignored

## Support

[//]: # (Always required)
If you encounter any issues with this module, please contact our support team.

[//]: # (### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (### Further Notes)
[//]: # (Possible location for further notes, may not be used)
