#!/bin/bash
i3-msg "workspace 1; append_layout ~/.i3/workspace-1.json"
#fill the containers
(Firefox &)
(urxvt256c &)
(Thunderbird &)
