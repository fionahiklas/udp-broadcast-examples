## Overview

We have a new shiney iKettle 2.0 but I'd rather it not have direct access to our network as I'm worried about it being hacked!  Okay, this may be paranoia but it still seems a sensible precaution given that IoT (Internet of Things) devices seems to be badly secured on the whole.

So I've set up a seperate wireless access point and connected this onto a USB ethernet interface plugged into my pfSense router.

The problem is, it's not a simple matter of forwarding ports to get this to work, it's actually more complicated and, in fact it appears that the client application for the iKettle is sending out broadcast UDP packets on port 2081 in order to find the device.

This led me to wonder about UDP and broadcast packets - I looked for a UDP proxy but can't find this for pfSense.

## Investigation


### UDP Client/Server

I Found the code for the example server [here](http://www.java2s.com/Code/Python/Network/UDPBroadcastServer.htm) 
