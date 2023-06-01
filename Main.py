import tkinter as tk
from QnAManager import QnAManager
from FAQManager import FAQManager
from SchoolManager import SchoolManager
from ChatManager import ChatManager
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class MainScreen:
    def __init__(self, root):
        self.root = root
        self.root.option_add("*Font", "돋움체 14")
        self.faq_manager = FAQManager(root)
        self.qna_manager = QnAManager(root)
        self.school_manager = SchoolManager(root)
        self.chat_manager = ChatManager(root)

        self.main_frame = customtkinter.CTkFrame(root)
        self.main_frame.pack(side="bottom", fill="x")

        self.faq_button = customtkinter.CTkButton(self.main_frame, text="학교정보", command=self.show_faq)
        self.faq_button.pack(side="left", fill="x", expand=True)

        self.qna_button = customtkinter.CTkButton(self.main_frame, text="QnA", command=self.show_qna)
        self.qna_button.pack(side="left", fill="x", expand=True)
        
        self.chat_button = customtkinter.CTkButton(self.main_frame, text="채팅", command=self.show_chat)
        self.chat_button.pack(side="left", fill="x", expand=True)

        self.show_faq() 

    def show_faq(self):
        self.hide_all()
        #self.faq_manager.main_frame.pack(fill="both", expand=True)
        self.school_manager.main_frame.pack(fill="both", expand=True)

    def show_qna(self):
        self.hide_all()
        self.qna_manager.main_frame.pack(fill="both", expand=True)
        
    def show_chat(self):
        self.hide_all()
        self.chat_manager.main_frame.pack(fill="both",expand=True)

    def hide_all(self):
        self.faq_manager.main_frame.pack_forget()
        self.qna_manager.main_frame.pack_forget()
        self.school_manager.main_frame.pack_forget()
        self.chat_manager.main_frame.pack_forget()
        
        self.faq_manager.details_frame.pack_forget()
        self.qna_manager.details_frame.pack_forget()
        
        self.school_manager.details_frame.pack_forget()
        #self.chat_manager.details_frame.pack_forget()

if __name__ == "__main__":
    root = customtkinter.CTk()
    root.title('재직자')
    root.geometry("820x600")
    root.minsize(00, 600)
    main_screen = MainScreen(root)

    root.mainloop()
    