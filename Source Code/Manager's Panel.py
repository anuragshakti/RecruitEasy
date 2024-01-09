import tkinter as tk
from tkinter import messagebox
import subprocess
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect("recruitment.db")
cursor = conn.cursor()

# Initialize empty list for job requirements
requirements_list = [{"Job Title": "dummy requirement"}]  # Add the dummy requirement

# Function to add a new job requirement
def add_requirement():
    job_title = job_title_entry.get()
    
    # Add the job requirement to the database
    cursor.execute("INSERT INTO job_recruitment (job_title) VALUES (?)", (job_title,))
    conn.commit()
    
    # Add code to save the requirement to the database or perform other actions
    # For this example, we'll just add it to the requirements list
    requirement = {"Job Title": job_title}
    requirements_list.append(requirement)
    update_requirements_list()

    # Clear the input field
    job_title_entry.delete(0, tk.END)

# Function to update the requirements list display
def update_requirements_list():
    cursor.execute("SELECT job_title FROM job_recruitment")
    requirements_data = cursor.fetchall()
    requirements_listbox.delete(0, tk.END)  # Clear the listbox
    for requirement in requirements_data:
        requirements_listbox.insert(tk.END, requirement[0])

# Function to open details of a job requirement
def open_requirement_details(event):
    selected_index = requirements_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        requirement_name = requirements_listbox.get(index)
        
        # Open "Job Description.py" with the selected job title as a command-line argument
        subprocess.Popen(["python", "Job Description.py", requirement_name])

# Function to add a new recruiter
def add_recruiter():
    recruiter_name = recruiter_name_entry.get()
    
    # Add the recruiter to the database
    cursor.execute("INSERT INTO recruiters (name) VALUES (?)", (recruiter_name,))
    conn.commit()

    # Update the recruiters list
    update_recruiters_list()

    # Clear the input field
    recruiter_name_entry.delete(0, tk.END)

# Function to update the recruiter list display
def update_recruiters_list():
    cursor.execute("SELECT name FROM recruiters")
    recruiter_data = cursor.fetchall()
    recruiter_listbox.delete(0, tk.END)  # Clear the listbox
    for recruiter in recruiter_data:
        recruiter_listbox.insert(tk.END, recruiter[0])

# Function to open details of a recruiter
def open_recruiter_details(event):
    selected_index = recruiter_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        recruiter_name = recruiter_listbox.get(index)
        # You can display the details of the selected recruiter here
        messagebox.showinfo("Recruiter Details", "Name: " + recruiter_name)
        # Open "Recruiter's Personal Details.py" when the dummy recruiter is clicked
        if recruiter_name == "dummy recruiter":
            subprocess.Popen(["python", "Recruiter's Personal Details.py"])

# Function to open the "New Job Form.py" script
def open_new_job_form():
    subprocess.Popen(["python", "New Job Form.py"])

# Function to open the "Recruiter Form.py" script
def open_recruiter_form():
    subprocess.Popen(["python", "Recruiter Form.py"])

# Create the main window
root = tk.Tk()
root.title("Manager's Panel")

# Set the window size
root.geometry("800x600")  # Adjust the size as needed

# Create and place widgets
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Create a title label for "Manager's Panel"
title_label = tk.Label(frame, text="Manager's Panel", font=("Helvetica", 24, "bold"), pady=10)
title_label.grid(row=0, column=0, columnspan=4)

# Create a label for the requirements section heading
requirements_heading = tk.Label(frame, text="Requirements", font=("Helvetica", 16, "bold"))

# Create a label for the recruiters section heading
recruiters_heading = tk.Label(frame, text="Recruiters", font=("Helvetica", 16, "bold"))

# Create a listbox to display the requirements
requirements_listbox = tk.Listbox(frame, height=10, width=60)
update_requirements_list()  # Update the list initially

# Create a listbox to display the recruiters
recruiter_listbox = tk.Listbox(frame, height=10, width=60)
update_recruiters_list()  # Update the list initially

# Bind double-click event to listboxes to open details
requirements_listbox.bind("<Double-Button-1>", open_requirement_details)
recruiter_listbox.bind("<Double-Button-1>", open_recruiter_details)

# Create a button to add a new job requirement and open the form
add_requirement_button = tk.Button(frame, text="Add Job Description", command=open_new_job_form)

# Create a button to add a new recruiter and open the recruiter form
add_recruiter_button = tk.Button(frame, text="Add Recruiter", command=open_recruiter_form)

# Grid layout for widgets
requirements_heading.grid(row=1, column=0, columnspan=2, pady=10)
recruiters_heading.grid(row=1, column=2, columnspan=2, pady=10)
requirements_listbox.grid(row=2, column=0, columnspan=2)
recruiter_listbox.grid(row=2, column=2, columnspan=2)
add_requirement_button.grid(row=3, column=0, columnspan=2, pady=10)
add_recruiter_button.grid(row=3, column=2, columnspan=2, pady=10)

# Start the Tkinter main loop
root.mainloop()

# Close the database connection when the application is closed
conn.close()