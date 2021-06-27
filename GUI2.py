import tkinter as tk
import socket 
from tkinter.ttk import *

FORMAT ='utf-8'
#SERVER = ""
PORT=8888
#ADDR=(SERVER,PORT)
listOfJunctions={}

def sendCommand():
    selection = str(v.get())
    client.send(str(selection).encode(FORMAT))
    junDetails.destroy()

#CLIENT SERVER
def connectToServer(server):
    global client,v,junDetails
    ADDR=(server,PORT)
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)
    #client.send(str("junction Name").encode(FORMAT))
    JunctionDetails = (client.recv(1024).decode(FORMAT)).split(",")
    print(JunctionDetails)
    junDetails = tk.Tk()
    v = tk.StringVar(junDetails)
    values = {"ON" : "1","OFF" : "2"}
    canvas5 = tk.Canvas(junDetails, width = 400, height = 300)
    canvas5.pack()
    for (text, value) in values.items():
        tk.Radiobutton(junDetails, text = text, variable = v,value = value,command = sendCommand).pack(side = tk.TOP, ipady = 5)
    j = tk.Text(junDetails,height = 5, width = 52)
    lat = tk.Text(junDetails,height = 5, width = 52)
    lon = tk.Text(junDetails,height = 5, width = 52)
    j.pack(side=tk.TOP)
    lat.pack(side=tk.TOP)
    lon.pack(side=tk.TOP)
    j.insert(tk.END,"Name = "+JunctionDetails[0])
    lat.insert(tk.END,"Latitude ="+JunctionDetails[1])
    lon.insert(tk.END,"Longitude ="+JunctionDetails[2])


def makelist():
    global listOfJunctions
    x1 = entry1.get()
    x2 = entry2.get()
    listOfJunctions[x1]=x2
    addj.destroy()

def addjunnction ():
    global entry1,entry2,addj
    addj= tk.Tk()
    canvas2 = tk.Canvas(addj, width = 400, height = 300)
    canvas2.pack()
    entry1 = tk.Entry (addj) 
    canvas3 = tk.Canvas(addj,width = 400, height=300)
    canvas3.pack()
    entry2 = tk.Entry(addj)
    canvas2.create_window(200, 50, window=entry1)
    canvas3.create_window(200, 20,window=entry2)
    button2 = tk.Button(addj,text='Add Junction',command=makelist)
    canvas2.create_window(200, 200, window=button2)

def viewJunctions():
    viewj=tk.Tk()
    canvas4 = tk.Canvas(viewj, width = 400, height = 300)
    canvas4.pack()
    for keys,values in  listOfJunctions.items():
        butName=tk.Button(viewj,text=keys,command=lambda:connectToServer(values))
        canvas4.create_window(200, 200, window=butName)

def mainwindow():
    global canvas1,entry1,entry2,root
    root= tk.Tk()
    canvas1 = tk.Canvas(root, width = 400, height = 300)
    canvas1.pack()
#    canvas1.create_window(200, 140, window=entry1)
    button1 = tk.Button(text='Add', command=addjunnction)
    button1.pack()
    canvas1.create_window(200, 180, window=button1)
    button2 = tk.Button(text='View Junctions', command=viewJunctions)
    button2.pack()
    canvas1.create_window(200, 180, window=button1)
    root.mainloop()

mainwindow()


