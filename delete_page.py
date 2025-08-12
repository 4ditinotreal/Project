import tkinter as tk
from tkinter import messagebox

class DeletePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Delete Student Data", font=("Arial", 18, "bold")).pack(pady=20)

        tk.Label(self, text="Roll No:").pack()
        self.roll_entry = tk.Entry(self)
        self.roll_entry.pack()

        tk.Button(self, text="Delete", command=self.delete_data).pack(pady=10)
        tk.Button(self, text="Back", command=lambda: controller.show_frame("StudentDataPage")).pack()

    def delete_data(self):
        roll = self.roll_entry.get()
        if roll:
            messagebox.showinfo("Deleted", f"Student with Roll No {roll} deleted")
            self.roll_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Roll No is required")
        self.roll_entry.focus()
        self.controller.refresh_all()