#Display IP

#Introduction
This application runs on the background and listens on the button event.

#Installation

1. Make the directory of the source.
mkdir /home/pi/workbench/DisplayIp
mkdir /home/pi/workbench/DisplayIp/bin
mkdir /home/pi/workbench/DisplayIp/logs
mkdir /home/pi/workbench/DisplayIp/src

2. Setup the systemctl
2.a Copy the service file
sudo cp displayip.service /lib/systemd/system/
2.b Reload the systemctl
sudo systemctl daemon-reload
2.c Enable the systemctl so that it gets loaded at boot
sudo systemctl  enable displayip

3. Code and dependencies
The code goes in the src folder.
The bin file goes in the bin folder
The display.service goes to the systemd folder

#Execution
To start the service execute this:
* sudo systemctl start displayip

To check if the service is running type:
* systemctl status displayip.service


##Reference
https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units
