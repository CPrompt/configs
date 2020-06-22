from i3pystatus import Status
from i3pystatus import get_module
from i3pystatus.weather import weathercom
import logging
import subprocess

from colors import *

status = Status(
        logfile='/home/curtis/.config/i3/i3pystatus/i3pystatus.log',
        #logformat='%(asctime)s $(levelname)s:',
        standalone=True,
        )

status.register(
        'weather',
        format='{city}, NC  {icon}{condition}  {current_temp}{temp_unit}   Hi: {high_temp} Lo: {low_temp}',
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
            log_level=10,
            ),
        )


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


status.run()
