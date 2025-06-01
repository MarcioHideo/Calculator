from tkinter import ttk
from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.clicked = 0
        self.result_content = StringVar(value = "")
        
        
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
            button = ttk.Button(frame, text = item[0], command=lambda val=item[0]: self.handle_text(val))
            button.grid(row=item[1], column = item[2])


        # button = ttk.Button(frame, text = "Click", command = self.calculate)
        # buttonñ.grid(column= 0, row = 1)

        # Creating Label
        label = ttk.Label(frame, textvariable= self.result_content)
        label.grid(column = 0, row = 0, columnspan= 5)

    # Handle all the buttons function
    def handle_text(self, value):
        current_value = self.result_content.get()
        if current_value == "Error":
            current_value = ""

        if value == "C":
            self.result_content.set("")
        elif value == "=":
            current_value = current_value.replace("×","*")
            try:
                result = eval(current_value)
                self.result_content.set(result)
            except:
                self.result_content.set("Error") 
        elif value == "±":
            self.resul_content.set(f"{current_value}")
        elif value == "%":
            current_value = float(current_value) * 0.01
            self.result_content.set(f"{current_value}")
        else:
            self.result_content.set(f"{current_value}{value}")



if __name__ == "__main__":
    root = Tk()
    App = Calculator(root)
    root.mainloop()