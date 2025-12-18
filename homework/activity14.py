import tkinter as tk
import random
import string
from tkinter import messagebox

def generated_password():
    try:
        length = int(length_var.get())
        chars = ""

        if upper_var.get():
            chars += string.ascii_uppercase
        if lower_var.get():
            chars += string.ascii_lowercase
        if digits_var.get():
            chars += string.digits
        if symbols_var.get():
            chars += string.punctuation

        if not chars:
            result_var.set("Select at least one option!")
            return

        if length <= 0:
            result_var.set("Enter valid length!")
            return

        password = ''.join(random.choice(chars) for i in range(length))
        result_var.set(password)

    except ValueError:
        result_var.set("Length must be a number")

def copy_password():
    window.clipboard_clear()
    window.clipboard_append(result_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

def reset():
    length_var.set("")
    result_var.set("")
    upper_var.set(False)
    lower_var.set(False)
    digits_var.set(False)
    symbols_var.set(False)

window = tk.Tk()
window.title("Password Generator")
window.geometry("450x380")
window.resizable(False, False)

tk.Label(window, text="Random Password Generator",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(window, text="Password Length").pack(pady=5, padx=10)
length_var = tk.StringVar()
tk.Entry(window, textvariable=length_var).pack(pady=5, padx=10)

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(window, text="Uppercase Letters",
               variable=upper_var).pack( padx=10,pady=2)
tk.Checkbutton(window, text="Lowercase Letters",
               variable=lower_var).pack( padx=10,pady=2)
tk.Checkbutton(window, text="Digits",
               variable=digits_var).pack( padx=10,pady=2)
tk.Checkbutton(window, text="Symbols",
               variable=symbols_var).pack( padx=10,pady=2)

tk.Button(window, text="Generate Password",
          command=generated_password).pack(pady=8, padx=10)
tk.Button(window, text="Copy Password",
          command=copy_password).pack(pady=5, padx=10)
tk.Button(window, text="Reset",
          command=reset).pack(pady=5, padx=10)
result_var = tk.StringVar()
tk.Entry(window, textvariable=result_var,
         width=45).pack(pady=10, padx=10)
window.mainloop()

