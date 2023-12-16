import tkinter as tk
from tkinter import Entry, Label, Button
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator App")

        self.label = Label(master, text="Generated Password:")
        self.label.pack()

        self.password_entry = Entry(master, state='disabled')
        self.password_entry.pack()

        self.generate_button = Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

    def generate_password(self):
        password_length = 8  # You can adjust the length as needed
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
        self.password_entry.config(state='normal')
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.password_entry.config(state='disabled')

# Create the main window
root = tk.Tk()

# Create an instance of the PasswordGeneratorApp
app = PasswordGeneratorApp(root)

# Run the Tkinter event loop
root.mainloop()
