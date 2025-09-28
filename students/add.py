from tkinter import simpledialog
from .data import students, COURSES, MAX_STUDENTS, SUBJECTS
from utils.messages import show_error, show_success

def add_student():
    """
    Adds a new student with details including ID, name, course, subject-wise marks, and attendance.
    """
    if len(students) >= MAX_STUDENTS:
        show_error("Error", f"Maximum {MAX_STUDENTS} students allowed!")
        return

    # Student ID
    id_ = simpledialog.askinteger("Input - Step 1 of 4", "Enter Student ID:")
    if id_ is None: return
    if any(s['id'] == id_ for s in students):
        show_error("Error", "Student ID already exists!")
        return

    # Student Name 
    name = simpledialog.askstring("Input - Step 2 of 4", "Enter Student Name:")
    if not name: return

    # Course Selection (Case-Insensitive) 
    course_options = ", ".join(COURSES)
    course = simpledialog.askstring("Input - Step 3 of 4", f"Enter Course ({course_options}):")
    if not course: return
    
    valid_courses = {c.lower(): c for c in COURSES}
    course_lower = course.strip().lower()

    if course_lower not in valid_courses:
        show_error("Error", f"Invalid course! Please choose from {course_options}")
        return
    
    course = valid_courses[course_lower]

    # Subject Marks
    marks = {}
    for subject in SUBJECTS:
        mark = simpledialog.askinteger("Input - Step 4 of 4", f"Enter marks for {subject}:")
        if mark is None: return
        marks[subject] = mark
        
    # Attendance 
    attendance = simpledialog.askinteger("Input", "Enter Attendance Percentage:")
    if attendance is None: return


    students.append({
        "id": id_, 
        "name": name, 
        "course": course, 
        "marks": marks,
        "attendance": attendance
    })
    show_success("Success", f"Student {name} added successfully!")
