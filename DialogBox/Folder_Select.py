import tkinter as tk
from tkinter import filedialog
import App.Config
from Frames.Status import *
from Download_Result import *
from pathlib import Path

def create_directory(directory_path):
    try:
        Path(directory_path).mkdir(parents=True, exist_ok=True)
        print(f"Directory '{directory_path}' created successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def select_file(label):
    image = Image.open(r'F:\C & C++\Result_Analyser\ok_alert.png')
    image = image.resize((20, 20), Image.LANCZOS)
    icon = ImageTk.PhotoImage(image)
    
    
    file_path = filedialog.askopenfilename()
    if file_path:
        App.Config.set_file_path(file_path)
        print(file_path)
        label.config(text="PRN List Selected", image=icon, compound='right',height=2,padx=5, pady=15)
        label.image = icon
        App.Config.set_file_path(file_path)
        create_directory(App.Config.get_directory_path()+"/mydir")
        
        
        
def Result_download(label):
    Download_Result.download(App.Config.get_directory_path(),label)
    
    label.config(text="Result Downloadeding...",height=2,padx=5, pady=15)
   
    print(App.Config.get_file_path())
    
    
    
            
def Process_Data(label):
    image = Image.open(r'F:\C & C++\Result_Analyser\ok_alert.png')
    image = image.resize((20, 20), Image.LANCZOS)
    icon = ImageTk.PhotoImage(image)
    
    label.config(text="Data Processed", image=icon, compound='right',height=2,padx=5, pady=15)
    label.image = icon
    