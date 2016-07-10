from i3pystatus import Status
from i3pystatus import get_module
from i3pystatus.weather import weathercom

import subprocess

color_teal = "#458588"

status = Status(standalone=True)


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

status.register("pulseaudio",
        color_unmuted = "#458588",
	format = ' : {volume}',)
'''
status.register("cmus",
    color = '#458588',
    #color = '#00ff00',
    color_not_running = '#ebdbb2',
    #color_not_running = '#ffffff',
    format = '{status} {song_elapsed}/{song_length} {artist} - {title}',
    format_not_running = 'Not running',
    interval = 1,
    )

status.register("now_playing",)
'''

status.register("mpd",
        #color = '#458588',
        color = color_teal,
	status = {"pause": "","play": "","stop": "",},
        format = '{status} {song_elapsed}/{len} {artist} - {title}',
        )

status.run()
