import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    """
    Generates a random password based on user-defined length and complexity.

    Retrieves the length and complexity values from the GUI scales,
    constructs a character set based on the selected complexity level,
    and generates a password of the specified length using random choices
    from the character set. Inserts the generated password into the password
    entry field.
    """
    length = length_scale.get()
    complexity = complexity_scale.get()

    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than zero.")
        return

    if complexity <= 0:
        messagebox.showerror("Error", "Password complexity must be greater than zero.")
        return 

    characters = ""
    if complexity >= 1:
        characters += string.ascii_letters
    if complexity >= 2:
        characters += string.digits
    if complexity >= 3:
        characters += string.punctuation

    password = ''.join(random.choices(characters, k=length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

def reset_password():
    """
    Resets the password generation parameters and clears the password entry field.
    """
    length_scale.set(8)
    complexity_scale.set(1)
    password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Password Generator")

# Heading
heading_label = tk.Label(root, text="Custom Password Generator", font=("Helvetica", 16, "bold"))
heading_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Password length Entry
length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 12))
length_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

length_scale = tk.Scale(root, from_=1, to=50, orient=tk.HORIZONTAL, length=200, bg="lightgrey")
length_scale.set(8)
length_scale.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Password Complexity Entry
complexity_label = tk.Label(root, text="Password Complexity:", font=("Helvetica", 12))
complexity_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

complexity_scale = tk.Scale(root, from_=1, to=3, orient=tk.HORIZONTAL, length=200, bg="lightgrey")
complexity_scale.set(1)
complexity_scale.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Generate Password Button
generate_button = tk.Button(root, text="Generate Password", bg="green", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Password Display
password_label = tk.Label(root, text="Generated Password:", font=("Helvetica", 12))
password_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

password_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
password_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Reset Password Button
reset_button = tk.Button(root, text="Reset Password", command=reset_password, bg="red")
reset_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
