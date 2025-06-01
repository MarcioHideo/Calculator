from tkinter import ttk
from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.clicked = 0
        self.result_content = StringVar(value = "You clicked 0 time.")
        
        # Creating frame
        frame = ttk.Frame(self.root, padding= 10)
        frame.grid()

        # Creating button
        button = ttk.Button(frame, text = "Click", command = self.calculate)
        button.grid(column= 0, row = 0)

        # Creating Label
        label = ttk.Label(frame, textvariable= self.result_content)
        label.grid(column = 0, row = 1)

    # Function to calculate the clicks
    def calculate(self):
        self.clicked+= 1
        self.result_content.set(f"You clicked {self.clicked} times.")


if __name__ == "__main__":
    root = Tk()
    App = Calculator(root)
    root.mainloop()