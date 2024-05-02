import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Entry widget for displaying the calculation
        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(master, textvariable=self.entry_var, justify="right", font=("Helvetica", 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        # Create and place the buttons
        for (text, row, col) in buttons:
            ttk.Button(master, text=text, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10)

        # Configure row and column weights so that they expand proportionally
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        current_text = self.entry_var.get()

        if button_text == '=':
            try:
                result = eval(current_text)
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")
        else:
            self.entry_var.set(current_text + button_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
