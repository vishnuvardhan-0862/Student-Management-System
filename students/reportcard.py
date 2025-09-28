import tkinter as tk
from tkinter import simpledialog, ttk
from .data import students, SUBJECTS
from utils.messages import show_error

def generate_report_card():
    """
    Generates and displays a detailed report card for a specific student.
    """
    id_ = simpledialog.askinteger("Report Card", "Enter Student ID to generate report card:")
    if id_ is None: return

    student = None
    for s in students:
        if s['id'] == id_:
            student = s
            break
            
    if not student:
        show_error("Error", "Student not found.")
        return

    # Report Card Window 
    report_win = tk.Toplevel()
    report_win.title(f"Report Card - {student['name']}")
    report_win.geometry("500x600")
    report_win.configure(bg="#E6E6FA") # Lavender background

    # Header
    header_frame = tk.Frame(report_win, bg="#483D8B", padx=20, pady=20) # Dark Slate Blue
    header_frame.pack(fill="x")
    tk.Label(header_frame, text="STUDENT REPORT CARD", font=("Arial", 20, "bold"), fg="white", bg="#483D8B").pack()

    # Student Info 
    info_frame = tk.Frame(report_win, padx=20, pady=10, bg="#E6E6FA")
    info_frame.pack(fill="x")
    
    tk.Label(info_frame, text=f"Student Name: {student['name']}", font=("Arial", 12), bg="#E6E6FA").pack(anchor="w")
    tk.Label(info_frame, text=f"Student ID: {student['id']}", font=("Arial", 12), bg="#E6E6FA").pack(anchor="w")
    tk.Label(info_frame, text=f"Course: {student['course']}", font=("Arial", 12), bg="#E6E6FA").pack(anchor="w")

    # Separator 
    ttk.Separator(report_win, orient='horizontal').pack(fill='x', padx=20, pady=10)

    # Marks Details
    marks_frame = tk.Frame(report_win, padx=20, pady=10, bg="#E6E6FA")
    marks_frame.pack(fill="x")
    tk.Label(marks_frame, text="Academic Performance", font=("Arial", 14, "bold"), bg="#E6E6FA").pack(anchor="w", pady=(0, 10))
    
    total_marks = sum(student["marks"].values())
    max_marks = len(SUBJECTS) * 100
    percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0
    
    for subject, mark in student["marks"].items():
        tk.Label(marks_frame, text=f"{subject}: {mark} / 100", font=("Arial", 12), bg="#E6E6FA").pack(anchor="w")
    
    # Summary 
    summary_frame = tk.Frame(report_win, padx=20, pady=10, bg="#F0F8FF") # Alice Blue
    summary_frame.pack(fill="x", pady=20)
    
    tk.Label(summary_frame, text=f"Total Marks: {total_marks} / {max_marks}", font=("Arial", 12, "bold"), bg="#F0F8FF").pack(anchor="w")
    tk.Label(summary_frame, text=f"Percentage: {percentage:.2f}%", font=("Arial", 12, "bold"), bg="#F0F8FF").pack(anchor="w")

    # Attendance & Eligibility 
    attendance = student.get("attendance", 0)
    eligibility = "ELIGIBLE for Final Exam" if attendance >= 75 else "NOT ELIGIBLE for Final Exam"
    eligibility_color = "green" if attendance >= 75 else "red"
    
    tk.Label(summary_frame, text=f"Attendance: {attendance}%", font=("Arial", 12, "bold"), bg="#F0F8FF").pack(anchor="w", pady=(10,0))
    tk.Label(summary_frame, text=eligibility, font=("Arial", 14, "bold"), fg=eligibility_color, bg="#F0F8FF").pack(pady=10)
