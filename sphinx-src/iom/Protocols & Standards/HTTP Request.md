# HTTP Request - Version 2.3.3

[//]: # (THIS IS WHAT A COMMENT LOOKS LIKE)
## Module Summary

Sends a HTTP/HTTPS requests and processes its response.

## Module Status

This IO Module is stable and has been tested internally. We highly recommend testing with your devices prior to being used on a project,
to check for suitability and compatibility.

If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.

[//]: # (#### Module Scope)
[//]: # (If important to mention explain the limitations and things this module cannot perform)

#### Release Notes

#### Version 2.3.3

* &nbsp;Added option to *Verify Peer SSL Certificate*.
* &nbsp;Updated documentation.
* &nbsp;Minor bug fixes.
* &nbsp;Improved hostname validation
* &nbsp;Improved data field validation

#### Version 2.2.2

* &nbsp;Added instance property to skip verification of peer SSL certificate.

#### Version 2.2.1

* &nbsp;Fixed bug to remove multiple '?' from the start of a query.

#### Version 2.2

* &nbsp;Clearer error response logging.
* &nbsp;Added *Log Full Response* option.
* &nbsp;Added support for escaping characters in headers (see references later on in documentation).

#### Version 2.1

* &nbsp;Updated documentation.

#### Version 2.0

* &nbsp;Added option for additional headers.
* &nbsp;Added *Default* *Method*, *Path* and *Data* instance properties.
* &nbsp;Added *Get JSON Values* Condition.
* &nbsp;Added *Extended Logging*.

*Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.*

[//]: # (### Requirements)
[//]: # (Mention any pre-requisites needed before setting up the module in terms of hardware, subscriptions, APIs)

## Operation

This module allows you to make HTTP and HTTPS requests to an external host, such as a Controller, external equipment or, if the Controller is connected to the Internet, remote third party APIs.

The response fires a Trigger and this data can either be used as a raw string or values can be extracted from a JSON file using a Condition.

### Instance Properties

##### Static Properties

Define the *Protocol* as HTTP or HTTPS.

Specify the *Hostname* as a string or IP address.

Specify the destination *Port*. If not specified, the default port for HTTP is *80* and the default port for HTTPS is *443*.

**Note:** The *Protocol*, *Hostname* and *Port* are specific to the module instance. If you need to send a request to a different host or the same host on a different port or using a different *Protocol*, you will be required to create a new instance for each case.

If *Verify Peer SSL Certificate* is checked, the Controller will attempt to verify the host against a list of known SSL certificates. If the Controller is returning authentication errors, disabling this may help.

##### Default Properties

The below default properties will be used for request when the *Make Request* Action is called, unless otherwise specified in the Action. See the instance property's placeholder for example syntax (the text is displayed when no user text is entered into the text field). Note that if the placeholder is showing, this counts as an empty string, not the string of the placeholder.

*Default Method* defines the request method: *GET*, *POST*, *PUT*, or *DELETE*. In most cases, this will be *GET* or *POST*.

Define any addition headers in the *Default Headers* as comma separated strings, using hyphens, equals sign, or colons.
The module will split and send the name and values accordingly, for example "content-type=application" will be split into the header name, "content-type" and value, "application".

**Note: If you wish to use commas, equals signs or spaces as part of the header, they must be escaped with a backwards slash (before the character), otherwise they will be stripped out.**

If *Add JSON Content Type* is enabled, the header: **content-type=application/json** will be added to the headers. Many applications use this format including the Controller HTTP API. If the header is already defined in *Default Headers* or *Headers* in the *Make Request* Action, the header will not be added twice.

Controllers use "content-type=application" by default so this is always set as one of the headers.

The *Default Path* specifies the request to the host and can be left blank if not required.

The *Default Data* specifies the addition query or body of the request and can be left blank if not required. This is in string format, commonly formatted as question-mark-equals format (eg. *?key1=value1&key=value2*) or a JSON array of key-value pairs (eg. *{"key":"value", "key2":"value2"}*)

##### Other Properties

*Read Type* defines how the *Receive Response* Trigger handles the incoming reply. Choosing *Full Response/JSON* will print the whole response in the log and pass the full response string to the Action as a Trigger variable(variable 1). If intending to use the *Extract Value* Condition, this property must be set to *Full Response/JSON*. Otherwise, if the *Line by Line* option is chosen, the Trigger will print each line of the response to the log separately and each line will be passed to the Action as a Trigger variable. This option is not compatible with the *Extract Value* Condition.

Checking the *Extended Logging* checkbox will provide more detailed log messages for fired Triggers and Actions as well as responses from the Xicato network.

### Triggers

#### Receive Response

A *Receive Response* Trigger must be added to the show file to be able to read the response. A Trigger must be created for each module instance (relating to an IP address and port) and will fire once it has received the HTTP/HTTPS response from the remote API.

### Actions

#### Make Request

The *Make Request* Action sends the HTTP/HTTPS request to the host specified in the instance properties. At least one *Make Request* Action must exist per module instance and a corresponding *Receive Request* Trigger must exist for that instance to successfully receive the reply.

If any of the below properties are not defined, the request will use the default value set in the instance property, on a per-property basis (if defined). If they are defined in the Action, then the value will override the default instance property's value.

See the instance property's placeholder for example syntax (the text is displayed when no user text is entered into the text field). Note that if the placeholder is showing, this counts as an empty string, not the string of the placeholder.

*Method* defines the request as a *GET*, *POST*, *PUT*, or *DELETE*. In most cases, this will be *GET* or *POST*.

Define any addition headers in the *Headers* as comma separated strings, using hyphens, equals sign, or colons. The module will split and send the name and values accordingly, for example "content-type=application" will be split into the header name, "content-type" and value, "application".

**Note: If you wish to use commas, equals signs or spaces as part of the header, they must be escaped with a backwards slash (before the character), otherwise they will be stripped out.**

Controllers use "content-type=application" by default so this is always send as one of the headers.

The *Path* specifies the request to the host and can be left blank if not required.

The *Data* specifies any additional information or body of the request and can be left blank if not required. This is in string format, commonly formatted as question-mark-equals format or an JSON array of key-value pairs.

#### Variables

##### Line by Line
* Variable 1: Response: (*a series of line-by-line strings*) <br>
##### Full Response/JSON
* Variable 1: *Always* the full response (*string*)
* Variable 2: "Timeline 1" (*string*: always the the identifier key's value if identifier is set)
* Variable 3: 1 (*integer* value for "num")
* Variable 4: "A" (*string* value for "group")
* Variable 5: 5000 (*integer* value for "position")
* Variable 6: "high"1 (*integer* value for "priority")

### Conditions

#### Get JSON Values

The *Make Request* Condition can be used to extract values from a JSON file. This Condition sits between a *Receive Response* Trigger and the Action that will use the JSON value/values. To be able to this, the *Read Type* in the instance properties must be set to *Full Response/JSON*. If a Condition exists and the property is not set to *Full Response/JSON*, an error will be logged and the Condition will not be met (the subsequent Action will not be executed). The full response string will always be Trigger variable number 1.

**Note:** This Condition is meant for simple, best-effort parsing of JSON values to use in Actions. It is not intended as a full JSON parser. It will only match keys and identifiers within a single JSON object (strings surrounded by {}) and parent and child object properties can not be matched together.

The *Value Keys* are a one-or-more, comma separated list of JSON keys (or properties) that you wish to return the values for. At least one *Value Key* but be specified, otherwise the Condition will return false. If these keys can be found in the JSON file, the values for these will be passed as Trigger variables in the order defined in *Value Keys*. If a key does not match a key in the JSON file, that key will be ignored but the Condition will not fail.

The *Identifier Key* is used for filtering. If the *Identifier Key* is found in the JSON file, then the Condition will return true and the values for the *Value Keys* will be passed as Trigger variables, with the *Identifier Key*'s value as variable number 2. If *Identifier Key* is left blank, then there is no filtering and all *Value Key* values will be passed as Trigger variables.

For an exact identifier match, if the *Identifier Value* is set and it matches the value of the found *Identifier Key*, the Condition will return true and pass all the above Trigger variables. If this field is blank, it will match any value of the *Identifier Key*.

Below is an example of a JSON file returned from a Controller when queried for a list of timelines using eg. *10.101.10.1/api/timeline*.

<div style="margin-left: 0px">
{
</div>
    <div style="margin-left: 10px">
    "timelines": [
    </div>
        <div style="margin-left: 20px">
        {
        </div>
            <div style="margin-left: 30px">
            "group": "A",<br>
            "length": 0,<br>
            "name": "Timeline 1",<br>
            "num": 1,<br>
            "onstage": false,<br>
            "position": 5000,<br>
            "priority": "high",<br>
            "state": "none",<br>
            </div>
        <div style="margin-left: 20px">
        },<br>
        {
        </div>
            <div style="margin-left: 30px">
            "group": "C",<br>
            "length": 0,<br>
            "name": "Timeline 2",<br>
            "num": 2,<br>
            "onstage": false,<br>
            "position": 0,<br>
            "priority": "normal",<br>
            "state": "none",
            </div>
        <div style="margin-left: 20px">
        }
        </div>
    <div style="margin-left: 10px">
    ]
    </div>
<div style="margin-left: 0px">
}
</div>

Below is the example used in the placeholder text of the Condition (the text is displayed when no user text is entered into the text field).

* *Value Keys*: num,group,position,priority
* *Identifier Key*: name
* *Identifier Value*: Timeline 1

In this example, the Trigger variables passed to the Action would be:

* Variable 1: Full response (Always variable 1 (*string*)
* Variable 2: "Timeline 1" (*string*: always the identifier key's value if identifier is set)
* Variable 3: 1 (*integer* value for "num")
* Variable 4: "A" (*string* value for "group")
* Variable 5: 5000 (*integer* value for "position")
* Variable 6: "high"1 (*integer* value for "priority")

**Note:** If a long query is returned, this may get cut off in the log but will be still be parsed in the module correctly.

### Support

If you encounter any issues with this module, please contact our support team.

[//]: # (#### Module Use Example)
[//]: # (If relevant to documentation give examples of module use)

[//]: # (#### Further Notes)
[//]: # (Possible location for further notes, may not be used)
