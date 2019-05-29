#timelapse shell script
#43200000ms in 12 hours
#This script will take a picture every 30 seconds for 12 hours
raspistill -t 43200000 -tl 30000 -o /home/pi/Pictures/timelapse/image%04d.jpg