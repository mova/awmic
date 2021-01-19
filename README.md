## Simple microphone indicator for awesome wm

This widget shows
- a mask, if no app is listening to microphone
- a muted mic symbol, if an app is listening, but the app is muted.
- a mic if an app is recording should.
The widget also allows you to deafen/change the amplification for the currently listening apps by clicking/scrolling.
The settings for the actual mic remain unchanged by these actions.

Scroll to change the amplification for the apps, that are currently listening.
Click to toggle the input for these applications.

Requirements:
- pulsectl (`pip install pulsectl`)
- Any font with containing the fontawesome glyphs, default is FiraCode Nerd Font.

Clone this repository to `~/.config/awesome/awmic`.
Add this to theme:
```
local micwidget_builder = require("awmic")
micobj = micwidget_builder({font="FiraCode Nerd Font" .. " " .. 12})
```
Finally add `micobj.widget` to your list of widgets.

Feedback welcome.
