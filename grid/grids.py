from tkinter import *

root = Tk()

myLabel1 = Label(root, text = "Hello World again")
myLabel2 = Label(root, text = "My name is SomeName")

myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 0)

root.mainloop();
