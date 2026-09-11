from tkinter import *
from functools import partial
import json

global types
global colour
global types_checkbox
global root 
global rel 
global type_string_var

FIXED_X_LENGTH = 7
def z():
    default = 0
    for v in type_string_var:
        v.set(str(default))

    selected = []
    for val, type_name in zip(types, rel.keys()):
        if val['selected'].get() == 1:
            selected.append(type_name)

    for text, type_name in zip(type_string_var, rel.keys()):
        curr_val = float(text.get())
        for s in selected:
            curr_sel_val = float(rel[s]['rel'][type_name])
            if curr_sel_val > curr_val:
                curr_val = curr_sel_val
        if curr_val == 0.5:
            text.set(str(curr_val))
        else:
            text.set(str(int(curr_val)))    
with open("relationship_grid.json") as f:
    rel = json.load(f)
root = Tk()
colour = []
for c in rel.values():
    colour.append(c["color"])

labelframe_input = LabelFrame(root,text="Attack types")
labelframe_output = LabelFrame(root,text="Pokoverage")

labelframe_input.pack(fill="both", side="top")
labelframe_output.pack(fill="both", side="bottom")
types = []
types_checkbox = []
i = 0
for r in rel.keys():
    val = IntVar()
    types.append ({'name' : r, 'selected' : val})
    types_checkbox.append(Checkbutton(labelframe_input, text=r,variable= val, onvalue= 1, offvalue=0, bg=colour[i], width=FIXED_X_LENGTH))
    i += 1

for check in types_checkbox:
    check.pack(side = LEFT)
run_button = Button(labelframe_input,text= "compute", command=z)
run_button.pack(side= BOTTOM)

i = 0
type_text = []
type_string_var = []
for r in rel.keys():
    new_string = StringVar()
    label = Label(labelframe_output, textvariable=new_string, width=FIXED_X_LENGTH+ 3)
    new_string.set("x")
    type_text.append(label)
    type_string_var.append(new_string)
    label.pack(side=LEFT)

root.mainloop()
