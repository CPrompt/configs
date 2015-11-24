#!/bin/bash
i3-msg "workspace 4; append_layout ~/.i3/workspace-4.json"
#fill the containers
(thunar "/home/curtis/" &)
(keepassx -lock &)
