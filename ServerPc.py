# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 08:18:42 2021
Sockect 
@author: HP
"""
import socket
import threading
from math import radians, sin, cos, acos

# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "127.0.0.1"
PORT = 8888
ADDR =(SERVER,PORT)
FORMAT =  'utf-8'

JunctionName = "Singanallur"
j_latitude = "11.000660"
j_longitude= "77.029573"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

#for connection between control room and junction
# def handle_client(conn,addr):
#     print(addr,' connected')
#     connected = True
#     conn.send(str(JunctionName+","+j_latitude+","+j_longitude).encode(FORMAT))
#     while connected:
#         content = conn.recv(1080).decode(FORMAT)
#         if content:
#             print(content)
#             if(content=="1"):
#                 print("Junction ON")
#             else:
#                 print("Road is blocked please choose alternate route")
#             connected = False
#     print("Closing connection")
#     conn.close()

#for finding distance
def handle_client(conn,addr):
    print(addr,' connected')
    data = conn.recv(1080).decode(FORMAT)
    print("The data received are latitude, longitude, speed, "+data)
    data=data.split(",")
    # print(v_latitude,v_longitude,v_speed)
    slat=radians(float(j_latitude))
    elat=radians(float(data[0]))
    slon=radians(float(j_longitude))
    elon=radians(float(data[1]))
    dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
    time = (dist/float(data[2]))*60
    print(str(dist)+"km ",str(time)+"min")
    # conn.send(str(dist).encode(FORMAT))
    # conn.send(str(time).encode(FORMAT))
    # connected = False
    print("closing connection")
    conn.close()



def start():
    server.listen()
    print('Server listening on ',SERVER)
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target = handle_client,args=(conn,addr))
        thread.start()
        print('No of connenctions :',threading.activeCount()-1)


print('Server is starting')
start()
