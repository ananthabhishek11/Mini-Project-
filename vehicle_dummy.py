# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 19:02:39 2021

@author: HP
"""

import socket 
import geocoder

FORMAT ='utf-8'
SERVER = "127.0.0.1"
PORT=8888
ADDR=(SERVER,PORT)

# JunctionName = "Singanallur"
# j_latitude = "11.000660"
# j_longitude= "77.029573"

g = geocoder.ip('me')
location = g.latlng

# data=str(location[0])+","+str(location[1])+","+"60"
data=str(11.003363)+","+str(77.048518)+","+"60"
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
client.send(str(data).encode(FORMAT))
