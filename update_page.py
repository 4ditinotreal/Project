import tkinter as tk
from tkinter import messagebox

class UpdatePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Update Student Data", font=("Arial", 18, "bold")).pack(pady=20)

        tk.Label(self, text="Roll No:").pack()
        self.roll_entry = tk.Entry(self)
        self.roll_entry.pack()

        tk.Label(self, text="New Name:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        tk.Label(self, text="New Course:").pack()
        self.course_entry = tk.Entry(self)
        self.course_entry.pack()

        tk.Button(self, text="Update", command=self.update_data).pack(pady=10)
        tk.Button(self, text="Back", command=lambda: controller.show_frame("StudentDataPage")).pack()

    def update_data(self):
        roll = self.roll_entry.get()
        name = self.name_entry.get()
        course = self.course_entry.get()

        if roll and (name or course):
            messagebox.showinfo("Success", f"Updated Roll No {roll}")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Roll No and at least one field are required")

    def clear_entries(self):
        self.roll_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.course_entry.delete(0, tk.END)
        self.roll_entry.focus()
        self.controller.refresh_all()