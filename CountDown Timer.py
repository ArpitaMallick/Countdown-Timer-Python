#!/usr/bin/env python
# coding: utf-8

# In[27]:


import tkinter as tk
from tkinter import *


# In[28]:


t=0
def set_timer():
    global t
    t=t+int(t1.get())
    return t

def countdown():
    global t
    if t>0:
        l1.config(text=t)
        t=t-1
        l1.after(1000, countdown)
    elif t==0:
        l1.config(text="TIME OVER")


box = tk.Tk()
box.title("Countdown Timer")
box.geometry('160x120')

l1=Label(box, font="times 20")
l1.grid(row=1,column=2)

t1 = tk.Entry(box)
t1.grid(row=3,column=2)

b1 = tk.Button(box, text="SET", command = set_timer)
b1.grid(row=4,column=2,padx=20)

b2 = tk.Button(box, text="START", command = countdown)
b2.grid(row=6,column=2,padx=20)

box.mainloop()


# In[ ]:




