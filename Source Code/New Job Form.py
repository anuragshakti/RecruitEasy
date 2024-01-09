import tkinter as tk
import sqlite3
import re

def extract_skills(description):
    pattern = r'\b(?:java|python|sql|html|css|javascript)\b'  # Customize with more skills
    skills = re.findall(pattern, description, re.IGNORECASE)
    return skills

def submit_job():
    job_title = job_title_entry.get()
    location = location_entry.get()
    duration = duration_entry.get()
    rate = rate_entry.get()
    job_description = job_description_text.get("1.0", "end-1c")
    client = client_entry.get()
    selected_recruiters = assigned_to_var.get()  # Get selected recruiters

    skills = extract_skills(job_description)

    conn = sqlite3.connect("Recruitment.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS new_job_recruitment (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      job_title TEXT,
                      location TEXT,
                      duration TEXT,
                      rate REAL,
                      job_description TEXT,
                      client TEXT,
                      assigned_recruiter_name TEXT,
                      skills TEXT)''')  # Update the column name

    cursor.execute('''INSERT INTO new_job_recruitment (job_title, location, duration, rate, job_description, client, assigned_recruiter_name)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
                   (job_title, location, duration, rate, job_description, client, ', '.join(selected_recruiters)))  # Update the column name

    # Update recruiters' "assigned_requirements" in the "recruiters" table
    for recruiter in selected_recruiters:
        cursor.execute('''UPDATE recruiters SET assigned_requirements = assigned_requirements || ? WHERE name = ?''',
                       (', ' + job_title, recruiter))

    conn.commit()
    conn.close()

    job_title_entry.delete(0, "end")
    location_entry.delete(0, "end")
    duration_entry.delete(0, "end")
    rate_entry.delete(0, "end")
    job_description_text.delete("1.0", "end")
    client_entry.delete(0, "end")
    assigned_to_var.set([])  # Clear selected recruiters

root = tk.Tk()
root.title("Create A Requirement")  # Added a title
root.geometry("400x600")

title_label = tk.Label(root, text="Create A Requirement", font=("Helvetica", 16, "bold"), padx=10, pady=10)
title_label.grid(row=0, column=0, columnspan=2)

# Fetch the list of recruiters from the "recruiters" table
conn = sqlite3.connect("Recruitment.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM recruiters")
recruiters_list = [rec[0] for rec in cursor.fetchall()]
conn.close()

# Create form elements
job_title_label = tk.Label(root, text="Job Title:")
job_title_entry = tk.Entry(root)

location_label = tk.Label(root, text="Location:")
location_entry = tk.Entry(root)

duration_label = tk.Label(root, text="Duration:")
duration_entry = tk.Entry(root)

rate_label = tk.Label(root, text="Rate:")
rate_entry = tk.Entry(root)

job_description_label = tk.Label(root, text="Job Description:")
job_description_text = tk.Text(root, wrap=tk.WORD, width=30, height=5)

client_label = tk.Label(root, text="Client:")
client_entry = tk.Entry(root)

recruiters_label = tk.Label(root, text="Assign this to:")
assigned_to_var = tk.StringVar()
recruiters_dropdown = tk.Listbox(root, listvariable=assigned_to_var, selectmode=tk.MULTIPLE, height=3)
recruiters_dropdown.insert(0, *recruiters_list)  # Populate with recruiters

# Create buttons
submit_button = tk.Button(root, text="Submit", command=submit_job)

# Place form elements using the grid layout manager
job_title_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
job_title_entry.grid(row=1, column=1, padx=10, pady=5)
location_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
location_entry.grid(row=2, column=1, padx=10, pady=5)
duration_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
duration_entry.grid(row=3, column=1, padx=10, pady=5)
rate_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
rate_entry.grid(row=4, column=1, padx=10, pady=5)
job_description_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
job_description_text.grid(row=5, column=1, padx=10, pady=5)
client_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
client_entry.grid(row=6, column=1, padx=10, pady=5)
recruiters_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
recruiters_dropdown.grid(row=7, column=1, padx=10, pady=5)
submit_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()