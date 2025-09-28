from tkinter import simpledialog
from .data import students
from utils.messages import show_info, show_error

def search_student():
    """
    Searches for a student by ID or name and displays their detailed information.
    """
    query = simpledialog.askstring("Search", "Enter Student ID or Name to search:")
    if not query: return
    
    query = query.strip().lower()
    found_student = None
    
    for s in students:
        # Check by ID (string comparison) or by name (case-insensitive)
        if str(s["id"]) == query or s["name"].lower() == query:
            found_student = s
            break

    if found_student:
        marks_details = "\n".join([f"  - {subject}: {mark}" for subject, mark in found_student["marks"].items()])
        attendance = found_student.get("attendance", "N/A")
        
        info_message = (
            f"ID: {found_student['id']}\n"
            f"Name: {found_student['name']}\n"
            f"Course: {found_student['course']}\n"
            f"Attendance: {attendance}%\n\n"
            f"Marks:\n{marks_details}"
        )
        show_info("Student Found", info_message)
    else:
        show_error("Not Found", "Student not found.")
