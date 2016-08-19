#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 curtis <curtis@wayne-manor.gotham>
#

from colors.color_changer import *

objColor = Colors()

# Theme file
objColor.read_json('gruvbox.json')

# Theme vars
# Shouldn't have to change these.  Just make sure they 
#	are declared correctly in your theme file
cmus_color = objColor.get_key_value('cmus_color')
cmus_not_running = objColor.get_key_value('cmus_not_running')
pulse_audio = objColor.get_key_value("pulse_audio")
color_clock = objColor.get_key_value("color_clock")
updates = objColor.get_key_value("updates")
color_no_updates= objColor.get_key_value("color_no_updates")
color_disk = objColor.get_key_value("color_disk")
color_online= objColor.get_key_value("color_online")
color_offline = objColor.get_key_value("color_offline")
color_network_up = objColor.get_key_value("color_network_up")
color_network_down = objColor.get_key_value("color_network_down")
