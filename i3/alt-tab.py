#!/usr/bin/python3

import operator
import subprocess
import json

output_workspace = subprocess.Popen(
        ['i3-msg','-t','get_workspaces'],
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)

output,err = output_workspace.communicate()

# make the output readable json
str_response = output.decode('utf-8')
readable_json = json.loads(str_response)

# loop through all indicies of "num"
# This will tell us how many workspaces are active
# as well as which one has focus
#
# The num cooresponding to the focused workpsace is our
# starting point.
#
# Then we add 1 to that number each time the key combo is pressed
#
# If the focused workspace is equal to the number of workspaces
# the next keypress starts at 1


workspace_list = []
current_workspace = ""
next_workspace = ""

for i in readable_json:
    # make the list of workspaces and sort it
    num_values = i["num"]

    workspace_list.append(num_values)
    workspace_list = sorted(workspace_list)

    focused = i["focused"]
    # find which of the workspaces have the focus
    # this will be our starting point
    # to figure out what the next workspace will be
    if focused == True:
        current_workspace = num_values

# enumerate the list so that the workspaces and indicies are in order
# when i3-msg outputs the json data, these get jumbled sometimes
enum_list = list(enumerate(workspace_list))
# here we get the index of the current workspace that has focus
current_index = workspace_list.index(current_workspace)

# determine the max and min index and values of the active workpsaces
min_index, min_value = min(enumerate(workspace_list), key=operator.itemgetter(1))
max_index, max_value = max(enumerate(workspace_list), key=operator.itemgetter(1))

# to figure out where to go next we have to
# increment the index by 1 unless doing so brings it out of range
# then we just go back to 0
if current_index >= max_index:
    next_workspace_index = 0
    next_workspace = enum_list[0][1]
    #print("i3-msg workspace " + str(next_workspace))
    subprocess.call(["i3-msg","workspace", str(next_workspace)])
else:
    next_workspace_index = current_index + 1
    next_workspace = enum_list[next_workspace_index][1]
    subprocess.call(["i3-msg","workspace", str(next_workspace)])
