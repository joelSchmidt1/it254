# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 20:16:25 2017

@author: Joel
"""

from Tkinter import *

def var_states():
   print("Selection: %d,\nfemale: %d" % (var1.get(), var2.get(), var3.get()))

master = Tk()
Label(master, text="Welcome to Contoso Travel. Say new reservation or press 1. Say change reservation or press 2. Say restaurant recommendation or press 3.").grid(row=0)
master = Tk()
var1 = IntVar()
Checkbutton(master, text="1", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="2", variable=var2).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="3", variable=var2).grid(row=2, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
mainloop( )
