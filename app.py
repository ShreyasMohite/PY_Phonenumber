from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
from phonenumbers import carrier
from phonenumbers import timezone
from phonenumbers import geocoder
import phonenumbers 
import threading

class Googles:
    def __init__(self,root):
        self.root=root
        self.root.title("Phone_Number Search")
        self.root.geometry("500x400")
        self.root.iconbitmap("logo902.ico")
        self.root.resizable(0,0)

        search_number=StringVar()
        numbers=StringVar()


#=================================================================================#

        def clear():
            search_number.set("")
            numbers.set("Select Categories")
            text.delete("1.0","end")

        def searchs():
            try:
                with open("C:/TEMP/num.txt","w") as f:

                    
                    if search_number.get()!="":
                        if numbers.get()!="Select Categories":
                            if numbers.get()=="Extract":
                                z = phonenumbers.parse("+91{}".format(search_number.get()), None)
                                f.write(str(z)+"\n")

                            if numbers.get()=="Possible_Number":
                                z = phonenumbers.parse("+91{}".format(search_number.get()), None)
                                ans=phonenumbers.is_possible_number(z)
                                f.write(str(ans)+"\n")

                            if numbers.get()=="Valid_Number":
                                z = phonenumbers.parse("+91{}".format(search_number.get()), None)
                                ans=phonenumbers.is_valid_number(z)
                                f.write(str(ans)+"\n")

                            if numbers.get()=="Service_Provider":
                                z = phonenumbers.parse("+91{}".format(search_number.get()), "GB")
                                ans=carrier.name_for_number(z, "en")
                                f.write(str(ans)+"\n")

                            if numbers.get()=="Timezone":
                                z = phonenumbers.parse("+91{}".format(search_number.get()), "GB")
                                ans=timezone.time_zones_for_number(z)
                                f.write(str(ans)+"\n")

                            if numbers.get()=="Geolocation":
                                z = phonenumbers.parse("+91{}".format(search_number.get()), "CH")
                                ans=geocoder.description_for_number(z,"en")
                                f.write(str(ans)+"\n")

                        
                        else:
                            tkinter.messagebox.showerror("Error","Please Select Categories")
                    else:
                        tkinter.messagebox.showerror("Error","Please Enter Number for search")
                with open("C:/TEMP/num.txt","r") as f:
                    text.insert("end",f.read())

                
            except Exception as e:
                #print(e)
                tkinter.messagebox.showerror("Error","Please Enter only phone number")

        def thread_search():
            t1=threading.Thread(target=searchs)
            t1.start()
                

#==================================================================================#
        def on_enter1(e):
            but_search['background']="black"
            but_search['foreground']="cyan"
  
        def on_leave1(e):
            but_search['background']="SystemButtonFace"
            but_search['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

#==================================================================================#
        mainframe=Frame(self.root,width=500,height=400,bd=3,relief="ridge")
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=150,bd=3,relief="ridge")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=243,bd=3,relief="ridge")
        secondframe.place(x=0,y=150)

#================================firstframe===================================================#

        lab_frame=LabelFrame(firstframe,width=488,height=145,text="Phone Number Search",bg="#89b0ae",fg="white")
        lab_frame.place(x=0,y=0)
#==============================================================================================#

        lab=Label(lab_frame,text="Search Number",font=('times new roman',12),bg="#89b0ae")
        lab.place(x=0,y=5)

        ent_search=Entry(lab_frame,width=37,font=('times new roman',12),bd=3,relief="ridge",textvariable=search_number)
        ent_search.place(x=170,y=5)

        lab_results=Label(lab_frame,text="Number Categories:",font=('times new roman',12),bg="#89b0ae")
        lab_results.place(x=0,y=50)

        but_search=Button(lab_frame,width=13,text="Search",font=('times new roman',12),cursor="hand2",command=thread_search)
        but_search.place(x=50,y=90)
        but_search.bind("<Enter>",on_enter1)
        but_search.bind("<Leave>",on_leave1)

        fileselect=["Extract","Possible_Number","Valid_Number","Service_Provider","Timezone","Geolocation"]
        fileselect_combo=Combobox(firstframe,values=fileselect,font=('arial',12),width=20,state="readonly",textvariable=numbers)
        fileselect_combo.set("Select Categories")
        fileselect_combo.place(x=200,y=60)

        but_clear=Button(lab_frame,width=13,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=300,y=90)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)

#=============================================================================================================#
        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=12,width=58,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)



if __name__ == "__main__":
    root=Tk()
    app=Googles(root)
    root.mainloop()


    
