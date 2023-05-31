import tkinter as tk
import json
from FAQ import FAQ
import customtkinter

class FAQManager():
    def __init__(self, root, filename='./컴퓨팅적사고/재직자전형소개프로그램/data/faq_data.json'):
        self.faqs = []
        self.current_faq_index = None
        self.root = root

        self.create_main_frame()
        self.create_main_widgets()
        self.create_button_frame()
        
        self.create_detail_frame()
        self.create_detail_widgets()
        self.create_details_button_frame()

        self.filename = filename
        self.load_data()

    def create_main_frame(self):
        self.main_frame = customtkinter.CTkFrame(self.root,fg_color="#222222")
        self.main_frame.pack(fill="both", expand=True)

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=30)
        self.main_frame.grid_rowconfigure(3, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=8)
        self.main_frame.grid_columnconfigure(2, weight=30)
        
    def create_main_widgets(self):
        self.main_frame.grid_columnconfigure(1, weight=1)
        
        self.title_label = customtkinter.CTkLabel(self.main_frame, text="질문:")
        self.title_label.grid(row=0, column=0, sticky='e')
        self.title_entry = customtkinter.CTkTextbox(self.main_frame, height=4)
        self.title_entry.grid(row=0, column=1, sticky='ew')

        self.contents_label = customtkinter.CTkLabel(self.main_frame, text="답변:")
        self.contents_label.grid(row=1, column=0, sticky='e')
        self.contents_entry = customtkinter.CTkTextbox(self.main_frame, height=4)
        self.contents_entry.grid(row=1, column=1, sticky='ew')

        self.create_button = customtkinter.CTkButton(self.main_frame, text="등록", command=self.create, height=2)
        self.create_button.grid(row=0, column=2, rowspan=2, sticky='nsew')

        self.listbox = customtkinter.CTkTextbox(self.main_frame)
        self.listbox.grid(row=2, column=0, columnspan=3, sticky="nsew")

    def create_button_frame(self):
        self.button_frame = customtkinter.CTkFrame(self.main_frame)
        self.button_frame.grid(row=3, column=0, columnspan=3)

        self.read_button = customtkinter.CTkButton(self.button_frame, text="조회", command=self.read)
        self.read_button.pack(side="left")

        self.delete_button = customtkinter.CTkButton(self.button_frame, text="삭제", command=self.delete)
        self.delete_button.pack(side="left")

    def create_detail_frame(self):
        self.details_frame = customtkinter.CTkFrame(self.root)
        self.details_frame.pack_forget()

        self.details_frame.grid_rowconfigure(0, weight=1)
        self.details_frame.grid_rowconfigure(1, weight=30)
        self.details_frame.grid_rowconfigure(2, weight=1)
        self.details_frame.grid_columnconfigure(0, weight=1)
        self.details_frame.grid_columnconfigure(1, weight=8)
        self.details_frame.grid_columnconfigure(2, weight=1)

    def create_detail_widgets(self):
        self.details_title_label = customtkinter.CTkLabel(self.details_frame, text="Title")
        self.details_title_label.grid(row=0, column=0, sticky='e')
        self.details_title_entry = customtkinter.CTkTextbox(self.details_frame, height=4)
        self.details_title_entry.grid(row=0, column=1, sticky='w')

        self.details_contents_label = customtkinter.CTkLabel(self.details_frame, text="Contents:")
        self.details_contents_label.grid(row=1, column=0, sticky='e')
        self.details_contents_entry = customtkinter.CTkTextbox(self.details_frame, height=40)
        self.details_contents_entry.grid(row=1, column=1, sticky='w')

    def create_details_button_frame(self):
        self.details_button_frame = customtkinter.CTkFrame(self.details_frame)
        self.details_button_frame.grid(row=3, column=0, columnspan=3)
    
        self.update_button = customtkinter.CTkButton(self.details_button_frame, text="수정", command=self.update)
        self.update_button.pack(side="left")

        self.back_button = customtkinter.CTkButton(self.details_button_frame, text="Back", command=self.back)
        self.back_button.pack(side="left")

    def create(self):
        title = self.title_entry.get("1.0", 'end').strip()
        contents = self.contents_entry.get("1.0", 'end').strip()

        if title and contents:
            faq = FAQ(title, contents)
            self.faqs.append(faq)
            self.current_faq_index = len(self.faqs) - 1
            self.save_data()
            self.update_ui()

    def read(self):
        self.current_faq_index = self.listbox.curselection()[0]
        faq = self.faqs[self.current_faq_index]

        self.details_title_entry.delete('1.0', 'end')
        self.details_title_entry.insert('1.0', faq.title)
        self.details_contents_entry.delete('1.0', 'end')
        self.details_contents_entry.insert('1.0', faq.contents)

        self.main_frame.pack_forget()
        self.details_frame.pack()

    def update(self):
        if self.current_faq_index is not None:
            updated_title = self.details_title_entry.get('1.0', 'end').strip()
            updated_contents = self.details_contents_entry.get('1.0', 'end').strip()

            self.faqs[self.current_faq_index].title = updated_title
            self.faqs[self.current_faq_index].contents = updated_contents

            self.save_data()
            self.update_ui()

    def delete(self):
        selection = self.listbox.curselection()

        if selection:
            index = selection[0]
            del self.faqs[index]

            if self.faqs:
                self.current_faq_index = 0
            else:
                self.current_faq_index = None

            self.save_data()
            self.update_ui()

    def back(self):
        self.details_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)

    def update_ui(self):
        self.listbox.delete(0, 'end')
        for faq in self.faqs:
            self.listbox.insert('end', faq.title)
        
        if self.current_faq_index is not None and self.current_faq_index < len(self.faqs):
            self.listbox.selection_set(self.current_faq_index)

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump([faq.__dict__ for faq in self.faqs], f)

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                self.faqs = [FAQ(**data) for data in json.load(f)]
                self.update_ui()
        except FileNotFoundError:
            pass