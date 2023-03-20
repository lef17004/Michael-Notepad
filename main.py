import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import * 
 

window = tk.Tk()

menu = Menu(window)
 

fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label ='New', command = None)
fileMenu.add_command(label ='New window', command = None)
fileMenu.add_command(label ='Open', command = None)
fileMenu.add_command(label ='Save', command = None)
fileMenu.add_command(label ='Save as', command = None)
fileMenu.add_command(label ='Page setup', command = None)
fileMenu.add_command(label ='Print', command = None)
fileMenu.add_command(label ='Exit', command = None)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label ='Undo', command = None)
editMenu.add_command(label ='Cut', command = None)
editMenu.add_command(label ='Copy', command = None)
editMenu.add_command(label ='Paste', command = None)
editMenu.add_command(label ='Delete', command = None)
editMenu.add_command(label ='Find', command = None)
editMenu.add_command(label ='Find next', command = None)
editMenu.add_command(label ='Find previous', command = None)
editMenu.add_command(label ='Replace', command = None)
editMenu.add_command(label ='Go to', command = None)
editMenu.add_command(label ='Select all', command = None)
editMenu.add_command(label ='Time/Date', command = None)
editMenu.add_command(label ='Font', command = None)

viewMenu = Menu(menu)
menu.add_cascade(label="View", menu=viewMenu)
viewMenu.add_command(label ='Zoom', command = None)
viewMenu.add_command(label ='Status bar', command = None)
viewMenu.add_command(label ='Word wrap', command = None)

window.config(menu=menu)
ScrolledText(window).pack()

window.mainloop()