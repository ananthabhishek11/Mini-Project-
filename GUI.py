from tkinter import*
from tkinter.ttk import *
def nwindow():
  master = Tk()
  master.geometry("175x175")
  master.title("junction details")
 
# Tkinter string variable
# able to store any string value
v = StringVar(master, "1")
 
# Dictionary to create multiple buttons
values = {"ON" : "1",
        "OFF" : "2",
        }
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(master, text = text, variable = v,
        value = value).pack(side = TOP, ipady = 5)

# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
def main(junction):
    root=Tk()
    btn1 = Button(root, text=junction,command=nwindow)
    btn1.pack(padx=20,pady=20)
    root.geometry("500x500")
    root.title("MY PROJECT GUI")
    root.mainloop()