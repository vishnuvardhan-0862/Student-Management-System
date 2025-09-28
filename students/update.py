from tkinter import simpledialog
from .data import students, COURSES, SUBJECTS
from utils.messages import show_info, show_error

def update_student():
    """
    Updates a student's course, subject marks, or attendance.
    """
    id_ = simpledialog.askinteger("Update", "Enter Student ID to update:")
    if id_ is None: return

    student_to_update = None
    for s in students:
        if s["id"] == id_:
            student_to_update = s
            break
            
    if not student_to_update:
        show_error("Error", "Student not found.")
        return

    # Update Choice
    choice = simpledialog.askstring("Choice", "What to update? (Course/Marks/Attendance)").strip().lower()

    if choice == "course":
        course_options = ", ".join(COURSES)
        new_course = simpledialog.askstring("Input", f"Enter new Course ({course_options}):").strip().upper()
        if new_course in COURSES:
            student_to_update["course"] = new_course
            show_info("Success", "Course updated successfully!")
        else:
            show_error("Error", f"Invalid course! Choose from {course_options}")

    elif choice == "marks":
        subject_options = ", ".join(SUBJECTS)
        subject_to_update = simpledialog.askstring("Input", f"Which subject to update? ({subject_options}):").strip().title()
        if subject_to_update in SUBJECTS:
            new_marks = simpledialog.askinteger("Input", f"Enter new marks for {subject_to_update}:")
            if new_marks is not None:
                student_to_update["marks"][subject_to_update] = new_marks
                show_info("Success", "Marks updated successfully!")
        else:
            show_error("Error", "Invalid subject entered.")

    elif choice == "attendance":
        new_attendance = simpledialog.askinteger("Input", "Enter new attendance percentage:")
        if new_attendance is not None:
            student_to_update["attendance"] = new_attendance
            show_info("Success", "Attendance updated successfully!")
    else:
        show_error("Error", "Invalid choice. Please enter 'Course', 'Marks', or 'Attendance'.")
