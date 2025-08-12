import tkinter as tk
from pages.login_page import LoginPage
from pages.student_data_page import StudentDataPage
from pages.insert_page import InsertPage
from pages.update_page import UpdatePage
from pages.delete_page import DeletePage
from pages.view_page import ViewPage

class StudentManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Management System")
        self.geometry("800x500")

        self.frames = {}
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        for F in (LoginPage, StudentDataPage, InsertPage, UpdatePage, DeletePage, ViewPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = StudentManagementSystem()
    app.mainloop()
