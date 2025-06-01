from tkinter import ttk
from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.clicked = 0
        self.result_content = StringVar(value = "You clicked 0 time.")
        
        # Creating frame
        # frame = ttk.Frame(self.root, padding= 10)
        frame = ttk.Frame(self.root, borderwidth=6, relief="ridge", width=200, height=100)
        frame.grid()

        # Buttons style with ("textValue","row","column")
        buttons = (
            ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("×", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 3, 2)
        )

        # Creating button for calculator
        for item in buttons:
            button = ttk.Button(frame, text = item[0], command= self.calculate)
            button.grid(row=item[1], column = item[2])


        # button = ttk.Button(frame, text = "Click", command = self.calculate)
        # button.grid(column= 0, row = 1)

        # Creating Label
        label = ttk.Label(frame, textvariable= self.result_content)
        label.grid(column = 0, row = 0, columnspan= 5)

    # Function to calculate the clicks
    def calculate(self):
        self.clicked+= 1
        self.result_content.set(f"You clicked {self.clicked} times.")


if __name__ == "__main__":
    root = Tk()
    App = Calculator(root)
    root.mainloop()