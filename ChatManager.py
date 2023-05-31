import tkinter as tk
import json
from School import School
from tkinter import Button, Canvas, Label
from PIL import ImageTk, Image
from os import path
from functools import partial
import customtkinter

class ChatManager():
    def __init__(self, root):
        self.root = root
        self.message = ""
        self.create_main_frame()
      
        
    def send_message(self):
        self.message = str(self.entry.get())
        if self.message != "":
            self.chatbox.insert(tk.END, self.message + "\n")
        self.entry.delete(0, 'end')
        
    def create_main_frame(self):
        
        self.main_frame = customtkinter.CTkFrame(self.root)
        self.main_frame.pack(expand=True)

        self.frame = customtkinter.CTkFrame(self.main_frame)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        self.chatbox = customtkinter.CTkTextbox(self.frame, width=650, height=300)
        self.chatbox.pack(fill='both', expand=True, pady=10)
        
        self.entry = customtkinter.CTkEntry(self.frame, width=500, height=50)
        self.entry.pack(fill='both', expand=True, pady=5, side='left')

        self.button = customtkinter.CTkButton(self.frame, text="보내기", command=self.send_message, width=70, height=50)
        self.button.pack(fill='both', expand=True, side='left')

        self.entry.focus()
        self.root.bind('<Return>', lambda event=None: self.button.invoke())
            
    
