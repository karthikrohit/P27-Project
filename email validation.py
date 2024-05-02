import tkinter as tk
from tkinter import ttk
import re
from tkinter import messagebox  

class FormApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Form Validation")

        self.email_var = tk.StringVar()

        # Email Entry
        ttk.Label(master, text="Email:").grid(row=0, column=0, padx=10, pady=10)
        self.email_entry = ttk.Entry(master, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=0, column=1, padx=10, pady=10)

        # Submit Button
        ttk.Button(master, text="Submit", command=self.submit_form).grid(row=1, column=0, columnspan=2, pady=10)

    def submit_form(self):
        email = self.email_var.get()

        if self.is_valid_email(email):
            messagebox.showinfo("Success", "Form submitted successfully!")
        else:
            messagebox.showerror("Error", "Form failed to submit. Invalid email address.")

    def is_valid_email(self, email):
        # Simple email validation using a regular expression
        pattern = r'^\S+@\S+\.\S+$'
        return re.match(pattern, email) is not None

if __name__ == "__main__":
    root = tk.Tk()
    app = FormApp(root)
    root.mainloop()
