import tkinter as tk
from tkinter import messagebox

class InsertPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Centered Heading
        tk.Label(self, text="Insert Student Data", font=("Arial", 18, "bold")).pack(pady=20)

        # Example form
        tk.Label(self, text="Name:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        tk.Label(self, text="Roll No:").pack()
        self.roll_entry = tk.Entry(self)
        self.roll_entry.pack()

        tk.Label(self, text="Course:").pack()
        self.course_entry = tk.Entry(self)
        self.course_entry.pack()

        tk.Button(self, text="Insert", command=self.insert_data).pack(pady=10)

        # Back button
        tk.Button(self, text="Back", command=lambda: controller.show_frame("StudentDataPage")).pack()

    def insert_data(self):
        name = self.name_entry.get()
        roll = self.roll_entry.get()
        course = self.course_entry.get()

        if name and roll and course:
            messagebox.showinfo("Success", f"Inserted {name} ({roll}) into {course}")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "All fields are required")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.roll_entry.delete(0, tk.END)
        self.course_entry.delete(0, tk.END)
        self.name_entry.focus()
        self.controller.refresh_all()