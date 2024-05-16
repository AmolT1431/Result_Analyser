from tkinter import *
from App.Center import *
from App.Frames import *
from Frames.Buttons import*
from Frames.Option_Frame import*
from Frames.Control_Panel import*
 


App = Tk()
App.title("Test")
App.geometry('1150x750')
# App.maxsize('1050','700')
App.minsize('850','550')
App.resizable(width=TRUE,height=True)
 

App.update_idletasks()
 
Center.center_window(App,App.winfo_width(),App.winfo_height())

 

# Create the main frame
main_frame = Frame(App, bg="black", width=1000, height=700)
main_frame.pack(fill=BOTH, expand=True)

 # for frame right
#######################################################################
control_frame=Frame(main_frame,bg="lightgray",width=0,height=0)
control_frame.pack(side=RIGHT,fill="both",expand=False)

Logo_frame=Frame(control_frame,bg="white",width=250,height=200)
Logo_frame.pack(side=TOP,fill="x",padx=(15,15),pady=10)

control_panel=Control_Panel(control_frame)

########################################################################




# for frame left
########################################################################
content_frame=Frame(main_frame,bg="black",width=600,height=0)
content_frame.pack(side=LEFT,fill="both",padx=(0,10),expand=TRUE)

option_frame=Option_Frame(content_frame)
option_frame.pack(side=TOP,fill="both",expand=True,pady=(0,10))

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
 
