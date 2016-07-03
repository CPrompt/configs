from i3pystatus import Status
from i3pystatus import get_module
from i3pystatus.updates import dnf
status = Status(logfile='/home/curtis/Desktop/i3pystatus.log')



status.register("pulseaudio",
# font-awesome f028
	format = ' : {volume}',)


status.register("clock",
#  Note: this config requires the gsimplecal package to be installed
    hints = {"markup": "pango"},
    format = " %a %d %b <span color=\"#fff\">  </span>  %H:%M:%S %P <span color=\"#fff\"> </span> ",
#    format = "(' %a %d %b ', America/New_York)",
    color = "#5f87af",
    on_leftclick = ["gsimplecal"],
    )

# Shows disk usage of /home/curtis/
status.register("disk",
		path="/home/curtis/",
		hints = {"markup": "pango"},
		format = "<span color=\"#fff\"> :</span> {used}/{total}G [{avail}G]",
		color = "#afaf87",)

# Shows internet connection status
status.register("online",
    format_online = '',
    color = '#00DD00',
    format_offline = '',
    color_offline = '#FF0000',
        )

status.register("network",
    interface="enp2s0",
    hints = {"markup": "pango"},
    format_up="<span color=\"#fff\"> :</span> {v4} ",
    color_up = "#fd971f",
    color_down = "red",
    )


status.run()
