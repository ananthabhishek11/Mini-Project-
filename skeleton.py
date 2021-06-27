# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 12:31:50 2021

@author: HP
"""

from tkinter import*
def nwindow():
  new_window=Toplevel(root)
  new_window.geometry("200x200")
  new_window.title("junction")
  label=Label(new_window,text="junction details")
  label.pack()
  btn1=Button(new_window, text ="ON")
  btn1.pack()
  btn2=Button(new_window, text ="OFF",command=lambda: new_window.destroy())
  btn2.pack()
root=Tk()
btn1 = Button(root, text="junction 1",command=nwindow)
btn1.pack(padx=20,pady=20)
btn2 = Button(root, text="junction 2",command=nwindow)
btn2.pack(padx=20,pady=20)
btn3 = Button(root, text="junction 3",command=nwindow)
btn3.pack(padx=20,pady=20)
btn4 = Button(root, text="junction 4",command=nwindow)
btn4.pack(padx=20,pady=20)
root.geometry("500x500")
root.title("MY PROJECT GUI")
root.mainloop()