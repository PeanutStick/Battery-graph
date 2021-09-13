#!/bin/bash
capacity=$( cat /sys/class/power_supply/BAT0/capacity )
status=$( cat /sys/class/power_supply/BAT0/status )
upsince=$( uptime -s | awk '{print $2}' )
currenttime=$( uptime | awk '{print $1}' )

#echo "La capacité est de $capacity% depuis $upsince il est $currenttime et la battery se $status"


# Convert to epoch time and calculate difference.
difference=$(( $(date -d "$currenttime" "+%s") - $(date -d "$upsince" "+%s") ))
up=$(echo "$difference/60" | bc )
echo "$up,$currenttime,$capacity,$status" >> /path/to/the/same/directory/as/main.py/bat-data1.csv #change it

