import tkinter as tk
from tkinter import ttk

class ViewPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="View Student Data", font=("Arial", 18, "bold")).pack(pady=20)

        # Table
        columns = ("Roll No", "Name", "Course")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10)

        # Example static data
        students = [
            (1, "Aditi", "Computer Engineering"),
            (2, "Sahil", "IT"),
            (3, "Tanaya", "AI")
        ]
        for student in students:
            self.tree.insert("", tk.END, values=student)

        tk.Button(self, text="Refresh", command=self.refresh_table).pack(pady=5)
        tk.Button(self, text="Back", command=lambda: controller.show_frame("StudentDataPage")).pack()

    def refresh_table(self):
        # Example refresh (just clears and re-adds same data)
        for row in self.tree.get_children():
            self.tree.delete(row)

        students = [
            (1, "Aditi", "Computer Engineering"),
            (2, "Sahil", "IT"),
            (3, "Tanaya", "AI")
        ]
        for student in students:
            self.tree.insert("", tk.END, values=student)
        self.controller.refresh_all()
        self.tree.focus_set()  # Set focus back to the treeview