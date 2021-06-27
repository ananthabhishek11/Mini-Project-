# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 08:44:14 2021
Client
@author: HP
"""
import socket 

FORMAT ='utf-8'
SERVER = "127.0.0.1"
PORT=9999
ADDR=(SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
client.send(str("junction Name").encode(FORMAT))

