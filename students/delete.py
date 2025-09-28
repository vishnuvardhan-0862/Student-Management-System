from tkinter import simpledialog, messagebox
from .data import students
from utils.messages import show_error, show_success

def delete_student():
    """
    Deletes a student record based on their ID.
    """
    id_ = simpledialog.askinteger("Delete", "Enter Student ID to delete:")
    if id_ is None: return

    student_to_delete = None
    for s in students:
        if s["id"] == id_:
            student_to_delete = s
            break
            
    if student_to_delete:
        # Confirmation dialog
        confirm = messagebox.askyesno(
            "Confirm Deletion", 
            f"Are you sure you want to delete {student_to_delete['name']}?"
        )
        if confirm:
            students.remove(student_to_delete)
            show_success("Deleted", f"Student {student_to_delete['name']} removed successfully!")
    else:
        show_error("Error", "Student not found.")
