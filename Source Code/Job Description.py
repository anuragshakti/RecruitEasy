import tkinter as tk
from tkinter import ttk
import sqlite3

def submit_candidate():
    # Your candidate submission logic here
    pass

def load_job_requirements(job_title):
    conn = sqlite3.connect("Recruitment.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM new_job_recruitment WHERE job_title = ?", (job_title,))
    job_data = cursor.fetchone()
    if job_data:
        for i in range(len(job_data)):
            if i < len(entry_fields):
                entry_fields[i].config(state='normal')
                entry_fields[i].delete(0, tk.END)
                entry_fields[i].insert(0, job_data[i])
                entry_fields[i].config(state='disabled')

    conn.close()

    # Update the window title with the selected job title
    root.title(f"Job Requirements Details - {job_title}")

def on_job_title_selected(*args):
    selected_job_title = job_title_var.get()
    load_job_requirements(selected_job_title)

root = tk.Tk()
root.title("Job Requirements Details")
root.geometry("600x600")

canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

details_frame = tk.Frame(canvas, padx=20, pady=20, bg="#F3F4F6")
canvas.create_window((0, 0), window=details_frame, anchor="nw")

title_label = tk.Label(details_frame, text="Job Requirements Details", font=("Helvetica", 18), bg="#3498db", fg="white", padx=10, pady=10)
title_label.grid(row=0, column=0, columnspan=2, sticky="ew")

job_title_label = tk.Label(details_frame, text="Job Title:")
job_title_label.grid(row=1, column=0, sticky="w")

conn = sqlite3.connect("Recruitment.db")
cursor = conn.cursor()
cursor.execute("SELECT job_title FROM new_job_recruitment")
job_titles = [row[0] for row in cursor.fetchall()]
conn.close()

job_title_var = tk.StringVar()
job_title_var.set(job_titles[0])

job_title_dropdown = tk.OptionMenu(details_frame, job_title_var, *job_titles)
job_title_dropdown.grid(row=1, column=1)
job_title_var.trace("w", on_job_title_selected)

# Create labels and entry fields for all fields
field_labels = [
    "Location:", "Duration:", "Rate:", "Job Description:", "Client:", "Assigned Recruiter:", "Skills:"
]

entry_fields = []

for i, field_label in enumerate(field_labels):
    label = tk.Label(details_frame, text=field_label)
    label.grid(row=i + 2, column=0, sticky="w")

    entry = tk.Entry(details_frame, state='disabled')
    entry.grid(row=i + 2, column=1, padx=10, pady=5, sticky="w")
    entry_fields.append(entry)

# Load the default job description
load_job_requirements(job_titles[0])

# Create a frame for candidate submission
submission_frame = tk.Frame(details_frame, padx=20, pady=20, bg="#F3F4F6")
submission_frame.grid(row=len(field_labels) + 2, column=0, columnspan=2, sticky="ew")

# Add labels and entry fields for candidate submission
candidate_name_label = tk.Label(submission_frame, text="Candidate Name:")
candidate_phone_label = tk.Label(submission_frame, text="Phone Number:")
candidate_email_label = tk.Label(submission_frame, text="Email:")
visa_label = tk.Label(submission_frame, text="Visa Allowed:")
pay_rate_label = tk.Label(submission_frame, text="Pay Rate:")
skills_label = tk.Label(submission_frame, text="Skills:")

candidate_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
candidate_phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
candidate_email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
visa_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
pay_rate_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
skills_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

# Entry fields for candidate submission
candidate_name_entry = tk.Entry(submission_frame)
candidate_phone_entry = tk.Entry(submission_frame)
candidate_email_entry = tk.Entry(submission_frame)
visa_entry = tk.Entry(submission_frame, bg="white")
pay_rate_entry = tk.Entry(submission_frame)

candidate_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
candidate_phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
candidate_email_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
visa_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")
pay_rate_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Create checkboxes for skills
skills = ["Python", "Java", "C++", "JavaScript"]
skill_vars = [tk.IntVar() for _ in skills]
skill_checkboxes = [tk.Checkbutton(submission_frame, text=skill, variable=var, bg="#F3F4F6") for skill, var in zip(skills, skill_vars)]

for i, checkbox in enumerate(skill_checkboxes):
    checkbox.grid(row=5, column=i+1, sticky="w")

# Add a button to submit the candidate
submit_button = tk.Button(submission_frame, text="Submit Candidate", command=submit_candidate, bg="#3498db", fg="white")
submit_button.grid(row=6, columnspan=2, pady=10)

# Create a listbox to display submitted candidates
candidates_label = tk.Label(submission_frame, text="Submitted Candidates:", bg="#F3F4F6")
candidates_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")

submitted_candidates_listbox = tk.Listbox(submission_frame, selectmode=tk.SINGLE, width=40, height=5)
submitted_candidates_listbox.grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Set the window title dynamically based on the job title
job_title = job_titles[0]
root.title(f"Job Requirements Details - {job_title}")

# Update the canvas scroll region when the frame size changes
def configure_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", configure_scroll_region)

# Start the Tkinter main loop
root.mainloop()