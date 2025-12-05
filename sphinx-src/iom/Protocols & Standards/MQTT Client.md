# MQTT Client - Version 2.3.4

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)

## Module Summary

Subscribes to topics and publishes MQTT messages to a MQTT Broker.

## Module Status

**Note: This module has been tested internally but has limited field testing. Testing is recommended before being used on a live project.**

**Note: This module is intended for use with a limited number of subscriptions. Whilst this may work on larger installations,**
**this may have an impact on Controller performance.**

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

#### Release Notes

#### Version 2.3.4
* &nbsp;Increase required IoM API version to 2.2.1
* &nbsp;Fix ping requests
* &nbsp;Fix publish responses

#### Version 2.3.3
* &nbsp;Improved handling of internal message tracking

#### Version 2.3.2
* &nbsp;Improved support for larger payloads

#### Version 2.3.1
* &nbsp;Added ping timeout
* &nbsp;Minor fix for Designer 2.12
* &nbsp;Improved topic matching

#### Version 2.2.5
* &nbsp;When using SSL, the disconnected handler is now only called once
* &nbsp;Fixed Connect action
* &nbsp;Added support for Last Will and Testament (LWT)

#### Version 2.2

* &nbsp;Fixed an issue where multiple message received in the same packet were not all being processed.

#### Version 2.1

* &nbsp;Added status variables.

#### Version 2.0

* &nbsp;Initial release.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (## Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

[//]: # (## Configuration)
[//]: # (Mention any setup aspects the user should note that are generally done outside the Designer interface)

## Operation

### QoS Definitions

The *QoS Level* defines how the request is delivered to the Broker and the acknowledgements received.

*At Most Once* is the simplest and quickest method and does not require acknowledgement from the Broker. This level an used by default if the QoS level is not known or important.

*At Least Once* expects a simple acknowledgment from the Broker. If the Client does not receive a response from the Broker in the time specified in *QoS Timeout Delay*, the message will be sent again,
the number of times specified in *QoS Max Resend Attempts*. If an acknowledgment is not received within the *QoS Timeout Delay* time, a *QoS Response Timeout* trigger will fire if one exists in the project. With this QoS level, it is possible that
a message could be sent/received several times.

*Exactly Once* is the highest level service and there is a two-way acknowledgment process (handled in the working of the module) between the MQTT Client and the Broker.
This method comes with higher overheads than the previous two methods, due to the number of message back-and-forth. If an acknowledgment is not received within the *QoS Timeout Delay* time, a *QoS Response Timeout* trigger will fire if one exists in the project.

If the *QoS* level is set to *At Least Once* (1) or *Exactly Once* (2), the Broker's responses which will appear in the Controller log.

When subscribing and publishing, the same QoS level should be set on both the Client and Broker side to ensure the integrity of the message.

### Disconnect

When the controller is rebooted or a new show file is uploaded, it may not always be possible to send a MQTT disconnect message to the Broker before the TCP socket is closed.

### Wildcards

Wildcards (using *#* or *+* in the topic name) can be used in the *Subscribe To Topic* action and *MQTT Message Received* trigger to match any value for a given part of the topic.

A multi-level wildcard hash character (#), matches any number of levels within a topic. A multi-level must only be placed after the last separator.
For example, if a Client subscribes to "hello/world/#", it would receive messages published using these topic names:

* &nbsp;"hello/world/controller"
* &nbsp;"hello/world/controller/trigger"
* &nbsp;"hello/world/controller/trigger/action"

</br>

* &nbsp;"hello/world/# is valid"
* &nbsp;"hello/world# is not valid"
* &nbsp;"hello/world/#/controller is not valid"

A single level wildcard plus character (+) will match only one topic level.
For example, if a Client subscribes to "hello/world/+", it would receive messages published using these topic names:

* &nbsp;"hello/world/controller"
* &nbsp;"hello/world/trigger"

but not:

* &nbsp;"hello/world/controller/trigger"

Single level wildcards can also go between levels so "hello/+/world" would receive messages published using these topic names:

* &nbsp;"hello/controller/world"
* &nbsp;"hello/trigger/world"

### Instance Properties

Set *Broker Name* and *Port Number* to that of the MQTT Broker. A useful tool for testing communication and messaging is [Hive MQ](http://www.mqtt-dashboard.com/).
This uses the host name *broker.hivemq.com* on port *1883*.

[//]: # (The *Secure*, *User Name* and *Password* fields may be required for the MQTT Broker but can be left disabled/blank if not required. **Note:** These features are not implemented in this build.)

The *Keep Alive* time defines how long a connection to the MQTT Broker persists, if no requests are made from the Client. The default is *60* seconds.
If the connection times out, a reconnection will be tried when sending requests from actions or if a *Connect To Broker* action is called.
The minimum is set as 10 seconds as it may take a few seconds to establish a TCP connection, send a connection request and receive a reply from the Broker.
The *Broker Disconnected* trigger can be used to re-initialise a connection and re-subscribe to topics if necessary.

If *Enable SSL* is selected, a secure TCP connection will be used. This should _only_ be used if the MQTT Broker supports it.

The *Client ID* is sent to the MQTT Broker when a connection is initialised. If the *Client ID* field is left blank, a 10 digit random number will be generated.

The *User Name* and *Password* are optional fields, but must be filled if the MQTT broker requires credentials to be used, otherwise, the connection will be refused.

If pings are utilised, then *Ping Timeout* determines the time between a ping being sent and no response (be that ping reply or other) from the remote server, before a disconnect is triggered.

*QoS Timeout Delay* and *QoS Max Resend Attempts* are use for QoS level *At Least Once* (1) and *Exactly Once* (2), when sending Subscribe and Publish requests to the Broker.

For QoS level *At Least Once* (1), if a acknowledgment is not received within the specified *QoS Timeout Delay* then a re-attempt will be tried the number of times specified in *QoS Max Sensed Attempt*.
If an acknowledgment has not been received after these attempts, the *QoS Response Timeout* trigger will fire if one exists in the show file.

For QoS level *Exactly Once* (2), if the two-way acknowledgment sequence does not complete time specified in *QoS Timeout Delay*, the message is deemed undelivered and
the *QoS Response Timeout* trigger will fire if one exists in the show file.

Last Will and Testament (LWT) can be set using *Last Will Topic* and *Last Will Message*.

Connection to the MQTT Broker can be initialised at startup using the *Connect at Startup* option.
This is optional and the Client will send a connection request on any message send, if not already connected, or the connection can be manually established using a *Connect To Broker* action.
It is recommended that *Connect at Startup* is enabled so communication can begin instantly.

When *Disconnect Action Fires Trigger* is enabled, if a *Broker Disconnect* trigger exists in the project, this trigger will fire regardless of how the disconnect happened
(by the Broker, a TCP disconnection, the *Disconnect From Broker* action).
If *Disconnect Action Fires Trigger* is disabled, the trigger will not fire if the disconnect happened by calling a *Disconnect From Broker* action,
but will still fire in other cases.

Checking the *Log Triggers* checkbox will provide more detailed logs for trigger matching.

Checking the *Log Actions* checkbox will show actions in the log.

Checking the *Extended Logging* checkbox will provide more detailed information for communication between the Client and the Broker such as connection status, responses and error messages.

Checking the *Log TCP Comms* checkbox will provide detailed log messages for the TCP connection, including the state (connected or disconnected) of the socket as well as raw TCP data.

**Note:** Logging options are intended for diagnostics and problem solving and should be ideally be disabled during normal operation.

### Status Variables

The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.

<table>
    <tbody>
    <tr class="separator"></tr>
    <tr>
        <td>Broker Name&nbsp;&nbsp;&nbsp;</td>
        <td>The Broker hostname set in the Instance properties.</td>
    </tr>
    <tr>
        <td>Connection</td>
        <td>Whether the Controller is connected or disconnected to the MQTT client.</td>
    </tr>
    <tr>
        <td>Last Action</td>
        <td>The last MQTT Action attempted from the Controller. This may not be representees of commands sent to the Broker if a connection is not established.</td>
    </tr>
        <tr>
        <td>Last Data Received</td>
        <td>The last topic/data information sent for the Broker. This will not show general commands.</td>
    </tr>
    <tr>
        <td>Last Request to Broker&nbsp;&nbsp;&nbsp;</td>
        <td>The last MQTT message sent from the Controller to Broker. This is for all types of messages and may not reflect the Last Action.</td>
    </tr>
    <tr>
        <td>Last Broker Response</td>
        <td>The last MQTT message received from the Broker. This is for all types of messages and may not reflect the Last Data Received.</td>
    </tr>
    <tr class="separator"></tr>
    </tbody>
</table>


### Triggers

#### MQTT Message Received

Fires when an MQTT message is received from the Broker and the received topic string matches the *Topic* property. The *Topic* property can also be left blank to match any received topic
but messages will only be received from topics subscribed to using the *Subscribe to Topic* action. See also *Wildcards* section of the documentation.

If matched, the below trigger variables will be passed to the action:

* &nbsp;*Variable 1* :   Topic name (*string*).
* &nbsp;*Variable 2* :   Message body (*string*).
* &nbsp;*Variable 3-n* : Topic parts (*strings*)

 The message body could contain no data so this variable will be a blank string.

Topic parts are each of this the individual topic levels (split by forward slashes), passed as separate variables.

#### Broker Disconnected

Fires when a disconnect from the Broker is detected. This could be a disconnect initialised by the Broker, an interrupted TCP connection or using a *Disconnect From Broker* Action.

This trigger can be useful if the disconnect is not expected and the actions associated with this trigger can be used to reconnect and re-subscribe if necessary.

If *Disconnect Action Fires Trigger* is disabled, the trigger will not fire if the disconnect happened when a *Disconnect From Broker* action was called,
but will still fire in other cases. This allows for the *Disconnect From Broker* action to assert a disconnect without performing actions associated with a *Broker Disconnected* trigger.

#### Broker Connected

Fires when a MQTT connection is established with the Broker.

#### QoS Response Timeout

Fires when a reply has not been received from the Broker in response to a Publish or Subscribe message, when QoS level of the action is set to *At Least Once* (1), or *Exactly Once* (2).

The trigger will not fire if QoS level is set to *At Most Once* (0) as this level does not invoke a acknowledgment.

See *QoS Definitions* section of the documentation.

### Actions

#### Subscribe To Topic

Sends a request to the MQTT Broker to subscribe to the *Topic*. The *Topic* can be split in to levels using forward slashes eg. "helloworld/trigger". See also *Wildcards* section of the documentation.

For accurate message matching, it is advised that complete topics are subscribed to. Some Brokers may not support wildcards and the connection may be closed if wildcards are detected.

*QoS Level* defines the delivery method of the Subscribe message. See *QoS Definitions* section of the documentation.

When the Broker receives a message to the subscribe-to topic, it will send a message back to the Controller and fire a *MQTT Message Received* trigger.

Depending on the *QoS* level selected, the Broker's responses will appear in the Controller log.
#### Publish To Topic

Sends a request to the MQTT Broker to publish a message using the *Topic*.
The *Topic* must be set and can not contain wildcards (the server may close the connection if it receives a publish topic with a wildcard).
The message *Payload* will be sent along with the message but can be left blank if no data is required.

*QoS Level* defines the delivery method of the Publish message. See *QoS Definitions* section of the documentation.

If *Retain* is set to *Yes*, an instruction is given to the Broker to store the message internally to be send to other Clients as and when they subscribe to a topic.

Depending on the *QoS* level selected, the Broker's responses will appear in the Controller log.

#### Unsubscribe From Topic

Sends a request to the MQTT Broker to unsubscribe from a previously subscribed to the *Topic* (using a *Subscribe To Topic* action).

The Broker will respond to an unsubscribe request with a confirmation which will appear in the Controller log.

#### Connect To Broker

Manually sends a request to the MQTT Broker to create a connection. If a connection is not established, other requests will not be possible and previously subscribe-to topics will
not be honoured. This action is optional and if the Client is not connected to the Broker, when a message attempt is made the Client will automatically request a connection before the message is sent.

The Broker will respond to a connection request with a confirmation which will appear in the Controller log.

#### Disconnect From Broker

Manually sends a disconnect request to the MQTT Broker to terminate the connection. This will also close the TCP connection.

The Broker will not respond with a confirmation of disconnection.
If the connection had previously been closed (whether by the Client or Broker), when a message attempt is made the Client will automatically request a connection before the message is sent.

If *Disconnect Action Fires Trigger* is disabled, the *Broker Disconnected* will not fire when a *Disconnect From Broker* action is called but will still fire in other cases.
This allows for the *Disconnect From Broker* action to assert a disconnect without performing actions associated with a *Broker Disconnected* trigger.

#### Ping Broker

Sends an MQTT specific (not ICMP) ping to the Broker.

If *Ping Interval* is set to *Single Ping* then only one ping will be sent, otherwise a ping will be sent at intervals specified in seconds.

If *Log Pings* is enabled, the ping requests and responses will appear in the Controller log, otherwise they will be performed silently (unless *Log TCP Comms* is selected).

#### Stop Ping

Stops repeating pings, if this has been initialised by a *Ping Broker* action.

### Support

If you encounter any issues with this module, please contact our support team.

[//]: # (#### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (#### Further Notes)
[//]: # (Possible location for further notes, may not be used)
