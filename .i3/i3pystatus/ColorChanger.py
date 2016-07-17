#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 curtis <curtis@wayne-manor.gotham>
#
# Distributed under terms of the MIT license.

"""
Module to more easily change the colors of the i3pystatus moduels
Will have a themes folder where you will set specific colors to varialbes
The module will be called from the i3pystatus config by simply setting the theme
Much like a vim theme
"""

import json

theme_file = 'theme1.json'

with open(theme_file) as data_file:
    data = json.load(data_file)

    color1 = data["theme_information"]["color1"]
    color2 = data["theme_information"]["color2"]

    print(color1)
    print(color2)


