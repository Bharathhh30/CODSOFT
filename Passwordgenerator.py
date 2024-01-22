import random
import string
import tkinter as tk
from tkinter import Entry, Label, Button, StringVar, Text, Scrollbar

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = ['@', '#', '%', "_", "*", "&", "^"]
c = list(string.ascii_lowercase)
d = list(string.ascii_uppercase)

Weak = list([a, c, d])
Strong = list([a, b, c, d])

def generate_password():
    password_var.set("")  # Clear previous password
    n = int(length_entry.get())
    strength = strength_var.get()

    password = []
    if strength.lower() == "strong":
        for i in range(n):
            random_list_selection = random.choice(Strong)
            random_element = random.choice(random_list_selection)
            password.append(random_element)
    elif strength.lower() == "weak":
        for i in range(n):
            random_list_selection = random.choice(Weak)
            random_element = random.choice(random_list_selection)
            password.append(random_element)

    # Set the state to 'normal' to insert text
    password_display.config(state='normal')
    password_display.delete(1.0, tk.END)
    password_display.insert(tk.END, "".join(map(str, password)))
    # Set the state back to 'disabled'
    password_display.config(state='disabled')

# Create the main window
window = tk.Tk()
window.title("Password Generator")

custom_font=("Helvetica",25)

# Length label and entry
length_label = Label(window, text="Enter the Length of password:")
length_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
length_entry = Entry(window, width=30)
length_entry.grid(row=0, column=1, padx=10, pady=5)

# Strength label and entry
strength_label = Label(window, text="Enter the Strength of the password (Strong or Weak):")
strength_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
strength_var = StringVar()
strength_entry = Entry(window, textvariable=strength_var, width=30)
strength_entry.grid(row=1, column=1, padx=10, pady=5)

# Button to generate password
generate_button = Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Display the generated password
password_var = StringVar()
password_label = Label(window, text="Generated Password:")
password_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
password_display = Text(window, height=3, width=30, state='disabled')
password_display.grid(row=3, column=1, padx=10, pady=5)

# Scrollbar for the password display
password_scrollbar = Scrollbar(window, command=password_display.yview)
password_scrollbar.grid(row=3, column=2, sticky='ns')
password_display.config(yscrollcommand=password_scrollbar.set)

# Start the GUI main loop
window.mainloop()
