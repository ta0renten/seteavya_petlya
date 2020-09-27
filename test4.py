from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from sqlite3 import*
import time
import random
import webbrowser
import tkinter

tk = Tk()
app_running = True

size_canvas_x = 768
size_canvas_y = 768
class But:
     def __init__(self):
          self.but = Button(root)
          self.but["text"] = "помощь"
          self.but.bind("<Button-1>", open)
          self.but.pack()
     def open(event):
         import webbrowser
         webbrowser.open("https://google.com")

root = Tk()
obj = But()
obj = But1()
root.mainloop()
