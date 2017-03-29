from i3pystatus import Status
from i3pystatus import get_module
from i3pystatus.weather import weathercom
from i3pystatus.updates import dnf
import subprocess


from colors import *

status = Status(standalone=True)

# Displays clock like this:
status.register("clock",
                        #  Note: this config requires the gsimplecal package to be installed
                        hints = {"markup": "pango"},
                        format = " %a %d %b <span color=\"#ebdbb2\">  </span>  %H:%M:%S %P <span color=\"#ebdbb2\"> </span> ",
                        #    format = "(' %a %d %b ', America/New_York)",
                        #color = "#b16286",
                        #color = "#5f87af",
                        color = color_clock,
                        on_leftclick = ["gsimplecal"],)



# Display updates

status.register("updates",
                        format = "Updates: {count}",
                        #color = "#689d6a",
                        #color_no_updates = "#ebdbb2",
                        color = updates,
                        color_no_updates = color_no_updates,
                        color_working = None,
                        format_no_updates = "No updates",
                        format_working = "Working...",
                        notification_icon = "software-update-available",
                        backends = [dnf.Dnf()],)

# Uses weather.com to get current temp

status.register("weather",
        #format='{city} : Right Now: {condition} {current_temp}{temp_unit} {icon}   Hi: {high_temp} Lo: {low_temp}',
        format='{city}: Right Now: {condition} {current_temp}{temp_unit}{icon} Hi: {high_temp} Lo: {low_temp}',
	colorize=True,
        color_icons = {
            'Fair': (u'\u263c', '#ffcc00'),
            'Cloudy': (u'\u2601', '#f8f8ff'),
            'Partly Cloudy': (u'\u2601', '#f8f8ff'),  # \u26c5 is not in many fonts
            'Rainy': (u'\u26c8', '#cbd2c0'),
            'Thunderstorm': (u'\u03de', '#cbd2c0'),
            'Sunny': (u'\u2600', '#ffff00'),
            'Snow': (u'\u2603', '#ffffff'),
            'default': ('', None),
        },
	interval = 1000,
	backend=weathercom.Weathercom(
            location_code="USNC0314:1:US",
            units='imperial',
            update_error='<span color="#ff0000">|</span>',
        ),
)

# http://api.wunderground.com/api/0b012a21f26a3f71/conditions/q/NC/pws:KNCHIGHP24.json
'''
status.register(
            'weather',
            format='{city} Right Now: {condition} {current_temp}{temp_unit}{icon}  Hi: {high_temp} Lo: {low_temp}',
            colorize=True,
            color_icons = {
				'Fair': (u'\u263c', '#ffcc00'),
				'Cloudy': (u'\u2601', '#f8f8ff'),
				'Partly Cloudy': (u'\u2601', '#f8f8ff'),  # \u26c5 is not in many fonts
				'Rainy': (u'\u26c8', '#cbd2c0'),
				'Thunderstorm': (u'\u03de', '#cbd2c0'),
				'Sunny': (u'\u2600', '#ffff00'),
				'Snow': (u'\u2603', '#ffffff'),
				'default': ('', None),
			},
            backend=wunderground.Wunderground(
                api_key='0b012a21f26a3f71',
                location_code='pws:KNCHIGHP24',
				units='imperial',
				forecast='True',
	),
)
'''

# Shows disk usage of /home/curtis/
status.register("disk",
                        path="/home/curtis/",
                        hints = {"markup": "pango"},
                        format = "<span color=\"#ebdbb2\"> :</span> {used}/{total}G [{avail}G]",
                        #color = "#d79921",)
                        #color = "#afaf87",)
                        color = color_disk,)



# Shows internet connection status
status.register("online",
                        format_online = '',
                        #color = '#98971a',
                        #color = '#00DD00',
                        color = color_online,
                        format_offline = '',
                        #color_offline = '#FF0000',)
                        color_offline = color_offline,)


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
                        format_up="<span color=\"#ebdbb2\"> :</span> {v4} ",
                        #color_up = "#98971a",
                        #color_up = "#fd971f",
                        #color_down = "red",)
                        color_up = color_network_up,
                        color_down = color_network_down,)




status.register("pulseaudio",
        color_unmuted = pulse_audio,
	format = ' : {volume}',
        )


status.register("cmus",
    color = cmus_color,
    color_not_running = cmus_not_running,
    format = '{status} {song_elapsed}/{song_length} {artist} - {title}',
    format_not_running = 'Not running',
    status = {
        'paused': '',
        'playing': '',
        'stopped': '',
    },
    interval = 1,
)

status.run()
