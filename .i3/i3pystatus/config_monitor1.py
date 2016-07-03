from i3pystatus import Status
from i3pystatus import get_module
from i3pystatus.weather import weathercom

import subprocess


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
# font-awesome f028
	format = ' : {volume}',)


status.register("cmus",
	color = '#00ff00',
    color_not_running = '#ffffff',
    format = '{status} {song_elapsed}/{song_length} {artist} - {title}',
    format_not_running = 'Not running',
    interval = 1,
    )

#status.register("now_playing",)

status.run()
