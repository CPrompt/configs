from i3pystatus import Status
from i3pystatus import get_module
#from i3pystatus.weather import wunderground
from i3pystatus.weather import weathercom
import logging
import subprocess

from colors import *

status = Status(
        logfile='/home/curtis/.config/i3/i3pystatus/logs/i3pystatus_monitor1.log',
        logformat='%(asctime)s $(levelname)s:',
        standalone=True,
        )

'''
status.register(
        'weather',
        format='{city}, NC  {icon}{condition}  {current_temp}{temp_unit}   Hi: {high_temp} Lo: {low_temp}',
        #format='{condition}  {current_temp}{temp_unit}   Hi: {high_temp} Lo: {low_temp}',
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
'''
'''
status.register(
        'weather',
        format='{condition}  {current_temp}{temp_unit}   Hi: {high_temp} Lo: {low_temp}',
        interval=900,
        colorize=True,
        hints={'markup': 'pango'},
        backend=weathercom.Weathercom(
            location_code='9bdb8423644be2c9fd8d98cc4a8518d5044f5bdef19504710b5c7dab4ee066da',
            units='imperial',
            update_error='<span color="#ff0000">!</span>',
            ),
        )
'''
'''
status.register(
        'weather',
        format='{condition} {current_temp}{temp_unit}[ {icon}][ Hi: {high_temp}][ Lo: {low_temp}][ {update_error}]',
        interval=9000,
        colorize=True,
        hints={'markup': 'pango'},
        backend=weathercom.Weathercom(
            location_code='USNC0314:1:US',
            units='imperial',
            update_error='<span color="#ff0000">!</span>',
            ),
        )
'''

'''
status.register(
    'weather',
    format='{condition} {current_temp}{temp_unit}[ {icon}][ Hi: {high_temp}][ Lo: {low_temp}][ {update_error}]',
    colorize=True,
    hints={'markup': 'pango'},
    backend=wunderground.Wunderground(
        location_code='KNCHIGHP109',
        units='imperial',
        update_error='<span color="#ff0000">!</span>',
    ),
)
'''
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
'''

# Displays clock like this:
status.register("clock",
                        #  Note: this config requires the gsimplecal package to be installed
                        hints = {"markup": "pango"},
                        format = " %a %d %b <span color=\"#ebdbb2\">  </span>  %H:%M:%S %P <span color=\"#ebdbb2\"> </span> ",
                        #    format = "(' %a %d %b ', America/New_York)",
                        #color = "#b16286",
                        #color = "#5f87af",
                        color = color_clock,
                        #on_leftclick = ["gsimplecal"],)
                        on_leftclick = ["orage"],)

status.register("moon",
                format = "{status} {moonicon}",
                color={
                    "New Moon":color_disk,
                    "Waxing Crescent":color_disk,
                    "First Quarter":color_disk,
                    "Waxing Gibbous":color_disk,
                    "Full Moon":color_disk,
                    "Waning Gibbous":color_disk,
                    "Last Quarter":color_disk,
                    "Waning Crescent":color_disk
                    }
                )


status.run()
