#!/bin/bash

# start these programs
(thunar "/home/curtis/" &)
(keepassx &)

# send them to the scratchpad
i3-msg '[class="Thunar"] move window to scratchpad'
i3-msg '[class="Keepassx"] move window to scratchpad'
