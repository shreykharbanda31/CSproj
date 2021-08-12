from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import font
import mysql.connector


"""

#Create table
conn=mysql.connector.connect(host="localhost",user="root",password="Student123",database="cipher_database")

mycur=conn.cursor()
mycur.execute("Create Table register(fname varchar(20), lname varchar(20), contact int, email varchar(20), securityQ varchar(20), securityA varchar(20), pass varchar(20))")

"""

def reg_screen():
    global screen2
    screen2=Tk()
    screen2.title("Register")
    screen2.geometry("1600x900+0+0")

    #variables

    #Variables

    screen2.var_fname=StringVar()
    screen2.var_lname=StringVar()
    screen2.var_contact=StringVar()
    screen2.var_email=StringVar() 
    screen2.var_securityQ=StringVar()
    screen2.var_securityA=StringVar()
    screen2.var_pass=StringVar()
    screen2.var_confpass=StringVar()

    #bgimage

    screen2.bg=ImageTk.PhotoImage(file=r"C:\Users\Shrey Kharbanda\Desktop\CSProj\register.png")

    bg_lbl=Label(screen2,image=screen2.bg)
    bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

    #mainframe

    frame=Frame(screen2,bg="black")
    frame.place(x=500,y=100,width=800,height=550 )

    register_lbl=Label(frame,text="SIGN UP HERE",font=("times new roman",20,"underline"),fg="black")
    register_lbl.place(x=20,y=20)


    #===============================label and entry===============================

#--------------------------------row 1--------------------------------

    fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
    fname.place(x=50,y=100)

    fname_entry=ttk.Entry(frame, textvariable=screen2.var_fname, font=("times new roman",15,"bold"))
    fname_entry.place(x=50,y=130,width=250)

    l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
    l_name.place(x=370,y=100)

    screen2.txt_l_name=ttk.Entry(frame,textvariable=screen2.var_lname,font=("times new roman",15))
    screen2.txt_l_name.place(x=370,y=130,width=250)

#ROW2

    contact=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black")
    contact.place(x=50,y=170)

    screen2.txt_contact=ttk.Entry(frame,textvariable=screen2.var_contact,font=("times new roman",15))
    screen2.txt_contact.place(x=50,y=200,width=250)

    email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
    email.place(x=370,y=170)

    screen2.txt_email=ttk.Entry(frame,textvariable=screen2.var_email, font=("times new roman",15))
    screen2.txt_email.place(x=370,y=200,width=250)

    #--------------------------------row3--------------------------------
    security_Q=Label(frame,textvariable=screen2.var_securityQ, text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
    security_Q.place(x=50,y=240)

    screen2.combo_securiy_Q= ttk.Combobox(frame,font=("times new roman",15,"bold"),state="readonly")
    screen2.combo_securiy_Q["values"]=("Select","Your Birth Place","Your Best Friend's Name","Your PetName")
    screen2.combo_securiy_Q.place(x=50,y=270,width=250)
    screen2.combo_securiy_Q.current(0)

    security_A=Label(frame,textvariable=screen2.var_securityA, text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
    security_A.place(x=370,y=240)

    screen2.txt_security=ttk.Entry(frame,font=("times new roman",15))
    screen2.txt_security.place(x=370,y=270,width=250)
    
#--------------------------------row4--------------------------------
    pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
    pswd.place(x=50,y=310)

    screen2.txt_pswd=ttk.Entry(frame,textvariable=screen2.var_pass, font=("times new roman",15))
    screen2.txt_pswd.place(x=50,y=340,width=250)

    confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
    confirm_pswd.place(x=370,y=310)

    screen2.txt_confirm_pswd=ttk.Entry(frame, textvariable=screen2.var_confpass, font=("times new roman",15))
    screen2.txt_confirm_pswd.place(x=370,y=340,width=250)
#CheckBtn
    screen2.var_check=IntVar()
    screen2.checkbtn=Checkbutton(frame, variable=screen2.var_check, text="I Agree To The Terms & Conditions", font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
    screen2.checkbtn.place(x=50,y=380)

#LoginBtn
    b1=Button(frame,text="REGISTER",font=("arial",10,"bold"),command= lambda: register_data(screen2),borderwidth=0,fg="black",bg="light grey",activeforeground="white",activebackground="black")
    b1.place(x=100,y=420,width=200)

    img1=Image.open(r"C:\Users\Shrey Kharbanda\Desktop\CSProj\login2.jpg")
    img1=img1.resize((200,50),Image.ANTIALIAS)                    
    screen2.photoimage=ImageTk.PhotoImage(img1)
    b1=Button(frame,image=screen2.photoimage,borderwidth=10,cursor="hand2",font=("times new roman",15 ,"bold"))
    b1.place(x=330,y=420,width=200)
    
#FunctionDeclaration

    def register_data(screen2):
        if screen2.var_fname.get()=="" or screen2.var_email.get()=="" or screen2.var_securityQ.get()== "Select":
            messagebox.showerror("Error","All fields are required")
        elif screen2.var_pass.get()!= screen2.var_confpass.get():
            messagebox.showerror("Error","password and confirm password must be same")
        elif screen2.var_check.get()== 0:
            messagebox.showerror("Error","please agree to our terms and conditions")

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Student123", database="cipher_database")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(screen2.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showinfo("Error","User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        screen2.var_fname.get(),
                                                                                        screen2.var_lname.get(),
                                                                                        screen2.var_contact.get(),
                                                                                        screen2.var_email.get(),
                                                                                        screen2.var_securityQ.get(),
                                                                                        screen2.var_securityA.get(),
                                                                                        screen2.var_pass.get()

                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucess","Registration Successful")

    screen2.mainloop()

reg_screen()