# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess

# Function to open the selected panel
def open_selected_panel():
    selected_role = role_var.get()
    
    if selected_role == "C Level":
        subprocess.Popen(["python", "C Level Pannel.py"], shell=True)
    elif selected_role == "Manager":
        subprocess.Popen(["python", "Manager's Panel.py"], shell=True)
    elif selected_role == "Recruiter":
        subprocess.Popen(["python", "Rcruiter's Pannel.py"], shell=True)

# Function to check login credentials
def check_credentials():
    password = password_entry.get()
    selected_role = role_var.get()  # Get the selected user role

    # Replace with your authentication logic
    if selected_role == "C Level" and password == "123":
        messagebox.showinfo("Login Successful", f"Welcome, {selected_role}!")
        open_selected_panel()  # Open the selected panel
    elif selected_role == "Recruiter" and password == "124":
        messagebox.showinfo("Login Successful", f"Welcome, {selected_role}!")
        open_selected_panel()  # Open the selected panel
    elif selected_role == "Manager" and password == "125":
        messagebox.showinfo("Login Successful", f"Welcome, {selected_role}!")
        open_selected_panel()  # Open the selected panel
    else:
        messagebox.showerror("Login Failed", "Invalid password or role")

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Set the window size to be larger
root.geometry("600x400")  # Adjust the size as needed

# Create and place widgets
frame = tk.Frame(root)
frame.pack(pady=50)

# Add the company name label with a larger font
company_label = tk.Label(frame, text="Welltech Infotech Pvt Ltd.", font=("Helvetica", 20, "bold"))
company_label.grid(row=0, column=0, columnspan=2, pady=20)

# Create a dropdown menu for user roles with a larger font
roles = ["C Level", "Manager", "Recruiter"]
role_var = tk.StringVar()
role_dropdown = ttk.Combobox(frame, textvariable=role_var, values=roles, font=("Helvetica", 14))
role_dropdown.set("Select Role")  # Default text for the dropdown
role_dropdown['state'] = 'readonly'  # Make it read-only

label_password = tk.Label(frame, text="Select User Role:", font=("Helvetica", 14))
label_role = tk.Label(frame, text="Password:", font=("Helvetica", 14))

password_entry = tk.Entry(frame, show="*")  # Use show="*" to hide the password characters

login_button = tk.Button(frame, text="Login", font=("Helvetica", 16), command=check_credentials)

label_role.grid(row=2, column=0, sticky="e")
label_password.grid(row=1, column=0, sticky="e")

password_entry.grid(row=2, column=1)
role_dropdown.grid(row=1, column=1)
login_button.grid(row=3, columnspan=2)

# Start the Tkinter main loop
root.mainloop()
