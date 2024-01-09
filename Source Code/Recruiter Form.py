import tkinter as tk
import tkinter.messagebox as messagebox
import sqlite3

def add_recruiter_to_database():
    name = name_entry.get()
    email = email_entry.get()
    employee_id = employee_id_entry.get()
    salary = salary_entry.get()
    recruiter_type = recruiter_type_entry.get()

    conn = sqlite3.connect("recruitment.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS recruiters (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      email TEXT,
                      employee_id TEXT,
                      salary REAL,
                      recruiter_type TEXT)''')

    cursor.execute("INSERT INTO recruiters (name, email, employee_id, salary, recruiter_type) VALUES (?, ?, ?, ?, ?)",
                   (name, email, employee_id, salary, recruiter_type))

    conn.commit()
    conn.close()

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    employee_id_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)
    recruiter_type_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Recruiter created successfully!")

root = tk.Tk()
root.title("Add Recruiter")
root.geometry("400x400")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

title_label = tk.Label(frame, text="Add Recruiter", font=("Helvetica", 18, "bold"), pady=10)
title_label.grid(row=0, column=0, columnspan=2)

name_label = tk.Label(frame, text="Name:")
name_entry = tk.Entry(frame)
email_label = tk.Label(frame, text="Email:")
email_entry = tk.Entry(frame)
employee_id_label = tk.Label(frame, text="Employee ID:")
employee_id_entry = tk.Entry(frame)
salary_label = tk.Label(frame, text="Salary:")
salary_entry = tk.Entry(frame)
recruiter_type_label = tk.Label(frame, text="Recruiter Type:")
recruiter_type_entry = tk.Entry(frame)

name_label.grid(row=1, column=0, padx=10, pady=5)
name_entry.grid(row=1, column=1, padx=10, pady=5)
email_label.grid(row=2, column=0, padx=10, pady=5)
email_entry.grid(row=2, column=1, padx=10, pady=5)
employee_id_label.grid(row=3, column=0, padx=10, pady=5)
employee_id_entry.grid(row=3, column=1, padx=10, pady=5)
salary_label.grid(row=4, column=0, padx=10, pady=5)
salary_entry.grid(row=4, column=1, padx=10, pady=5)
recruiter_type_label.grid(row=5, column=0, padx=10, pady=5)
recruiter_type_entry.grid(row=5, column=1, padx=10, pady=5)

submit_button = tk.Button(frame, text="Submit", command=add_recruiter_to_database)
submit_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()