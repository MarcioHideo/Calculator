from tkinter import ttk
from tkinter import *

# Create a root, which it is the parent of every widget later
root = Tk() # object
frame = ttk.Frame(root) # child of root, but parent of all widgets 
frame.grid(column=0,row=0)


def calculate(*args):
    ...
    
# Creating a button
button = ttk.Button(frame, text = "Click", command = calculate)
button.grid(column=0, row=0)
button['padding'] = 5


# s = ttk.Style()
# s.configure('Danger.TFrame', background = 'red', borderwidth=5)
# ttk.Frame(root, width=200, height=200, style='Danger.TFrame').grid()



def print_hierarchy(w, depth = 0):
    print('  '*depth + w.winfo_class() + ' w=' + str(w.winfo_width()) + ' h=' + str(w.winfo_height()) + ' x=' + str(w.winfo_x()) + ' y=' + str(w.winfo_y()))
    for i in w.winfo_children():
        print_hierarchy(i, depth+1)

print_hierarchy(root)


# Using Label, only a view with no interaction with user ************************
# label = ttk.Label(root, text = 'Testing the Label')
# label.grid(column=0, row=0)



root.mainloop()