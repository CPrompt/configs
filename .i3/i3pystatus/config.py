from i3pystatus import Status
from i3pystatus import get_module
import subprocess


status = Status(standalone=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
#  Note: this config requires the gsimplecal package to be installed
    hints = {"markup": "pango"},
    format = "<span color=\"#fff\"> :</span>%a %d %b <span color=\"#fff\">:</span>%H:%M:%S %P ",
    color = "#5f87af",
    on_leftclick = ["gsimplecal"],
    )

# Shows disk usage of /home/curtis/
status.register("disk",
		path="/home/curtis/",
		hints = {"markup": "pango"},
		format = "<span color=\"#fff\">:</span> {used}/{total}G [{avail}G]",
		color = "#afaf87",)
#status.register("moon",
#		format = "Moon Phase : {status}",
#		)


# /*******	Custom function to open firefox to weather.com  ********/
# on click, open firefox to weather.com with current detailed page
def open_weather():
	subprocess.call(['firefox','-url','www.weather.com/weather/today/l/27265:4:US'])

# Uses weather.com to get current temp
status.register("weather",
	location_code = "USNC0314:1:US",
	units = "imperial",
	colorize = "true",
	format = "{loc}:  {text}, {current_temp}",
	on_leftclick = open_weather,
	log_level=40,
	)

#status.register("weather_info",
#	location_code = "USNC0314:1:US",
#	format = "{current_temp}",
#       )


# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces

status.register("network",
    interface="enp2s0",
    hints = {"markup": "pango"},
    format_up="<span color=\"#fff\">:</span> {v4} ",
    color_up = "#fd971f",
    color_down = "red",
    )
'''
status.register("network",
    interface="enp2s0",
    hints = {"markup": "pango"},
    format_up="<span color=\"#00FF00\">{v4}</span>{bytes_recv:6.1f}KiB {bytes_sent:5.1f}KiB",
    format_down = "",
    dynamic_color = True,
    start_color = "#00FF00",
    end_color = "#FF0000",
    color_down = "#FF0000",
    upper_limit = 800.0,
    )
'''
status.register("pulseaudio",)
status.register("cmus",
	color = '#00ff00',
    color_not_running = '#ffffff',
    format = '{status} {song_elapsed}/{song_length} {artist} - {title}',
    format_not_running = 'Not running',
    interval = 1,
)
status.register("now_playing",)

status.run()
