from customtkinter import *

set_appearance_mode("dark")

class text_frame(CTkFrame):
    def __init__(self,master):
        super().__init__(master,fg_color="transparent")
        self.grid_columnconfigure((0,1),weight=1)
        self.entry=CTkEntry(self)
        self.line=CTkLabel(self,text="to submit press enter",corner_radius=10,border_color="gray40",border_width=3)
        
        self.entry.grid(row=0,column=0,padx=10,pady=10,sticky="ew",columnspan=2)
        
        self.line.grid(row=1,column=0,padx=10,pady=10,sticky="ew",columnspan=2)


    def change_line(self,event=None):
        self.line.configure(text="you typed in: "+self.entry.get()) 


    
class Radio_Frame(CTkScrollableFrame):
    def __init__(self,master,values,title,color=None):
        super().__init__(master,fg_color=color,label_text=title)
        self.grid_columnconfigure(0,weight=1)

        self.values=values
        self.variable=StringVar(value="")
        
        self.radios=[]
        for i,now_value in enumerate(self.values):
            radiobutton=CTkRadioButton(self,text=now_value, value=now_value, variable=self.variable)
            print(i ,", ",now_value)
            radiobutton.grid(row=i,column=0,padx=10,pady=10,sticky="w")
            self.radios.append(radiobutton)


    def get (self):
        return self.variable.get()
    
    def no_bar(self):
        self._scrollbar.grid_forget()
            


class CheckboxFrame(CTkScrollableFrame):
    def __init__(self,master,values,title,color=None):
        super().__init__(master,fg_color=color,label_text=title,)

        self.grid_columnconfigure(0,weight=1)
        
        self.values=values
        self.checkboxes=[]

        for i,value in enumerate(self.values):
            variable_checkbox= CTkCheckBox(self,text=value)
            variable_checkbox.grid(row=i+1 ,column=0,padx=10,pady=10,sticky="w")
            self.checkboxes.append(variable_checkbox)

        
    def get(self):
        
        checked_checkboxes=[]
        for checkbox in self.checkboxes:
            if checkbox.get()==1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

    def no_bar(self):
        self._scrollbar.grid_forget()

        

class App(CTk):
    def __init__(self):
        super().__init__()
        
        self.title("window")
        self.x_size=800
        self.y_size=600
        self.geometry(f"{self.x_size}x{self.y_size}")
        self.center()

        self.grid_columnconfigure((0,1),weight=1)
        self.grid_rowconfigure((0,2), weight=1)

        self.checkboxframe = CheckboxFrame(self, values=["value 1","value 2","value 3","bye woody"],
                                           title="first frame")
        self.checkboxframe.grid(row=0,column=0,padx=10,pady=10,sticky="nesw")

        self.frame2=CheckboxFrame(self,values=["another frame","value 67","3"],title="second frame")
        self.frame2.grid(row=0,column=1,padx=10,pady=10,sticky="nesw")

        self.radioframe=Radio_Frame(master=self,values=["YES","NO","option3 "],title="desisions",color="transparent")
        self.radioframe.no_bar()
        self.radioframe.grid(row=2,column=0,padx=10,pady=10,sticky="nesw")
        
        self.radfram2=Radio_Frame(master=self,values=["","do","45"],title="2",color="indigo")
        self.radfram2.no_bar()
        self.radfram2.grid(row=2,column=1,padx=10,pady=10,sticky="nesw")
        

        self.check_btn=CTkButton(self, text="check button",corner_radius=10,command=self.checkbox_maneger)
        self.check_btn.grid(row=1,column=0,padx=10,pady=10,sticky="nesw",columnspan=2)

        self.radio_btn=CTkButton(self,text="radio button",command=self.radio_maneger)
        self.radio_btn.grid(row=3,column=0,padx=10,pady=10,sticky='ew',columnspan=2)

        self.center=CTkButton(self,text="center",command=self.center)
        self.center.grid(row=5,column=0,padx=10,pady=10,sticky="ew")

        self.toggle=CTkButton(self,text="maximize",command=self.toggle_size)
        self.toggle.grid(row=5,column=1,padx=10,pady=10,sticky="ew")

        self.cool_func=text_frame(self)
        self.cool_func.grid(row=4,column=0,padx=10,pady=10,sticky="nesw",columnspan=2)

        frame_var=self.cool_func
        frame_var.entry.bind("<Return>",lambda event : frame_var.change_line())

        #frame_var=self.

    def center(self):
    
        scaling= ScalingTracker.get_window_scaling(self)
        x=int((self.winfo_screenwidth()-self.x_size*scaling)/2)
        y=int((self.winfo_screenheight()-self.y_size*scaling)/2)
        self.geometry(f"{self.x_size}x{self.y_size}+{x}+{y}")

    def toggle_size(self):
        self.attributes("-fullscreen",not self.attributes("-fullscreen"))
        if self.attributes("-fullscreen")==0:
            self.toggle.configure(text="mininize",fg_color="red")
        if self.attributes("-fullscreen")==1:
            self.toggle.configure(text="maximize",fg_color="blue")

    def checkbox_maneger(self):
        print("checked checkboxes frame1:", self.checkboxframe.get())
        print("checked checkboxes frame2:", self.frame2.get())
    
    def radio_maneger(self):
        print("checked radiobuttons frame1:", self.radioframe.get())
        print("checked radiobuttons frame2:", self.radfram2.get())
        
app=App()
app.mainloop()