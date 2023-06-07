import tkinter as tk
from QnA import QnA
import json
import customtkinter

class QnAManager():
    def __init__(self, root, filename='./comsaco/data/qna_data.json'):
        self.qnas = []
        self.current_qna_index = None
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
        self.main_frame = customtkinter.CTkFrame(self.root,width=800,height=600)
        self.main_frame.pack(expand=True)

        self.frame = customtkinter.CTkFrame(self.main_frame, width=800, height=600)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')
        # self.main_frame.grid_rowconfigure(0, weight=1)
        # self.main_frame.grid_rowconfigure(1, weight=1)
        # self.main_frame.grid_rowconfigure(2, weight=30)
        # self.main_frame.grid_rowconfigure(3, weight=1)
        # self.main_frame.grid_columnconfigure(0, weight=1)
        # self.main_frame.grid_columnconfigure(1, weight=8)
        # self.main_frame.grid_columnconfigure(2, weight=30)

    def create_main_widgets(self):
        self.question_label = customtkinter.CTkLabel(self.frame, text="질문:",padx=10, pady=10)
        self.question_label.grid(row=0, column=0, sticky='e',padx=10, pady=15)
        self.question_entry = customtkinter.CTkTextbox(self.frame, height=40, width=500,padx=10, pady=20)
        self.question_entry.grid(row=0, column=1, sticky='w',padx=10, pady=15)

        self.create_button = customtkinter.CTkButton(self.frame, text="등록",command=self.create,height=50,width=100)
        self.create_button.grid(row=0, column=2,columnspan = 2,padx=15)

        self.answer_label = customtkinter.CTkLabel(self.frame, text="답변:",padx=10, pady=10)
        self.answer_label.grid(row=1, column=0, sticky='e', padx=10, pady=15)
        self.answer_entry = customtkinter.CTkTextbox(self.frame, height=150, width=500,padx=10, pady=20)
        self.answer_entry.grid(row=1, column=1, sticky='w', padx=10, pady=15)

        self.listbox = tk.Listbox(self.frame,bg="#222222",fg="white",bd=0)
        self.listbox.grid(row=2, column=0, columnspan=3, sticky="nsew")

    def create_button_frame(self):
        self.button_frame = customtkinter.CTkFrame(self.frame)
        self.button_frame.grid(row=3, column=0, columnspan=3)

        self.read_button = customtkinter.CTkButton(self.button_frame, text="조회", command=self.read)
        self.read_button.grid(row=0, column=1, sticky='w')

        self.delete_button = customtkinter.CTkButton(self.button_frame, text="삭제", command=self.delete)
        self.delete_button.grid(row=0, column=3, sticky='w')


    def create_detail_frame(self):
        self.details_frame = customtkinter.CTkFrame(self.root,width=800,height=600)
        self.details_frame.pack(expand=True)
        self.details_frame.pack_forget()
        
        self.frame = customtkinter.CTkFrame(self.details_frame, width=800, height=600)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        # self.details_frame.grid_rowconfigure(0, weight=1)
        # self.details_frame.grid_rowconfigure(1, weight=30)
        # self.details_frame.grid_rowconfigure(2, weight=1)
        # self.details_frame.grid_columnconfigure(0, weight=1)
        # self.details_frame.grid_columnconfigure(1, weight=8)
        # self.details_frame.grid_columnconfigure(2, weight=30)

    def create_detail_widgets(self):
        self.details_question_label = customtkinter.CTkLabel(self.frame, text="질문",height=70,width=100)
        self.details_question_label.grid(row=0, column=0, sticky='e',padx=10,pady=10)
        self.details_question_entry = customtkinter.CTkTextbox(self.frame, height=200,width=500)
        self.details_question_entry.grid(row=0, column=1, sticky='e',padx=10,pady=10)

        self.details_answer_label = customtkinter.CTkLabel(self.frame, text="답변:",height=70,width=100)
        self.details_answer_label.grid(row=1, column=0, sticky='e',padx=10,pady=10)
        self.details_answer_entry = customtkinter.CTkTextbox(self.frame, height=200,width=500)
        self.details_answer_entry.grid(row=1, column=1,sticky='e',padx=10,pady=10)

    def create_details_button_frame(self):
        self.details_button_frame = customtkinter.CTkFrame(self.frame)
        self.details_button_frame.grid(row=3, column=0, columnspan=3)

        self.update_button = customtkinter.CTkButton(self.details_button_frame, text="수정", command=self.update)
        self.update_button.pack(side="left")

        self.back_button = customtkinter.CTkButton(self.details_button_frame, text="뒤로가기", command=self.back)
        self.back_button.pack(side="right")

    def create(self):
        question = self.question_entry.get("1.0", 'end').strip()  
        answer = self.answer_entry.get("1.0", 'end').strip()  

        if question and answer:
            qna = QnA(question, answer)
            self.qnas.append(qna)
            self.current_qna_index = len(self.qnas) - 1
            self.save_data()
            self.update_ui()

        self.question_entry.delete('1.0', 'end')
        self.question_entry.insert('1.0', '')
        self.answer_entry.delete('1.0', 'end')
        self.answer_entry.insert('1.0', '')

    def read(self):
        self.current_qna_index = self.listbox.curselection()[0]  
        qna = self.qnas[self.current_qna_index]

        self.details_question_entry.delete('1.0', 'end')
        self.details_question_entry.insert('1.0', qna.question)
        self.details_answer_entry.delete('1.0', 'end')
        self.details_answer_entry.insert('1.0', qna.answer)

        self.main_frame.pack_forget()
        self.details_frame.pack()

    def update(self):
        if self.current_qna_index is not None:
            updated_question = self.details_question_entry.get('1.0', 'end').strip()
            updated_answer = self.details_answer_entry.get('1.0', 'end').strip()

            self.qnas[self.current_qna_index].question = updated_question
            self.qnas[self.current_qna_index].answer = updated_answer

            self.save_data()
            self.update_ui()

    def delete(self):
        selection = self.listbox.curselection()

        if selection:
            index = selection[0]
            del self.qnas[index]

            if self.qnas:
                self.current_qna_index = 0
            else:
                self.current_qna_index = None

            self.save_data()
            self.update_ui()

    def back(self):
        self.details_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)

    def update_ui(self):
        self.listbox.delete(0, 'end')
        for qna in self.qnas:
            self.listbox.insert('end', qna.question)

        if self.current_qna_index is not None and self.current_qna_index < len(self.qnas):
            self.listbox.selection_set(self.current_qna_index)

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump([qna.__dict__ for qna in self.qnas], f)

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                self.qnas = [QnA(**data) for data in json.load(f)]
                self.update_ui()
        except FileNotFoundError:
            pass