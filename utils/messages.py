
from tkinter import messagebox

def show_info(title, message):
    """Displays an information message box."""
    messagebox.showinfo(title, message)

def show_error(title, message):
    """Displays an error message box."""
    messagebox.showerror(title, message)

def show_success(title, message):
    """Displays a success message box (using info style)."""
    messagebox.showinfo(title, message)
