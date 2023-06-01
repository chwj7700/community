import tkinter as tk
import json
from School import School
import tkinter as tk
from PIL import ImageTk, Image
from os import path
from functools import partial
import customtkinter

class SchoolManager():
    def __init__(self, root, filename='C:/workspace/comsaco/data/school_data.json'):
        self.root = root
        self.schools = []
        self.basePath = path.dirname(path.realpath(__file__))
        self.schoolDict = []
        
        self.filename = filename
        self.load_data()
        self.create_main_frame()
        self.create_detail_frame()
        self.create_detail_widgets()
        self.create_details_button_frame()
        
    def create_main_frame(self):
        # Variables
        column, row = 0, 0
        columnCnt = 3

        # Create frame
        self.main_frame = customtkinter.CTkFrame(self.root,bg_color="#222222",fg_color="#222222",border_color="#222222")
        self.main_frame.pack()

        # Create buttons with logos for each school
        for school in self.schools:
            # Variables
            schoolCnt = column + row * columnCnt
            logoPath = school.logoPath
            name = school.name

            # Create and configure logo
            logoImage = Image.open(self.basePath + logoPath)
            logoImage = logoImage.resize((259, 250), Image.ANTIALIAS)
            logo = ImageTk.PhotoImage(logoImage)

            # Create and pack canvas
            canvas = customtkinter.CTkFrame(self.main_frame)
            canvas.grid(column=column, row=row)

            # Create and pack button
            button = customtkinter.CTkButton(canvas, command=partial(self.read, schoolCnt), image=logo,text="",fg_color="#222222")
            button.pack()

            # Create and pack label
            customtkinter.CTkLabel(canvas, text=name).pack()

            # Update column and row counters
            column += 1
            if column >= columnCnt: 
                column = 0
                row += 1
    
    def create_detail_frame(self):
        self.details_frame = customtkinter.CTkFrame(self.root,width=800,height=600)
        self.details_frame.pack(expand=True)
        self.details_frame.pack_forget()

        self.frame = customtkinter.CTkFrame(self.details_frame, width=800, height=600)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

    # self.details_frame.grid_rowconfigure(0, weight=1)
    # self.details_frame.grid_rowconfigure(1, weight=1)
    # self.details_frame.grid_rowconfigure(2, weight=1)
    # self.details_frame.grid_rowconfigure(3, weight=1)
    # self.details_frame.grid_rowconfigure(4, weight=1)
    # self.details_frame.grid_rowconfigure(5, weight=1)
    # self.details_frame.grid_columnconfigure(0, weight=1)
    # self.details_frame.grid_columnconfigure(1, weight=8)
    # self.details_frame.grid_columnconfigure(2, weight=30)

    def create_detail_widgets(self):
        fields = [('학교명', 'name'), ('학과', 'department'), ('재직의무', 'obligation'), 
                ('입학처 링크', 'link'), ('위치', 'location')]
        for i, (label_text, entry_var) in enumerate(fields):
            label = customtkinter.CTkLabel(self.frame, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=10, sticky='e') # padding added
            entry = customtkinter.CTkTextbox(self.frame, height=20 if label_text == '학교명' or label_text == '위치' else 2, width=100) # Adjusted height and width
            entry.grid(row=i, column=1, padx=10, pady=10, sticky='ew') # Adjusted 'sticky' parameter for horizontal expansion
            setattr(self, 'details_' + entry_var + '_entry', entry)

    
    
    def create_details_button_frame(self):
        self.details_button_frame = customtkinter.CTkFrame(self.frame)
        self.details_button_frame.grid()

        self.back_button = customtkinter.CTkButton(self.details_button_frame, text="뒤로가기", command=self.back)
        self.back_button.grid(row=0, column=0, padx=10, pady=10, sticky='w')

    def back(self):
        self.details_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)

    def read(self, index):

        school = self.schools[index]

        self.details_name_entry.configure(state='normal')
        self.details_department_entry.configure(state='normal')
        self.details_location_entry.configure(state='normal')
        self.details_obligation_entry.configure(state='normal')
        self.details_link_entry.configure(state='normal')

        self.details_name_entry.delete('1.0', 'end')
        self.details_department_entry.delete('1.0', 'end')
        self.details_location_entry.delete('1.0', 'end')
        self.details_obligation_entry.delete('1.0', 'end')
        self.details_link_entry.delete('1.0', 'end')

        self.details_name_entry.insert('1.0', school.name)
        self.details_department_entry.insert('1.0', school.department)
        self.details_location_entry.insert('1.0', school.location)
        self.details_obligation_entry.insert('1.0', school.obligation)
        self.details_link_entry.insert('1.0', school.link)

        self.details_name_entry.configure(state='disabled')
        self.details_department_entry.configure(state='disabled')
        self.details_location_entry.configure(state='disabled')
        self.details_obligation_entry.configure(state='disabled')
        self.details_link_entry.configure(state='disabled')


        self.main_frame.pack_forget()
        self.details_frame.pack()

    def load_data(self):
        try:
            with open(self.filename, 'r', encoding='UTF8') as s:
                 self.schools = [School(**data) for data in json.load(s)]
                 print(self.schools)
        except FileNotFoundError:
            pass