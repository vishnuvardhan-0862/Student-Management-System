import tkinter as tk
from students.add import add_student
from students.view import view_students
from students.search import search_student
from students.update import update_student
from students.delete import delete_student
from students.reportcard import generate_report_card

def run_app():
    """
    Initializes and runs the main application window.
    """
    root = tk.Tk()
    root.title("Student Management System")
    root.geometry("500x550")
    root.configure(bg="#ADD8E6")    # Light blue background

    # Title Label
    title_label = tk.Label(
        root, 
        text="Student Management System", 
        font=("Helvetica", 20, "bold"), 
        bg="#4682B4",    # Steel blue
        fg="white",
        pady=15
    )
    title_label.pack(fill="x")

    #  Button Frame 
    btn_frame = tk.Frame(root, bg="#ADD8E6", pady=20)
    btn_frame.pack()

    #  Button Styling
    button_font = ("Arial", 12)
    button_width = 25
    button_pady = 8
    
    button_config = {
        'width': button_width,
        'font': button_font,
        'bg': '#87CEEB', # Sky Blue
        'fg': '#000000', # Black
        'relief': 'raised',
        'borderwidth': 2
    }

    # Menu Buttons
    tk.Button(btn_frame, text="Add Student", command=add_student, **button_config).pack(pady=button_pady)
    tk.Button(btn_frame, text="View All Students", command=view_students, **button_config).pack(pady=button_pady)
    tk.Button(btn_frame, text="Search for Student", command=search_student, **button_config).pack(pady=button_pady)
    tk.Button(btn_frame, text="Update Student Info", command=update_student, **button_config).pack(pady=button_pady)
    tk.Button(btn_frame, text="Delete Student", command=delete_student, **button_config).pack(pady=button_pady)
    tk.Button(btn_frame, text="Generate Report Card", command=generate_report_card, **button_config).pack(pady=button_pady)
    
    # Exit Button 
    tk.Button(
        btn_frame, 
        text="Exit Application", 
        command=root.destroy,
        width=button_width,
        font=button_font,
        bg="#FF6347", # Tomato Red
        fg="white",
        relief='raised',
        borderwidth=2
    ).pack(pady=20) 

    root.mainloop()