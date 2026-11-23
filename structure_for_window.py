from customtkinter import *

set_appearance_mode("dark")

class tabclass(CTkTabview):
    def __init__(self,master):
        super().__init__(master)
        self.add("monthly timetable")
        self.add("weekly timetable")
        for name in ("monthly timetable","weekly timetable"):
            self.tab(name).grid_columnconfigure(0,weight=1)
            self.tab(name).grid_rowconfigure(0,weight=1)


class week (CTkFrame):
    def __init__(self,master,week_number):
        super().__init__(master,bg_color="transparent")
        self.grid_columnconfigure((0,1,2,3,4,5,6,7),weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.week_number=week_number
        
        self.btnarray=[]
        self.title=CTkLabel(self,text=f"week {self.week_number}")
        self.title.grid(row=0,column=0,padx=10,pady=10,sticky="ew")
        


        for i in range(7):
            button=CTkButton(self,text="add activity",fg_color="gray40",hover_color="darkblue")
            button.grid(row=0,column=i+1,padx=10,pady=10,sticky="nesw")
            self.btnarray.append(button)

    



class grid (CTkFrame):
    def __init__(self,master,numb_weeks):
        super().__init__(master,fg_color="transparent")
        self.num_weeks=numb_weeks
        self.grid_columnconfigure(0,weight=1)
        for i in range (self.num_weeks):
            self.grid_rowconfigure(i,weight=1)
        i=0
        for i in range (self.num_weeks):
            week_frame=week(self,week_number=i+1)
            week_frame.grid(row=i,column=0,sticky="nesw")


class default_frame(CTkFrame):
    def __init__(self,master,color):
        super().__init__(master,border_color=color,border_width=3,corner_radius=10)

class App (CTk):
    def __init__(self):
        super().__init__()
        self.title("timetable")
        self.geometry("500x500")
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.frame_for_tab=default_frame(self,color="gray15")
        self.frame_for_tab.grid(row=0,column=1,padx=10,pady=10,sticky="nesw")

        self.tab=tabclass(self.frame_for_tab)
        self.tab.pack(fill="both",expand=True,padx=10,pady=10)
        
        
        self.timetable=grid(self.tab.tab("monthly timetable"), numb_weeks=4)
        self.timetable.grid(row=0,column=0,padx=10,pady=10,sticky="nesw")

        self.vertical=default_frame(self,color="gray")
        self.vertical.grid(row=0,column=0,padx=10,pady=10,sticky="nesw")








app=App()
app.mainloop()
