#!/bin/bash
#remove x708 old installtion
sudo sed -i '/x708/d' /etc/rc.local
sudo sed -i '/x708/d' ~/.bashrc

sudo rm /usr/local/bin/x708softsd.sh -f
sudo rm /etc/x708pwr.sh -f
