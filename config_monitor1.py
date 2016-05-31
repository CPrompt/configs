from i3pystatus import Status
from i3pystatus import get_module
from i3pystatus.weather import weathercom
from i3pystatus.updates import dnf
import subprocess


status = Status(standalone=True)

# Displays clock like this:
#status.register("clock",
#  Note: this config requires the gsimplecal package to be installed
#    hints = {"markup": "pango"},
#    format = " %a %d %b <span color=\"#fff\">  </span>  %H:%M:%S %P <span color=\"#fff\"> </span> ",
#    format = "(' %a %d %b ', America/New_York)",
#    color = "#5f87af",
#    on_leftclick = ["gsimplecal"],
#    )

# Display updates
'''
status.register("updates",
		format = "Updates: {count}",
		format_no_updates = "No Updates",
		backends = [dnf.Dnf],
		log_level = 10,
		)
'''

#status.register("updates",
#                        format = "Updates: {count}",
#                        color = "#00DD00",
#                        format_no_updates = "No updates",
#                        color_no_updates = "#FFFFFF",
#						format_working = None,
#						color_working = None,
#                        backends = [dnf.Dnf()],)


# Shows disk usage of /home/curtis/
#status.register("disk",
#		path="/home/curtis/",
#		hints = {"markup": "pango"},
#		format = "<span color=\"#fff\"> :</span> {used}/{total}G [{avail}G]",
#		color = "#afaf87",)


# Uses weather.com to get current temp

status.register("weather",
	format='{city} : {condition} {current_temp}{temp_unit} {icon} Lo: {low_temp}',
	colorize=True,
	interval = 1000,
	backend=weathercom.Weathercom(
		location_code="USNC0314:1:US",
        units='imperial',
        ),
)


# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces

#status.register("network",
#    interface="enp2s0",
#    hints = {"markup": "pango"},
#    format_up="<span color=\"#fff\"> :</span> {v4} ",
#    color_up = "#fd971f",
#    color_down = "red",
#    )

status.register("pulseaudio",
# font-awesome f028
	format = ' : {volume}',)


status.register("cmus",
	color = '#00ff00',
    color_not_running = '#ffffff',
    format = '{status} {song_elapsed}/{song_length} {artist} - {title}',
    format_not_running = 'Not running',
    interval = 1,
    )
status.register("now_playing",)

status.run()
