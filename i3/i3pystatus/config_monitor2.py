from i3pystatus import Status
from i3pystatus import get_module
from i3pystatus.updates import dnf
import subprocess
import logging

from colors import *


status = Status(
        logfile='/home/curtis/.config/i3/i3pystatus/logs/i3pystatus_monitor2.log',
        logformat='%(asctime)s $(levelname)s:',
        standalone=True,
        )


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

# Display updates
status.register("updates",
                        format = "Updates: {count}",
                        #color = "#689d6a",
                        #color_no_updates = "#ebdbb2",
                        color = updates,
                        color_no_updates = color_no_updates,
                        color_working = None,
                        format_no_updates = "No updates",
                        format_working = "Working...",
                        notification_icon = "software-update-available",
                        backends = [dnf.Dnf()],)

# Shows disk usage of /home/curtis/
status.register("disk",
                        path="/home/curtis/",
                        hints = {"markup": "pango"},
                        format = "<span color=\"#ebdbb2\"> :</span> {used}/{total}G [{avail}G]",
                        #color = "#d79921",)
                        #color = "#afaf87",)
                        color = color_disk,)



# Shows internet connection status
status.register("online",
                        format_online = '',
                        #color = '#98971a',
                        #color = '#00DD00',
                        color = color_online,
                        format_offline = '',
                        #color_offline = '#FF0000',)
                        color_offline = color_offline,)


# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces

status.register("network",
                        interface="enp2s0",
                        hints = {"markup": "pango"},
                        format_up="<span color=\"#ebdbb2\"> :</span> {v4} ",
                        #color_up = "#98971a",
                        #color_up = "#fd971f",
                        #color_down = "red",)
                        color_up = color_network_up,
                        color_down = color_network_down,)


status.run()
