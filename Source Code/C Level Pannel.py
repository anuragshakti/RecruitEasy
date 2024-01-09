# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess

# Initialize empty lists for job requirements, recruiter data, company data, and performance data
job_requirements = []
recruiter_data = []
company_data = []
performance_data = []

# Function to update the job requirements list display
def update_job_requirements_list():
    open_requirements_listbox.delete(0, tk.END)  # Clear the listbox
    for requirement in job_requirements:
        open_requirements_listbox.insert(tk.END, requirement)

# Function to open details of a job requirement
def open_job_requirement_details(event):
    selected_index = open_requirements_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        requirement = job_requirements[index]
        # Check if the selected requirement is the dummy requirement
        if requirement == "Dummy Requirement":
            try:
                # Use subprocess to run "Job Description.py"
                subprocess.run(["python", "Job Description.py"])
            except Exception as e:
                # Handle any exceptions here
                messagebox.showerror("Error", str(e))
        else:
            # You can display the details of the selected job requirement here
            messagebox.showinfo("Job Requirement Details", requirement)

# Function to update the company data list display
def update_company_data_list():
    company_data_listbox.delete(0, tk.END)  # Clear the listbox
    for data in company_data:
        company_data_listbox.insert(tk.END, data)

# Function to open details of company data
def open_company_data_details(event):
    selected_index = company_data_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        data = company_data[index]
        # You can display the details of the selected company data here
        messagebox.showinfo("Company Data Details", data)

# Function to update the performance data list display
def update_performance_data_list():
    performance_data_listbox.delete(0, tk.END)  # Clear the listbox
    for data in performance_data:
        performance_data_listbox.insert(tk.END, data)

# Function to open details of performance data
def open_performance_data_details(event):
    selected_index = performance_data_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        data = performance_data[index]
        # You can display the details of the selected performance data here
        messagebox.showinfo("Performance Data Details", data)

# Create the main window
root = tk.Tk()
root.title("C-Level Panel")

# Set the window size
root.geometry("800x600")  # Adjust the size as needed

# Set a background color for the window
root.configure(bg="#f2f2f2")

# Create and place widgets
frame = tk.Frame(root, padx=20, pady=20, bg="#f2f2f2")
frame.pack(fill=tk.BOTH, expand=True)

# Create a title label for "C-Level Panel" with a professional look
title_label = tk.Label(frame, text="C-Level Panel", font=("Helvetica", 32, "bold"), pady=20, bg="#2196F3", fg="white")
title_label.pack(fill=tk.X)

# Create a label for the company data section heading
company_data_heading = tk.Label(frame, text="Company Data", font=("Helvetica", 16, "bold"), bg="#f2f2f2")
company_data_heading.pack(anchor="w", padx=10, pady=10)

# Create a listbox to display the company data with a vertical scrollbar
company_data_listbox = tk.Listbox(frame, height=5, width=60, font=("Helvetica", 12))
update_company_data_list()  # Update the list initially
company_data_listbox.pack(fill=tk.X, padx=10, pady=(0, 10))

# Create a vertical scrollbar for the company data listbox
company_data_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=company_data_listbox.yview)
company_data_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
company_data_listbox.config(yscrollcommand=company_data_scrollbar.set)

# Create a label for the open requirements section heading
open_requirements_heading = tk.Label(frame, text="Open Requirements", font=("Helvetica", 16, "bold"), bg="#f2f2f2")
open_requirements_heading.pack(anchor="w", padx=10, pady=10)

# Add a dummy requirement to the list
job_requirements.append("Dummy Requirement")

# Create a listbox to display the open requirements with a vertical scrollbar
open_requirements_listbox = tk.Listbox(frame, height=15, width=60, font=("Helvetica", 12))
update_job_requirements_list()  # Update the list initially
open_requirements_listbox.pack(fill=tk.BOTH, padx=10, pady=10)

# Create a vertical scrollbar for the open requirements listbox
open_requirements_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=open_requirements_listbox.yview)
open_requirements_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
open_requirements_listbox.config(yscrollcommand=open_requirements_scrollbar.set)

# Bind the function to open job requirement details to a double click event
open_requirements_listbox.bind("<Double-1>", open_job_requirement_details)

# Start the Tkinter main loop
root.mainloop()
