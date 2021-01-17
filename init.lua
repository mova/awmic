awful = require("awful")

local indicator = {}

function indicator:new(args)
    return setmetatable({}, {__index = self}):init(args)
end

function indicator:init(args)
    self.micscript= 'python3 ' .. awful.util.getdir("config") .. 'awmic/micControl.py'
    self.queryMic=self.micscript .. ' --query'
    self.raiseMic=self.micscript .. ' --raise'
    self.lowerMic=self.micscript .. ' --lower'
    self.toggleMic=self.micscript .. ' --toggle'

    self.widget = awful.widget.watch(self.queryMic, 1)

    self.widget.font=args.font or "FiraCode Nerd Font 12"

    self.widget:buttons(awful.util.table.join(
        awful.button({ }, 4, function() awful.spawn(self.raiseMic, false) end),
        awful.button({ }, 5, function() awful.spawn(self.lowerMic, false) end),
        awful.button({ }, 1, function() awful.spawn(self.toggleMic, false) end)
    ))

    return self
end


return setmetatable(indicator, {
    __call = indicator.new,
})
