from i3pystatus import Status
from i3pystatus import get_module
from i3pystatus.weather import weathercom

import subprocess

status = Status(standalone=True)

# Uses weather.com to get current temp

status.register("weather",
        format='{city} : Right Now: {condition} {current_temp}{temp_unit} {icon}   Hi: {high_temp} Lo: {low_temp}',
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
        ),
)

status.register("pulseaudio",
        color_unmuted = "#458588",
	format = ' : {volume}',)

status.register("cmus",
    color = '#458588',
    #color = '#00ff00',
    color_not_running = '#ebdbb2',
    #color_not_running = '#ffffff',
    format = '{status} {song_elapsed}/{song_length} {artist} - {title}',
    format_not_running = 'Not running',
    status = {
        'paused': '',
        'playing': '',
        'stopped': '',
    },
    interval = 1,
    )
'''
status.register("now_playing",)
'''
'''
status.register("mpd",
        #color = '#458588',
        color = '#458588',
	status = {"pause": "","play": "","stop": "",},
        format = '{status} {song_elapsed}/{len} {artist} - {title}',
        )
'''
status.run()
