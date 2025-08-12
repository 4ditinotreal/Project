import tkinter as tk

class StudentDataPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Centered Heading
        tk.Label(self, text="Student Data Menu", font=("Arial", 18, "bold")).pack(pady=20)

        # Buttons for navigation
        tk.Button(self, text="Insert Data", width=20, command=lambda: controller.show_frame("InsertPage")).pack(pady=5)
        tk.Button(self, text="Update Data", width=20, command=lambda: controller.show_frame("UpdatePage")).pack(pady=5)
        tk.Button(self, text="Delete Data", width=20, command=lambda: controller.show_frame("DeletePage")).pack(pady=5)
        tk.Button(self, text="View Data", width=20, command=lambda: controller.show_frame("ViewPage")).pack(pady=5)
        
        # Logout button
        tk.Button(self, text="Logout", width=20, command=lambda: controller.show_frame("LoginPage")).pack(pady=20)
