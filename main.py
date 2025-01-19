from tkinter import *
from App.Center import *
from App.Frames import *
from Frames.Buttons import*
from Frames.Option_Frame import*
from Frames.Control_Panel import*
from Frames.Logo import*
import App.Config as con
from Frames.Status import *

class App(Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Test")
        self.geometry('1150x750')
        # App.maxsize('1050','700')
        self.minsize('1150','750')
        self.resizable(width=TRUE,height=True)
        
        getlist()
        self.update_idletasks()
        
        Center.center_window(self,self.winfo_width(),self.winfo_height())

 

        # Create the main frame
        main_frame = Frame(self, bg="black", width=1000, height=700)
        main_frame.pack(fill=BOTH, expand=True)

        # for frame right
#######################################################################
        control_frame=Frame(main_frame,bg="lightgray",width=0,height=0)
        control_frame.pack(side=RIGHT,fill="both",expand=False)


        Logo_frame=Logo_Frame(control_frame)
       


        

########################################################################




# for frame left
########################################################################
        content_frame=Frame(main_frame,bg="black",width=600,height=0)
        content_frame.pack(side=LEFT,fill="both",padx=(0,10),expand=TRUE)
 

        tframe=Frame(content_frame,bg="lightgray",width=0,height=0)
        tframe.pack(side=TOP,fill="both",expand=True,pady=(0,10))


        option_frame=Option_Frame(tframe)
        option_frame.pack(side=LEFT,fill="both",expand=True,pady=(0,10))


        status=Status_Frame(tframe)
        labels=(status.label,status.label2,status.label3)
        
        Control_Panel(control_frame,labels)
        
        

        display_frame=Frame(content_frame,bg="white",width=0,height=750)
        display_frame.pack(side=BOTTOM,fill="both",expand=True)


        Display_label = Label(display_frame, text="Display", bg="white",font=("Times New Roman", 20,"bold"))
        Display_label.pack(side=TOP, fill=X)

        display_content_frame = Frame(display_frame, bg="blue", width=600, height=550)
        display_content_frame.pack(side=BOTTOM, fill="both", expand=True)


        myframe=Display_Frames(display_content_frame)

        # Initially show frame1
        myframe.show_frame(myframe.frame1)

        option_frame.add_buttons(Display_label,myframe)
 
###########################################################################
        main_frame.mainloop()
 
App()