## Simple microphone indicator for awesome wm

The icon  tells you that an app is listening AND the mic isn't muted ( otherwise: ).

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
