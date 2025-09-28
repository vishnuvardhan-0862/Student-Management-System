import tkinter as tk
from tkinter import ttk
from .data import students
from utils.messages import show_info

def view_students():
    """
    Displays a list of all students with their total marks, attendance, and exam eligibility.
    """
    if not students:
        show_info("Info", "No students found. Please add a student first.")
        return

    view_win = tk.Toplevel()
    view_win.title("All Students")
    view_win.geometry("800x400")
    view_win.configure(bg="#F0F8FF")

    # --- Treeview Styling ---
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", 
        background="#FFFFFF",
        foreground="#333333",
        rowheight=25,
        fieldbackground="#FFFFFF"
    )
    style.map('Treeview', background=[('selected', '#347083')])

    # Treeview Columns
    columns = ("ID", "Name", "Course", "Total Marks", "Attendance (%)", "Exam Eligible")
    tree = ttk.Treeview(view_win, columns=columns, show="headings")

    # Column Headings
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Course", text="Course")
    tree.heading("Total Marks", text="Total Marks")
    tree.heading("Attendance (%)", text="Attendance (%)")
    tree.heading("Exam Eligible", text="Exam Eligible")

    #Column Widths
    tree.column("ID", width=50, anchor=tk.CENTER)
    tree.column("Name", width=150)
    tree.column("Course", width=100, anchor=tk.CENTER)
    tree.column("Total Marks", width=100, anchor=tk.CENTER)
    tree.column("Attendance (%)", width=120, anchor=tk.CENTER)
    tree.column("Exam Eligible", width=120, anchor=tk.CENTER)
    
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    # Populating Data 
    for s in students:
        total_marks = sum(s["marks"].values())
        attendance = s.get("attendance", 0)
        eligibility = "Yes" if attendance >= 75 else "No"
        
        tree.insert("", "end", values=(s["id"], s["name"], s["course"], total_marks, f"{attendance}%", eligibility))
