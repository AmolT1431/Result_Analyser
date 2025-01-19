 
from tkinter import *
from tkinter import ttk
from Result import *

class Fail(Frame):
    def __init__(self, parent):
        super().__init__(parent,bg="red")
        
        label4 = Label(self, text="Fails List",font=("Times New Roman", 15,"bold"))
        label4.pack(padx=20, pady=5)
        
        
        style = ttk.Style(self)
        style.theme_use("clam")  #
        style.configure("Custom.Treeview", rowheight=25, font=('Times New Roman', 10, 'bold'))
        style.configure("Custom.Treeview.Heading", font=('Times New Roman', 14, 'bold'))  # Adjust font size for headings
        
        # Create the Treeview widget
        self.table = ttk.Treeview(self, columns=('Name', 'Result'), show='headings', style="Custom.Treeview")
        self.table.heading('Name', text='Name')
        self.table.heading("Result", text='Fail Subs')
      
        
        # Set column width to center align the text
        self.table.column('Name')
        self.table.column('Result',width=95)
       
        # Insert sample data
      
        mylist = getlist()
        sort=sorted(mylist, key=lambda x: x.Total,reverse=True)
        sort.reverse()
        self.table.tag_configure("gray",background="lightgray")
        self.table.tag_configure("normal",background="white")
        my_tag="normal"
        for item in sort:
           if(item.Result()=="PASS"):
               my_tag='normal'
           else:
               my_tag='gray'
           st=""
           for string in item.failed_subjects():
               st=st + string + ","
               
           if(my_tag=="gray"):
               self.table.insert(parent='', index=0, values=(item.Name,st),tags=(my_tag))
            
           
        self.table.pack(fill="both", expand=True)
        self.pack(side=RIGHT,fill="both",expand=TRUE)