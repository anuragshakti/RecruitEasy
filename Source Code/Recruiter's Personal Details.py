import tkinter as tk
import sqlite3

# Function to display recruiter's details and assigned requirements
def display_recruiter_details(name):
    recruiter = get_recruiter_details(name)
    if recruiter:
        name_label.config(text=f"Name: {recruiter['name']}")
        email_label.config(text=f"Email: {recruiter['email']}")
        employee_id_label.config(text=f"Employee ID: {recruiter['employee_id']}")
        salary_label.config(text=f"Salary: {recruiter['salary']}")
        recruiter_type_label.config(text=f"Recruiter Type: {recruiter['recruiter_type']}")
        skills_expertise_label.config(text=f"Skills Expertise: {recruiter['skills_expertise']}")
        display_assigned_requirements(name)  # Call this function to display assigned requirements
    else:
        # Set labels to "None"
        name_label.config(text="Name: None")
        email_label.config(text="Email: None")
        employee_id_label.config(text="Employee ID: None")
        salary_label.config(text="Salary: None")
        recruiter_type_label.config(text="Recruiter Type: None")
        assigned_requirements_label.config(text="Assigned Requirements: None")
        assigned_requirements_list.delete(0, tk.END)  # Clear the list
        skills_expertise_label.config(text="Skills Expertise: None")

# Function to display assigned requirements for a specific recruiter
def display_assigned_requirements(name):
    assigned_requirements = get_assigned_requirements(name)
    assigned_requirements_list.delete(0, tk.END)  # Clear the list
    for req in assigned_requirements:
        assigned_requirements_list.insert(tk.END, req)

# Function to fetch assigned requirements for a specific recruiter from the database
def get_assigned_requirements(name):
    conn = sqlite3.connect("Recruitment.db")
    cursor = conn.cursor()
    cursor.execute("SELECT assigned_requirements FROM recruiters WHERE name=?", (name,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0].split(', ')
    else:
        return []

# Function to fetch recruiter's details from the database
def get_recruiter_details(name):
    conn = sqlite3.connect("Recruitment.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recruiters WHERE name=?", (name,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return {
            'name': result[1],
            'email': result[2],
            'employee_id': result[3],
            'salary': result[4],
            'recruiter_type': result[5],
            'assigned_requirements': result[6],
            'skills_expertise': result[7]
        }
    else:
        return None

# Function to fetch the list of recruiters from the database
def get_recruiters_from_db():
    conn = sqlite3.connect("Recruitment.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM recruiters")
    recruiters = [row[0] for row in cursor.fetchall()]
    conn.close()
    return recruiters

# Create the main window
root = tk.Tk()
root.title("Recruiter's Personal Details")
root.geometry("600x500")
root.configure(bg="#e6f7ff")

# Create a frame for personal details
details_frame = tk.Frame(root, padx=20, pady=20, bg="#66b3ff")
details_frame.pack()

# Add a label for the page heading
heading_label = tk.Label(details_frame, text="Recruiter's Personal Details", font=("Helvetica", 16), bg="#66b3ff", fg="white")
heading_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Add labels to display the recruiter's details with "None" as the initial text
name_label = tk.Label(details_frame, text="Name: None", font=("Helvetica", 12), bg="#66b3ff")
email_label = tk.Label(details_frame, text="Email: None", font=("Helvetica", 12), bg="#66b3ff")
employee_id_label = tk.Label(details_frame, text="Employee ID: None", font=("Helvetica", 12), bg="#66b3ff")
salary_label = tk.Label(details_frame, text="Salary: None", font=("Helvetica", 12), bg="#66b3ff")
recruiter_type_label = tk.Label(details_frame, text="Recruiter Type: None", font=("Helvetica", 12), bg="#66b3ff")

assigned_requirements_label = tk.Label(details_frame, text="Assigned Requirements: None", font=("Helvetica", 12), bg="#66b3ff")
assigned_requirements_list = tk.Listbox(details_frame, height=3, width=30, font=("Helvetica", 12))

skills_expertise_label = tk.Label(details_frame, text="Skills Expertise: None", font=("Helvetica", 12), bg="#66b3ff")

name_label.grid(row=1, column=0, sticky="w")
email_label.grid(row=2, column=0, sticky="w")
employee_id_label.grid(row=3, column=0, sticky="w")
salary_label.grid(row=4, column=0, sticky="w")
recruiter_type_label.grid(row=5, column=0, sticky="w")

assigned_requirements_label.grid(row=6, column=0, pady=(20, 0))
assigned_requirements_list.grid(row=7, column=0, padx=10)

skills_expertise_label.grid(row=8, column=0, pady=(20, 0))

# Add a dropdown menu to select a recruiter and display their details
recruiter_var = tk.StringVar()
recruiter_var.set("Anurag")  # Default recruiter
recruiters = get_recruiters_from_db()  # Get the list of recruiters from the database

recruiter_dropdown = tk.OptionMenu(details_frame, recruiter_var, *recruiters, command=lambda name: display_recruiter_details(name))
recruiter_dropdown.grid(row=9, column=0, pady=10)

# Call the display_recruiter_details function to display details for the default recruiter
display_recruiter_details(recruiter_var.get())

# Start the Tkinter main loop
root.mainloop()