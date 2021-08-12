from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import encrypter
from importlib import reload
reload(encrypter)


def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()


#MAINWINDOW
class login_window:
    global ju
    def __init__(screen,cipher):
        global ju
        screen.cipher=cipher
        screen.cipher.title("Login")
        screen.cipher.geometry("1800x800+0+0")

        screen.bg=ImageTk.PhotoImage(file=r"C:\Users\Shrey Kharbanda\Desktop\CSproj\hashing.png")
        lbl_bg=Label(screen.cipher,image=screen.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

#FRAME

        frame=Frame(screen.cipher,bg="black")
        frame.place(x=450,y=140,width=340,height=450)

        img1=Image.open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\hacker.jpeg")
        img1=img1.resize((75,75),Image.ANTIALIAS)
        screen.photoimage1=ImageTk.PhotoImage(img1)
        lblimage1=Label(image=screen.photoimage1,bg="black",borderwidth=0)
        lblimage1.place(x=583,y=150,width=75,height=75)

#Getstarted 

        get_str=Label(frame, text="Get Started",font=("system",31,"bold"),fg= "white",bg="black")
        get_str.place(x=65,y=90)

 #LABELS

        
        username=lbl=Label(frame,text="Email",font=("helvetica",16,"bold"),fg="white",bg="black")
        username.place(x=70,y=161)

        global boo
        screen.txtuser=boo=Entry(frame,font=("helvetica",15,"bold"))
        screen.txtuser.place(x=40,y=197,width=270)


        password=lbl=Label(frame,text="Password",font=("helvetica",16,"bold"),fg="white",bg="black")
        password.place(x=70,y=251)

        screen.txtpass=ttk.Entry(frame,font=("helvetica",15,"bold"),show='*')
        screen.txtpass.place(x=40,y=284,width=270)

#ICONIMAGE

        img2=Image.open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\getstart.jpeg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        screen.photoimage2=ImageTk.PhotoImage(img2)
        lbling1=Label(image=screen.photoimage2,bg="black",borderwidth=0)
        lbling1.place(x=490,y=303,width=25,height=25)

        img3=Image.open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\lock.jpeg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        screen.photoimage3=ImageTk.PhotoImage(img3)
        lbling1=Label(image=screen.photoimage3,bg="black",borderwidth=0)
        lbling1.place(x=490,y=393,width=25,height=25)

#Loginbtn

        loginbtn=Button(frame,command=screen.login,text="Login",font=("helvetica",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="teal")
        loginbtn.place(x=110,y=345,width=120,height=35)

#Registerbtn

        registerbtn=Button(frame,text="New user register",command=screen.register_window, font=("arial",10,"bold"),borderwidth=0,fg="black",bg="light grey",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=410,width=160)

   
    
#LinkWindow
    def register_window(screen):
        screen.new_window=Toplevel(screen.cipher)
        screen.app=Register(screen.new_window)
    
    def encrypt_window(screen):
        screen.new_window2=Toplevel(screen.cipher)
        screen.app=encrypter.encrypt(screen.new_window2)
#login
    def login(screen):
        global ju
        if screen.txtuser.get()=="" or screen.txtpass.get()=="":
            messagebox.showerror("Error","Field is empty")
        elif screen.txtuser.get()=="hello" and screen.txtpass.get()=="world":
            messagebox.showinfo("Succes","Welcome to cipher")
        else:
            global ju
            conn=mysql.connector.connect(host="localhost",user="root",password="Student123", database="cipher_database")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and pass=%s",( 
                                                                                screen.txtuser.get(),
                                                                                screen.txtpass.get()
                                                                            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","invalid username or password")
            else:
                messagebox.showinfo("Welcome","You have successfully logged in!")
                global ju
                screen.encrypt_window()
                ju=boo.get()
                file1= open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\fill.txt","a")
                file1.write("Login email: "+ ju +"\n\n")
                file1.close()
                screen.cipher.withdraw()
    

#==================================REGISTER PAGE=====================================#

class Register:
    def __init__(screen2,cipher):
        screen2.cipher=cipher
        screen2.cipher.title("Register")
        screen2.cipher.geometry("1600x900+0+0")

#Variables

        screen2.var_fname=StringVar()
        screen2.var_lname=StringVar()
        screen2.var_contact=StringVar()
        screen2.var_email=StringVar() 
        screen2.var_securityQ=StringVar()
        screen2.var_securityA=StringVar()
        screen2.var_pass=StringVar()
        screen2.var_confpass=StringVar()

#BGIMAGE

        screen2.bg=ImageTk.PhotoImage(file=r"C:\Users\Shrey Kharbanda\Desktop\CSproj\register1.png")

        bg_lbl=Label(screen2.cipher,image=screen2.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

#MAINFRAME

        frame=Frame(screen2.cipher,bg="black")
        frame.place(x=500,y=100,width=800,height=550 )

        register_lbl=Label(frame,text="SIGN UP HERE",font=("system",31,"underline","bold"),fg="white",bg="black")
        register_lbl.place(x=20,y=20)

#===============================label and entry===============================

#ROW1

        fname=Label(frame,text="First Name",font=("calisto",15,"bold"),bg="black",fg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame, textvariable=screen2.var_fname, font=("calisto",15))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("calisto",15,"bold"),bg="black",fg="white")
        l_name.place(x=370,y=100)

        screen2.txt_l_name=ttk.Entry(frame,textvariable=screen2.var_lname,font=("calisto",15))
        screen2.txt_l_name.place(x=370,y=130,width=250)


#ROW2

        contact=Label(frame,text="Contact No.",font=("calisto",15,"bold"),bg="black",fg="white")
        contact.place(x=50,y=170)

        screen2.txt_contact=ttk.Entry(frame,textvariable=screen2.var_contact,font=("calisto",15))
        screen2.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("calisto",15,"bold"),bg="black",fg="white")
        email.place(x=370,y=170)

        screen2.txt_email=ttk.Entry(frame,textvariable=screen2.var_email, font=("calisto",15))
        screen2.txt_email.place(x=370,y=200,width=250)
    
#ROW3
        security_Q=Label(frame, text="Select Security Questions",font=("calisto",15,"bold"),bg="black",fg="white")
        security_Q.place(x=50,y=240)

        screen2.combo_securiy_Q= ttk.Combobox(frame, textvariable=screen2.var_securityQ, font=("calisto",15),state="readonly")
        screen2.combo_securiy_Q["values"]=("Select","Your Birth Place","Your Best Friend's Name","Your PetName")

        screen2.combo_securiy_Q.place(x=50,y=270,width=250)
        screen2.combo_securiy_Q.current(0)

        security_A=Label(frame, text="Security Answer",font=("calisto",15,"bold"),bg="black",fg="white")
        security_A.place(x=370,y=240)

        screen2.txt_security=ttk.Entry(frame, textvariable=screen2.var_securityA, font=("calisto",15))
        screen2.txt_security.place(x=370,y=270,width=250)
    
#ROW4
        pswd=Label(frame,text="Password",font=("calisto",15,"bold"),bg="black",fg="white")
        pswd.place(x=50,y=310)

        screen2.txt_pswd=ttk.Entry(frame,textvariable=screen2.var_pass,font=("calisto",15),show='*')
        screen2.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("calisto",15,"bold"),bg="black",fg="white")
        confirm_pswd.place(x=370,y=310)

        screen2.txt_confirm_pswd=ttk.Entry(frame, textvariable=screen2.var_confpass, font=("calisto",15),show='*')
        screen2.txt_confirm_pswd.place(x=370,y=340,width=250)

#CheckBtn
        screen2.var_check=IntVar()
        screen2.checkbtn=Checkbutton(frame, variable=screen2.var_check, text="I Agree To The Terms & Conditions", font=("calisto",12,"bold"),onvalue=1,offvalue=0)
        screen2.checkbtn.place(x=50,y=380)
    
#Buttons

        img2=Image.open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\login1.png")
        img2=img2.resize((200,50),Image.ANTIALIAS)                    
        screen2.photoimage=ImageTk.PhotoImage(img2)
        b1=Button(frame,image=screen2.photoimage,command=screen2.register_data,borderwidth=10,cursor="hand2",font=("calisto",15 ,"bold"))
        b1.place(x=100,y=420,width=200)

        img1=Image.open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\login2.jpg")
        img1=img1.resize((200,50),Image.ANTIALIAS)                    
        screen2.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=screen2.photoimage1,command=screen2.return_login,borderwidth=10,cursor="hand2",font=("calisto",15 ,"bold"))
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


#LOGINPAGE

    def return_login(screen):
        screen.cipher.destroy()


if __name__=="__main__":
    main()