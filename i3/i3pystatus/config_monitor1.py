from i3pystatus import Status
from i3pystatus import get_module
from i3pystatus.weather import weathercom
from i3pystatus.weather import wunderground
import logging
import subprocess

from colors import *

status = Status(
        logfile='/home/curtis/.config/i3/i3pystatus/i3pystatus.log',
        #logformat='%(asctime)s $(levelname)s:',
        standalone=True,
        )

# Uses weather.com to get current temp

status.register(
        'weather',
        format='{city}    {condition}  {current_temp}{temp_unit}{icon}   Hi: {high_temp} Lo: {low_temp}',
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
            location_code='USNC0314:1:US',
            units='imperial',
        ),
)




#http://api.wunderground.com/api/0b012a21f26a3f71/conditions/q/NC/pws:KNCHIGHP24.json
'''
status.register(
            'weather',
            format='{city}    {condition}  {current_temp}{temp_unit}{icon}   Hi: {high_temp} Lo: {low_temp}',
            #format='{city} {condition} {current_temp}{temp_unit}{icon}  Hi: {high_temp} Lo: {low_temp}',
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
	        #location_code='NC/High-Point',
                units='imperial',
	        forecast='True',
	    ),
)
'''

status.register("pulseaudio",
        color_unmuted = pulse_audio,
        format = ' : {volume}',
        step = 1,
        log_level=10,
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
    log_level=10,
)


status.register("now_playing",
        on_leftclick=["player_command","PlayPause"],
        on_rightclick=["player_command","Stop"],
        on_middleclick=["player_prop","Shuffle",True],
        on_upscroll=["player_command","Seek",-10000000],
        on_downscroll=["player_command","Seek",+10000000],
        status = {
			'pause': '',
			'play': '',
			'stop': '',
		},
       format = '{song_elapsed}/{song_length} {artist} - {title}  {status}',
		format_no_player = 'Not running',    
       color = color_disk,
)


status.run()
