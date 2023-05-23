import tkinter as tk
from QnAManager import QnAManager
from FAQManager import FAQManager

class SchoolInfo:
    def __init__(self, university_name, department, location, employment_obligation, admission_link, image_path):
        self.university_name = university_name
        self.department = department
        self.location = location
        self.employment_obligation = employment_obligation
        self.admission_link = admission_link
        self.image_path = image_path

class MainScreen:
    def __init__(self, root):
        self.root = root
        
        self.faq_manager = FAQManager(root)
        self.qna_manager = QnAManager(root)

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(side="bottom", fill="x")

        self.faq_button = tk.Button(self.main_frame, text="FAQ Manager", command=self.show_faq)
        self.faq_button.pack(side="left", fill="x", expand=True)

        self.qna_button = tk.Button(self.main_frame, text="QnA Manager", command=self.show_qna)
        self.qna_button.pack(side="left", fill="x", expand=True)

        self.show_faq() 

    def show_faq(self):
        self.hide_all()
        self.faq_manager.main_frame.pack(fill="both", expand=True)

    def show_qna(self):
        self.hide_all()
        self.qna_manager.main_frame.pack(fill="both", expand=True)

    def hide_all(self):
        self.faq_manager.main_frame.pack_forget()
        self.qna_manager.main_frame.pack_forget()
        self.faq_manager.details_frame.pack_forget()
        self.qna_manager.details_frame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.minsize(800, 600)

    main_screen = MainScreen(root)

    root.mainloop()