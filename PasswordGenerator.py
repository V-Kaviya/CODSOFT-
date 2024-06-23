import tkinter as tk

from tkinter import messagebox

import random



def generate_password(length=12):



    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"

    password = ''.join(random.choice(characters) for i in range(length))

    return password



def generate_password_button():

    try:

        password_length = int(entry_length.get())

        if password_length <= 0:

            messagebox.showerror("Error", "Length should be a positive integer.")

            return

        generated_password = generate_password(password_length)

        generated_password_var.set(generated_password)

    except ValueError:

        messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")



root = tk.Tk()

root.title("Password Generator")



label = tk.Label(root, text="Enter password length:")

label.pack()



entry_length = tk.Entry(root, width=10)

entry_length.pack()



generate_button = tk.Button(root, text="Generate Password", comimport tkinter as tk

from tkinter import messagebox

import random



def generate_password(length=12):



    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"

    password = ''.join(random.choice(characters) for i in range(length))

    return password



def generate_password_button():

    try:

        password_length = int(entry_length.get())

        if password_length <= 0:

            messagebox.showerror("Error", "Length should be a positive integer.")

            return

        generated_password = generate_password(password_length)

        generated_password_var.set(generated_password)

    except ValueError:

        messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")



root = tk.Tk()

root.title("Password Generator")



label = tk.Label(root, text="Enter password length:")

label.pack()



entry_length = tk.Entry(root, width=10)

entry_length.pack()



generate_button = tk.Button(root, text="Generate Password", command=generate_password_button)

generate_button.pack()



generated_password_var = tk.StringVar()

generated_password_label = tk.Label(root, textvariable=generated_password_var, wraplength=300)

generated_password_label.pack()



root.mainloop()mand=generate_password_button)

generate_button.pack()



generated_password_var = tk.StringVar()

generated_password_label = tk.Label(root, textvariable=generated_password_var, wraplength=300)

generated_password_label.pack()



root.mainloop()