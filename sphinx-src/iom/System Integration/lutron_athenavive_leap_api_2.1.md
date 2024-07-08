# Lutron Athena/Vive (LEAP API) - Version 2.1.0


<h2>Module Summary</h2>
<p>Integrates with Lutron<span class="athena"> Athena,</span><span class="vive"> Vive,</span> using Lutron Extensible Application Protocol (LEAP).</p>
<p><strong>Note:</strong> Due to the security requirements of LEAP, the controller must be associated with the Lutron Ethernet bridge before use.<br>
Please refer to the <em>Associate</em> action documentation below.</br></p>
<h2>Module Status</h2>
<p>This IO Module is stable and has been tested internally.</p>
<p>If you encounter any issues with this module, or have any feedback regarding its operation, please contact our support team.</p>
<h3>Module Scope</h3>



<h3>Release Notes</h3>
<h4>Version 2.1</h4>
<ul>
<li class="vive">Support for Vive hubs</li>
<li>Updated triggers:
        <ul>
<li><i>Area: Status</i>
<ul>
<li>New property and return variable<i>Occupied</i>.</li>
</ul>
</li>
<li><i>Zone: Status</i>
<ul>
<li><i>Switched Level</i> renamed to <i>Non-dimmed level</i> to support reporting CCO and Receptacle control types.</li>
<li class="athena">Added <i>Vibrancy</i> and Spectrum variables</li>
</ul>
</li>
</ul>
</li>
<li>New actions:
        <ul>
<li><i>Zone: Goto level (CCO)</i></li>
<li><i>Zone: Goto level (Receptacle)</i></li>
<li class="athena"><i>Zone: Goto level (Spectrum Tuning - HSV)</i></li>
<li class="athena"><i>Zone: Goto level (Spectrum Tuning - CCT)</i></li>
<li class="athena"><i>Zone: Goto level (Spectrum Tuning - xy)</i></li>
<li class="athena"><i>Zone: Goto level (White Tuning)</i></li>
</ul>
</li>
<li>Added support for Unicode</li>
<li>Improved support for large LEAP responses</li>
</ul>
<h4>Version 2.0</h4>
<ul>
<li>Initial release.</li>
</ul>
<p><em>Minor point releases (eg. 1.1.x) will be for small fixes and may not be listed here.</em></p>
<h2>Operation</h2>
<h3>Instance Properties</h3>
<p>Checking the <em>Auto reconnect</em> checkbox will instruct the module to automatically reconnect to the Ethernet bridge in the event of an unexpected disconnection.</p>
<p>Checking the <em>Extended Logging</em> checkbox will provide more detailed log messages.\</p>

This is intended for diagnostics and problem solving and should ideally be disabled during normal operation.
<p><em>Ethernet bridge serial</em> is used by the trigger <em>Discovered</em>.</p>
<h4>Status Variables</h4>
<p>The IO Modules tab of the web interface provides status variables to shows information about the module and monitor its state.</p>
<table>
<style type="text/css">
    td {
        padding: 3 10px;
    }
    </style>
<tbody>
<tr class="separator"></tr>
<tr>
<td>Connection status</td>
<td>Current bridge connection status.
            <ul style="margin-top:0px;">
<li><i>'Access Denied'</i></li>
<li><i>'Associating'</i></li>
<li><i>'Connected'</i></li>
<li><i>'Connecting'</i></li>
<li><i>'Disconnected'</i></li>
</ul>
</td>
</tr>
<tr>
<td>Project name</td>
<td>Name of the currently loaded project on the ethernet bridge</td>
</tr>
<tr>
<td>Project type</td>
<td>Type project currently loaded project on the ethernet bridge</td>
</tr>
<tr>
<td>Project modified</td>
<td>Timestamp of the last modification to the currently loaded project on the ethernet bridge</td>
</tr>
<tr>
<td>Bridge IP address</td>
<td>IP Address of the currently connected/last connected LEAP bridge</td>
</tr>
<tr>
<td>Last socket error</td>
<td>Full details on the last communication error, if any</td>
</tr>
<tr class="separator"></tr>
</tbody>
</table>
<h3>Triggers</h3>
<h4>Access denied</h4>
<p>Fires when the Controller is denied access to the LEAP Ethernet bridge.<br/>
This can occur if the Controller hasn't yet been associated with the current LEAP Ethernet bridge.</p>
<h4>Connected</h4>
<p>Fires when the Controller connects to the LEAP Ethernet bridge.</p>
<h4>Disconnected</h4>
<p>Fires when the Controller disconnects from the LEAP Ethernet bridge.</p>
<h4>Discovered</h4>
<p>Fires when the Controller discovers a LEAP Ethernet bridge.</p>
<p>Matching instance properties:</p>
<ul>
<li><i>Ethernet bridge serial</i> Matching bridge serial number, or any if empty.</li>
</ul>
<p>Trigger variables:</p>
<ol>
<li>Name (<em>string</em>).</li>
<li>IP Address (<em>IP Address</em>).</li>
<li>Serial Number (<em>string</em>).</li>
</ol>
<h4>Area: Updated root</h4>
<p>Fires when the root area is updated.</p>
<p>Trigger variables:</p>
<ol>
<li>Area number (<em>integer</em>).</li>
<li>Name (<em>string</em>).</li>
</ol>
<h4>Area: New</h4>
<p>Fires when an area is discovered.</p>
<p>Matching properties:</p>
<ul>
<li><i>Number</i> Matching area number, or 'any'.</li>
<li><i>Name</i> Matching area name, or any if empty.</li>
</ul>
<p>Trigger variables:</p>
<ol>
<li>Area number (<em>integer</em>).</li>
<li>Name (<em>string</em>).</li>
<li>Parent or -1 if no parent (<em>integer</em>).</li>
</ol>
<h4>Area: Updated</h4>
<p>Fires when an area is updated.</p>
<p>Matching properties:</p>
<ul>
<li><i>Number</i> Matching area number, or 'any'.</li>
<li><i>Name</i> Matching area name, or any if empty.</li>
</ul>
<p>Trigger variables:</p>
<ol>
<li>Area number (<em>integer</em>).</li>
<li>Name (<em>string</em>).</li>
<li>Parent or -1 if no parent (<em>integer</em>).</li>
</ol>
<h4>Area: Status</h4>
<p>Fires when an area changes status.</p>
<p>Matching properties:</p>
<ul>
<li><i>Number</i>: Matching area number, or 'any'.</li>
<li><i>Name</i>: Matching area name, or any if empty.</li>
<div class="athena"> <b><i>Athena only</i></b>
<li><i>Scene</i>: Matching scene number, or 'any'.</li>
<li><i>Scene name</i>: Matching scene, or 'any'.</li>
</div>
<li><i>Occupied</i>: Matching occupancy state name, or 'any'.</li>
<div class="vive"> <b><i>Vive only</i></b>
<li><i>Power is</i>: Power matching condition operator.</li>
<li><i>Power</i>: Matching area power, or 'any'.</li>
</div>
</ul>
<p>Trigger variables:</p>
<ol>
<li>Area number (<i>integer</i>).</li>
<li>Name (<i>string</i>).</li>
<div class="athena"> <b><i>Athena only</i></b>
<li>Current scene number or -1 if no scene (<i>integer</i>).</li>
<li>Current scene name (<i>string</i>).</li>
<li>Current occupancy state (<i>boolean</i>).</li>
</div>
<div class="vive"> <b><i>Vive only</i></b>
<li>Current occupancy state (<i>boolean</i>).</li>
<li>Total power, in Watts, used by all the devices in the area (<i>integer</i>).</li>
</div>
</ol>
<h4>Event: New</h4>
<p>Fires when an event is discovered.</p>
<p>Matching properties:</p>
<ul>
<li><i>Number</i> Matching event number, or 'any'.</li>
<li><i>Name</i> Matching event name, or any if empty.</li>
</ul>
<p>Trigger variables:</p>
<ol>
<li>Event number (<em>integer</em>).</li>
<li>Name (<em>string</em>).</li>
<li>Parent or -1 if no parent (<em>integer</em>).</li>
</ol>
<h4>Event: Updated</h4>
<p>Fires when an event is updated.</p>
<p>Matching properties:</p>
<ul>
<li><i>Number</i> Matching event number, or 'any'.</li>
<li><i>Name</i> Matching event name, or any if empty.</li>
</ul>
<p>Trigger variables:</p>
<ol>
<li>Event number (<em>integer</em>).</li>
<li>Event Name (<em>string</em>).</li>
<li>Parent Timeclock number (<em>integer</em>).</li>
<li>Parent Timeclock name (<em>string</em>).</li>
<li>The Hour at which the event will occur, 0-23. If it is an astronomical event, this is calculated based on controller location (<em>integer</em>).</li>
<li>The Minute at which the event will occur, 0-59 (<em>integer</em>).</li>
<li>The schedule type of the event, either <code>ByDate</code> for events that occur on a specific date, or <code>DayOfWeek</code> for events that occur based on day of week (<em>string</em>).</li>
<li>The timeclock type of the event, either <code>FixedTime</code> for events occurring at a fixed time or <code>Astromomic</code> for astronomic events (<em>string</em>).</li>
<li>For DayOfWeek events, a table of days (Sunday through Saturday) with boolean values for each day. For ByDate events, a date in YYYY/MM/DD format when the events occur - comma separated for multiple dates (<em>string</em>).</li>
<li>Is the event is enabled (<em>boolean</em>).</li>
<li>Sunrise or Sunset for astronomic events - empty for non-astronomic events (<em>string</em>).</li>
<li>The offset from Sunrise/Sunset for an astronomic event - a floating point number of hours the event is offset from sunrise/sunset; or 0 for non-Astronomic events (<em>number</em>).</li>
</ol>
<h4>Event: Status</h4>
<p>Fires when an event changes status.</p>
<p>Matching properties:</p>
<ul>
<li><i>Number</i> Matching event number, or 'any'.</li>
<li><i>Name</i> Matching event name, or any if empty.</li>
<li><i>Enabled</i> Enabled status, or 'any'.</li>
</ul>
<p>Trigger variables:</p>
<ol>
<li>Event number (<em>integer</em>).</li>
<li>Name (<em>string</em>).</li>
<li>Enabled status (<em>boolean</em>).</li>
</ol>
<div class="athena">
<h4>Scene: New <b><i>(Athena only)</i></b></h4>
<p>Fires when a scene is discovered.</p>
<p>Matching properties:</p>
<ul>
<li><i>Number</i> Matching scene number, or 'any'.</li>
<li><i>Name</i> Matching area name, or any if empty.</li>
<li><i>Area</i> Matching area number, or 'any'.</li>
<li><i>Preset</i> Matching preset number, or 'any'.</li>
</ul>
<p>Trigger variables:</p>
<ol>
<li>Scene number (<em>integer</em>).</li>
<li>Name (<em>string</em>).</li>
<li>Area (<em>integer</em>).</li>
<li>Preset (<em>integer</em>).</li>
</ol>
</div>
<div class="athena">
<h4>Scene: Updated <b><i>(Athena only)</i></b></h4>
<p>Fires when a scene is updated.</p>
<p>Matching properties:</p>
<ul>
<li><i>Number</i> Matching scene number, or 'any'.</li>
<li><i>Name</i> Matching area name, or any if empty.</li>
<li><i>Area</i> Matching area number, or 'any'.</li>
<li><i>Preset</i> Matching preset number, or 'any'.</li>
</ul>
<p>Trigger variables:</p>
<ol>
<li>Scene number (<em>integer</em>).</li>
<li>Name (<em>string</em>).</li>
<li>Area (<em>integer</em>).</li>
<li>Preset (<em>integer</em>).</li>
</ol>
</div>
<h4>Timeclock: New</h4>
<p>Fires when an timeclock is discovered.</p>
<p>Matching properties:</p>
<li><i>Number</i> Matching timeclock number, or 'any'.</li>
<li><i>Name</i> Matching timeclock name, or any if empty.</li>
<p>Trigger variables:</p>
<ol>
<li>Timeclock number (<em>integer</em>).</li>
<li>Name (<em>string</em>).</li>
</ol>
<h4>Timeclock: Updated</h4>
<p>Fires when an timeclock is updated.</p>
<p>Matching properties:</p>
<ul>
<li><i>Number</i> Matching timeclock number, or 'any'.</li>
<li><i>Name</i> Matching timeclock name, or any if empty.</li>
</ul>
<p>Trigger variables:</p>
<ol>
<li>Timeclock number (<em>integer</em>).</li>
<li>Name (<em>string</em>).</li>
</ol>
<h4>Timeclock: Status</h4>
<p>Fires when an Timeclock changes status.</p>
<p>Matching properties:</p>
<ul>
<li><i>Number</i> Matching timeclock number, or 'any'.</li>
<li><i>Name</i> Matching timeclock name, or any if empty.</li>
<li><i>Enabled</i> Enabled status, or 'any'.</li>
</ul>
<p>Trigger variables:</p>
<ol>
<li>timeclock number (<em>integer</em>).</li>
<li>Name (<em>string</em>).</li>
<li>Enabled status (<em>boolean</em>).</li>
</ol>
<h4>Zone: New</h4>
<p>Fires when an zone is discovered.</p>
<p>Matching properties:</p>
<ul>
<li><i>Number</i> Matching zone number, or 'any'.</li>
<li><i>Name</i> Matching zone name, or any if empty.</li>
<li><i>Type</i> Matching zone type, or 'any'.</li>
<li><i>Area</i> Matching area number, or 'any'.</li>
</ul>
<p>Trigger variables:</p>
<ol>
<li>Zone number (<em>integer</em>).</li>
<li>Name (<em>string</em>).</li>
<li>Type (<em>string</em>).</li>
<li>Area or -1 if no area (<em>integer</em>).</li>
</ol>
<h4>Zone: Updated</h4>
<p>Fires when an zone is updated.</p>
<p>Matching properties:</p>
<ul>
<li><i>Number</i> Matching zone number, or 'any'.</li>
<li><i>Name</i> Matching zone name, or any if empty.</li>
<li><i>Type</i> Matching zone type, or 'any'.</li>
<li><i>Area</i> Matching area number, or 'any'.</li>
</ul>
<p>Trigger variables:</p>
<ol>
<li>Zone number (<em>integer</em>).</li>
<li>Name (<em>string</em>).</li>
<li>Type (<em>string</em>).</li>
<li>Area or -1 if no area (<em>integer</em>).</li>
</ol>
<h4>Zone: Status</h4>
<p>Fires when an zone changes status.</p>
<p>Matching properties:</p>
<ul>
<li><i>Number</i> Matching zone number, or 'any'.</li>
<li><i>Name</i> Matching zone name, or any if empty.</li>
<li><i>Type</i> Matching zone type, or 'any'.</li>
<li><i>Area</i> Matching area number, or 'any'.</li>
<li><i>Level is</i> Level matching condition operator.</li>
<li><i>Level</i> Matching level, or 'any'.</li>
<li><i>Non-dimmed level</i> Matching non-dimmed level, or 'any'.</li>
</ul>
<p>Trigger variables:</p>
<ol>
<li>Zone number (<i>integer</i>).</li>
<li>Name (<i>string</i>).</li>
<li>Type (<i>string</i>).</li>
<li>Area or -1 if no area (<i>integer</i>).</li>
<li>Level (percent) or -1 if no level (<i>integer</i>).</li>
<li>Non-dimmed level ('On', 'Off', 'Open, or 'Closed') or '' if no Non-dimmed level (<i>string</i>).</li>
<div class="athena"> <b><i>Athena only</i></b>
<li>Vibrancy (percent) or -1 if no vibrancy (<i>integer</i>).</li>
<li>Hue (degrees) or -1 if no hue (<i>number</i>).</li>
<li>Saturation (percent) or -1 if no saturation (<i>integer</i>).</li>
<li>CCT (kelvin) or -1 if no CCT (<i>number</i>).</li>
<li>CIE x (0-1) or -1 if no vibrancy (<i>number</i>).</li>
<li>CIE y (0-1) or -1 if no vibrancy (<i>number</i>).</li>
</div>
</ol>
<h3>Conditions</h3>
<h4>Connected</h4>
<p>Matches if the controller is currently connected to a bridge.</p>
<div class="athena">
<h4>Area: Scene <b><i>(Athena only)</i></b></h4>
<p>Matches if the active scene (stored in variable <em>Scene (Variable #)</em>) number in the area (stored in variable <em>Number (Variable #)</em>) matches.
If both <em>Number (Variable #)</em> and <em>Scene (Variable #)</em> are 'any', then a Lua table of active scenes is returned.</p>
<p>Condition properties:</p>
<ul>
<li><i>Number (Variable #)</i> Variable number containing matching area number, or 'any'.</li>
<li><i>Scene (Variable #)</i> Variable number containing matching scene number, or 'any'.</li>
</ul>
<p>Condition variables:</p>
<ol>
<li>Area number (<em>integer</em>).</li>
<li>Scene number or -1 if no scene (<em>integer</em>).<br/>
OR</li>
<li>Table of active scenes, indexed by area number (<em>string</em>).<pre><code>--- Example table usage
local areaScenes = load("return " .. get_trigger_variable(1).string)()
for area, scene in pairs(areaScenes) do
    log(table.concat({'Area', area, 'scene is', tostring(scene)}, ' '))
end
</code></pre>
</li>
</ol>
</div>
<h4>Event: Enabled</h4>
<p>Matches if the event (stored in variable <em>Number (Variable #)</em>) matches the <em>Enabled</em> property.
If <em>Number (Variable #)</em> is 'any', then a Lua table of matching event state is returned.</p>
<p>Condition properties:</p>
<ul>
<li><i>Number (Variable #)</i> Variable number containing matching event number, or 'any'.</li>
<li><i>Enabled</i> Matching enabled state, or 'any'.</li>
</ul>
<p>Condition variables:</p>
<ol>
<li>Event number (<em>integer</em>).</li>
<li>Enabled status (<em>boolean</em>).<br/>
OR</li>
<li>Table of event states, indexed by event number (<em>string</em>).<pre><code>--- Example table usage
local eventStates = load("return " .. get_trigger_variable(1).string)()
for event, state in pairs(eventStates) do
    log(table.concat({'Event', event, 'is', tostring(state)}, ' '))
end
</code></pre>
</li>
</ol>
<h4>Event: Scheduled</h4>
<p>Matches if the event (stored in variable <em>Number (Variable #)</em>) schedule matches the Year (stored in variable <em>Year (Variable #)</em>),
Month (stored in variable <em>Month (Variable #)</em>), and Day (stored in variable <em>Day (Variable #)</em>) properties.
If <em>Number (Variable #)</em> is 'any', then a Lua table of matching events is returned.
If <em>Year (Variable #)</em>, or <em>Month (Variable #)</em>, or <em>Day (Variable #)</em> are 'now' then the current Year, and/or Month, and/or Day; are utilised.</p>
<p>Condition properties:</p>
<ul>
<li><i>Number(Variable #)</i> Variable number containing matching event number, or 'any'.</li>
<li><i>Year (Variable #)</i> Variable number containing matching schedule year, or 'now'.</li>
<li><i>Month (Variable #)</i> Variable number containing matching schedule year, or 'now'.</li>
<li><i>Day (Variable #)</i> Variable number containing matching schedule year, or 'now'.</li>
</ul>
<p>Condition variables:</p>
<ol>
<li>Event number (<em>integer</em>).</li>
<li>Scheduled hour (<em>integer</em>).</li>
<li>Scheduled minute (<em>integer</em>).<br/>
OR</li>
<li>Table of event times, indexed by event number (<em>string</em>).<pre><code>--- Example table usage
local eventTimes = load("return " .. get_trigger_variable(1).string)()
for event, time in pairs(eventTimes) do
    log(table.concat({'Event', event, 'scheduled at', time.hour .. ':' .. time.minute}, ' '))
end
</code></pre>
</li>
</ol>
<h4>Timeclock: Enabled</h4>
<p>Matches if the timeclock (stored in variable <em>Number (Variable #)</em>) matches the <em>Enabled</em> property.
If <em>Number (Variable #)</em> is 'any', then a Lua table of matching timeclock state is returned.</p>
<p>Condition properties:</p>
<ul>
<li><i>Number (Variable #)</i> Variable number containing matching timeclock number, or 'any'.</li>
<li><i>Enabled</i> Matching enabled state, or 'any'.</li>
</ul>
<p>Condition variables:</p>
<ol>
<li>Timeclock number (<em>integer</em>).</li>
<li>Enabled status (<em>boolean</em>).<br/>
OR</li>
<li>Table of timeclock states, indexed by event number (<em>string</em>).<pre><code>--- Example table usage
local timeclockStates = load("return " .. get_trigger_variable(1).string)()
for timeclock, state in pairs(timeclockStates) do
    log(table.concat({'Timeclock', timeclock, 'is', tostring(state)}, ' '))
end
</code></pre>
</li>
</ol>
<h4>Zone: Level</h4>
<p>Matches if the zone (stored in variable <em>Number (Variable #)</em>) matches the zone's level using the <em>Level is</em> and <em>Level</em> properties.
If both (stored in variable <em>Number (Variable #)</em>) is 'any', then a Lua table of current matching levels is returned.</p>
<p>Condition properties:</p>
<ul>
<li><i>Number (Variable #)</i> Variable number containing matching zone number, or 'any'.</li>
<li><i>Level is</i> Level matching condition operator.</li>
<li><i>Level</i> Matching level, or 'any'.</li>
</ul>
<p>Condition variables:</p>
<ol>
<li>Zone number (<em>integer</em>).</li>
<li>Level (percent) or -1 if no level (<em>integer</em>).<br/>
OR</li>
<li>Table of zone levels, indexed by zone number (<em>string</em>).<pre><code>--- Example table usage
local zoneLevels = load("return " .. get_trigger_variable(1).string)()
for zone, level in pairs(zoneLevels) do
    log(table.concat({'Zone', zone, 'is at', tostring(level)}, ' '))
end
</code></pre>
</li>
</ol>
<h3>Actions</h3>
<h4>Associate</h4>
<p><strong>This process needs to be performed at least once during the initial commissioning process.</strong></p>
<p>Start an association process with ethernet bridge at <em>IP Address</em>.</p>
<div class="athena"><b>Athena - </b>After firing this action you will need to tap the button on the ethernet bridge.</div>
<div class="vive"><b>Vive - </b>The, time limited, one-time password generated Lutron Vive app should be entered in *Password*.</div>
Please refer to the controllers logs for results of the association.
<p><em>n.b. The association objects are stored on the controllers local SD card, they are <strong>not</strong> stored in the project file.</em>
<em>If the SD card or ethernet bridge is replaced, the association will need to be re-undertaken</em></p>
<h4>Connect</h4>
<p>Start connection to ethernet bridge at <em>IP Address</em>.</p>
<h4>Disconnect</h4>
<p>Disconnect from any connected (or connecting) ethernet bridge.</p>
<h4>Discover</h4>
<p>Run bridge discovery on the network, each discovered bridges will be reported by the trigger <em>Discovered ethernet bridge</em>.</p>
<p><strong>Note:</strong> The controller must have a default gateway set to a value other than 0.0.0.0.<br/>
If network is 'flat', and has no requirement for a default gateway/router, then the default gateway should be set to the controller's own IP.*</p>
<div class="athena">
<h4>Area: Goto scene <b><i>(Athena only)</i></b></h4>
<p>Sets an <em>Area</em> to a <em>Scene</em>.
The scene must exist in the area</p>
<p>Properties:</p>
<ul>
<li><i>Area</i> Area number.</li>
<li><i>Scene</i> Scene number.</li>
</ul>
</div>
<h4>Event: Set state</h4>
<p>Sets an <em>Event</em> state to either enabled or disabled.</p>
<p>Properties:</p>
<ul>
<li><i>Event</i> Event number.</li>
<li><i>Enabled</i> Enabled yes/no.</li>
</ul>
<h4>Zone: Goto level (Dimmed)</h4>
<p>Set a zone with the type 'Dimmed' to <em>Level</em> over <em>Fade</em> seconds after waiting <em>Delay</em> seconds.</p>
<p>Properties:</p>
<ul>
<li><i>Zone</i> Zone number.</li>
<li><i>Level</i> Level (percent).</li>
<li><i>Fade</i> Fade time (seconds).</li>
<li><i>Delay</i> Delay time (seconds).</li>
</ul>
<h4>Zone: Goto level (Switched)</h4>
<p>Set a zone with the type 'Switched' to <em>Level</em> after waiting <em>Delay</em> seconds.</p>
<p>Properties:</p>
<ul>
<li><i>Zone</i> Zone number.</li>
<li><i>Level</i> Level (On/Off).</li>
<li><i>Delay</i> Delay time (seconds).</li>
</ul>
<h4>Zone: Goto level (CCO)</h4>
<p>Set a zone with the type 'CCO' to <em>Level</em> after waiting <em>Delay</em> seconds.</p>
<p>Properties:</p>
<ul>
<li><i>Zone</i> Zone number.</li>
<li><i>Level</i> Level (Open/Closed).</li>
<li><i>Delay</i> Delay time (seconds).</li>
</ul>
<h4>Zone: Goto level (Receptacle)</h4>
<p>Set a zone with the type 'Receptacle' to <em>Level</em> after waiting <em>Delay</em> seconds.</p>
<p>Properties:</p>
<ul>
<li><i>Zone</i> Zone number.</li>
<li><i>Level</i> Level (On/Off).</li>
<li><i>Delay</i> Delay time (seconds).</li>
</ul>
<div class="athena">
<h4>Zone: Goto level (Spectrum Tuning - HSV) <b><i>(Athena only)</i></b></h4>
<p>Set a zone with the type 'SpectrumTuning' to <em>Level</em>, with a spectrum of <em>Hue</em> and <em>Saturation</em>, over <em>Fade</em> seconds after waiting <em>Delay</em> seconds.</p>
<p>Properties:</p>
<ul>
<li><i>Zone</i>: Zone number.</li>
<li><i>Level</i>: Level (percent).</li>
<li><i>Vibrancy</i>: Ratio of white LED vs RGB LEDs (percent).</li>
<li><i>Hue</i>: Spectrum hue (degrees).</li>
<li><i>Saturation</i>: Spectrum saturation (percent).</li>
<li><i>Fade</i>: Fade time (seconds).</li>
<li><i>Delay</i>: Delay time (seconds).</li>
</ul>
</div>
<div class="athena">
<h4>Zone: Goto level (Spectrum Tuning - CCT) <b><i>(Athena only)</i></b></h4>
<p>Set a zone with the type 'SpectrumTuning' to <em>Level</em>, with a spectrum of <em>CCT</em>, over <em>Fade</em> seconds after waiting <em>Delay</em> seconds.</p>
<p>Properties:</p>
<ul>
<li><i>Zone</i>: Zone number.</li>
<li><i>Level</i>: Level (percent).</li>
<li><i>Vibrancy</i>: Ratio of white LED vs RGB LEDs (percent).</li>
<li><i>CCT</i>: Colour temperature (1000 k - 25000 k).</li>
<li><i>Fade</i>: Fade time (seconds).</li>
<li><i>Delay</i>: Delay time (seconds).</li>
</ul>
</div>
<div class="athena">
<h4>Zone: Goto level (Spectrum Tuning - xy) <b><i>(Athena only)</i></b></h4>
<p>Set a zone with the type 'SpectrumTuning' to <em>Level</em>, with a spectrum of <em>x</em>/<em>y</em>, over <em>Fade</em> seconds after waiting <em>Delay</em> seconds.</p>
<p>Properties:</p>
<ul>
<li><i>Zone</i>: Zone number.</li>
<li><i>Level</i>: Level (percent).</li>
<li><i>Vibrancy</i>: Ratio of white LED vs RGB LEDs (percent).</li>
<li><i>x</i>: CIE 1931 x colour point (0-1).</li>
<li><i>y</i>: CIE 1931 y colour point (0-1).</li>
<li><i>Fade</i>: Fade time (seconds).</li>
<li><i>Delay</i>: Delay time (seconds).</li>
</ul>
</div>
<div class="athena">
<h4>Zone: Goto level (White Tuning) <b><i>(Athena only)</i></b></h4>
<p>Set a zone with the type 'WhiteTuning' to <em>Level</em>, with a spectrum of <em>CCT</em>, over <em>Fade</em> seconds after waiting <em>Delay</em> seconds.</p>
<p>Properties:</p>
<ul>
<li><i>Zone</i>: Zone number.</li>
<li><i>Level</i>: Level (percent).</li>
<li><i>CCT</i>: Colour temperature (1000 k - 25000 k).</li>
<li><i>Fade</i>: Fade time (seconds).</li>
<li><i>Delay</i>: Delay time (seconds).</li>
</ul>
</div>
<h2>Support</h2>
<p>If you encounter any issues with this module, please contact our support team.</p>
<h2>Licences</h2>
<p>This module uses the following third party code/modules:</p>
<h3>dkjson</h3>
Copyright (C) 2010-2024 David Heiko Kolf
<p>Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:</p>
<p>The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.</p>
<p>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.</p>
