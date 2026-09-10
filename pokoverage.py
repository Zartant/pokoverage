from tkinter import Tk, StringVar, Label, Entry, Button
from functools import partial
import json

with open("relationship_grid.json") as f:
    rel = json.load(f)

print(rel)

root = Tk()
label1 = Label(root, text="hello")
label2 = Label(root,text="flo")
label1.grid(column = 0, row=0)
label2.grid(column = 0, row=1)
root.mainloop()
