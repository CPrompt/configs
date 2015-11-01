from i3pystatus import Status

status = Status(standalone=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
    #format = [('%H:%M:%S  %m-%d-%Y','America/New_York'),('%X','Etc/GMT-5')],
    #format = [('%H:%M:%S %P  %m-%d-%Y','America/New_York'),('%X','Etc/GMT+4')],

    #format = [('%a %d %b %H:%M:%S %P'),('%X','US/Eastern')],
    #format="%H:%M:%S   %m-%d-%Y",


	# This is the good stuff
    #format = "%a %d %b  %H:%M:%S %P",
    #color = "#5f87af",)

    format = "%a %d %b  %H:%M:%S %P",
    color = "#5f87af",
    on_leftclick = ["gsimplecal"],
    )

# Shows disk usage of /home/curtis/
status.register("disk",
		path="/home/curtis/",
		format = "{used}/{total}G [{avail}G]",
		color = "#afaf87",)



# Uses weather.com to get current temp
status.register("weather",
	location_code = "USNC0314:1:US",
	units = "imperial",
	colorize = "true",
	format = "{current_temp}",)



# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
status.register("network",
    interface="enp2s0",
    format_up="{v4}",
    color_up = "#fd971f",
    color_down = "red",
    )


status.register("pulseaudio",)
status.register("cmus",)


status.run()
