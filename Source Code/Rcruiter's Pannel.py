# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
import subprocess

# Initialize empty lists for notifications and recruiter data
notifications = []
recruiter_data = []

# Function to update the notifications list display
def update_notifications_list():
    notifications_listbox.delete(0, tk.END)  # Clear the listbox
    for notification in notifications:
        notifications_listbox.insert(tk.END, notification)

# Function to open details of a notification
def open_notification_details(event):
    selected_index = notifications_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        notification = notifications[index]
        # You can display the details of the selected notification here
        messagebox.showinfo("Notification Details", notification)

# Function to update the recruiter data list display
def update_recruiter_data_list():
    recruiter_data_listbox.delete(0, tk.END)  # Clear the listbox
    for data in recruiter_data:
        recruiter_data_listbox.insert(tk.END, data)

# Function to open details of a recruiter's data
def open_recruiter_data_details(event):
    selected_index = recruiter_data_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        data = recruiter_data[index]
        # You can display the details of the selected data here
        messagebox.showinfo("Recruiter Data Details", data)

# Function to open "Job Description.py"
def open_job_description():
    try:
        subprocess.Popen(["python", "Job Description.py"])
    except Exception as e:
        # Handle any exceptions here
        messagebox.showerror("Error", str(e))

# Function to handle the click event for "Requirement 1"
def open_requirement_description(event):
    if assigned_requirements_listbox.get(tk.ACTIVE) == "Requirement 1":
        open_job_description()

# Create the main window
root = tk.Tk()
root.title("Recruiter's Panel")

# Set the window size
root.geometry("800x600")  # Adjust the size as needed

# Create and place widgets
frame = tk.Frame(root, padx=20, pady=20, bg="#f2f2f2")
frame.pack(fill=tk.BOTH, expand=True)

# Create a title label for "Recruiter's Panel"
title_label = tk.Label(frame, text="Recruiter's Panel", font=("Helvetica", 24, "bold"), pady=10, bg="#4CAF50", fg="white")
title_label.pack(fill=tk.X)

# Create a label for the assigned requirements section heading
assigned_requirements_heading = tk.Label(frame, text="Assigned Requirements", font=("Helvetica", 16, "bold"), bg="#f2f2f2")
assigned_requirements_heading.pack(anchor="w", padx=10, pady=10)

# Create a listbox to display the assigned requirements
assigned_requirements_listbox = tk.Listbox(frame, height=10, width=60)
# Add "Requirement 1" to the listbox
assigned_requirements_listbox.insert(tk.END, "Requirement 1")
# Add "Requirement 2" to the listbox
assigned_requirements_listbox.insert(tk.END, "Requirement 2")
assigned_requirements_listbox.pack()

# Bind the double-click event for "Requirement 1"
assigned_requirements_listbox.bind("<Double-Button-1>", open_requirement_description)

# Create a label for the notifications section heading
notifications_heading = tk.Label(frame, text="Notifications", font=("Helvetica", 16, "bold"), bg="#f2f2f2")
notifications_heading.pack(anchor="w", padx=10, pady=10)

# Create a listbox to display the notifications
notifications_listbox = tk.Listbox(frame, height=10, width=60)
update_notifications_list()  # Update the list initially
notifications_listbox.pack()

# Create a button to refresh notifications
refresh_button = tk.Button(frame, text="Refresh Notifications", command=update_notifications_list, bg="#4CAF50", fg="white")
refresh_button.pack(pady=10)

# Create a label for the recruiter data section heading
recruiter_data_heading = tk.Label(frame, text="Recruiter Data", font=("Helvetica", 16, "bold"), bg="#f2f2f2")
recruiter_data_heading.pack(anchor="w", padx=10, pady=10)

# Create a listbox to display the recruiter data
recruiter_data_listbox = tk.Listbox(frame, height=10, width=60)
update_recruiter_data_list()  # Update the list initially
recruiter_data_listbox.pack()

# Create a button to refresh recruiter data
refresh_recruiter_data_button = tk.Button(frame, text="Refresh Recruiter Data", command=update_recruiter_data_list, bg="#4CAF50", fg="white")
refresh_recruiter_data_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
