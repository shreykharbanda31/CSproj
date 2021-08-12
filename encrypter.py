from tkinter import *
from tkinter import ttk
from tkinter import font
import mysql.connector
from PIL import Image,ImageTk
from tkinter import messagebox
from importlib import reload
import atbashf,baconian,morse,pig,caeser,vigenere,mail,registerlogin
reload(atbashf)
reload(registerlogin)


def main():
    win=Tk()
    app=encrypt(win)
    win.mainloop()

#MAINWINDOW

class encrypt:
    def __init__(self,root):
        self.root=root
        self.root.title("Encrypt Program")
        self.root.geometry("1800x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Shrey Kharbanda\Desktop\CSproj\bg2.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
    
    #FRAME

        frame=Frame(self.root,bg="black")
        frame.place(x=350,y=0,width=600,height=750)

    #HEADINGLABEL   
        HEAD_str=Label(frame, text="ENCRYPT YOUR TEXT HERE",font=("system",28,"bold"),fg= "white",bg="black")
        HEAD_str.place(x=55,y=20)

    #INPUT TEXT
        global mess
        enter=Label(frame,text="Enter text to be encrypted",font=("franklin gothic medium",17,"bold italic"),fg="white",bg="black")
        enter.place(x=70,y=107)


        self.txtuser=Entry(frame,font=("times",15))
        self.txtuser.place(x=40,y=147,width=500,height=50)
        

        def mess():
            return mess
    #ICON
        img10=Image.open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\bubble.jpg")
        img10=img10.resize((25,25),Image.ANTIALIAS)
        self.root.photoimage10=ImageTk.PhotoImage(img10)
        lbling8=Label(frame,image=self.root.photoimage10,bg="black",borderwidth=0)
        lbling8.place(x=40,y=113,width=25,height=25)

    #LABEL TO ASK FOR OPTION
        opt=Label(frame,text="Select the required cipher",font=("cambria",17,"bold"),fg="white",bg="black")
        opt.place(x=180,y=250)

    #ICON
        img11=Image.open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\lock2.jpg")
        img11=img11.resize((100,50),Image.ANTIALIAS)
        self.photoimage11=ImageTk.PhotoImage(img11)
        lbling1=Label(frame,image=self.photoimage11,bg="black",borderwidth=0)
        lbling1.place(x=65,y=250,width=100,height=50)

    #RESPECTIVE BUTTONS
        btn1=Button(frame,text="ATBASH Cipher",command=lambda: atbascr(self,self.txtuser.get().upper()),font=("helvetica",14,"bold"),bd=3,relief=RIDGE,fg="white",bg="teal")
        btn1.place(x=110,y=345,width=350,height=35)

        btn2=Button(frame,text="BACONIAN Cipher",command=lambda: baconianscr(self,self.txtuser.get().upper()),font=("helvetica",14,"bold"),bd=3,relief=RIDGE,fg="white",bg="deepskyblue4")
        btn2.place(x=110,y=395,width=350,height=35)

        btn3=Button(frame,text="MORSE Cipher",command=lambda: morsescr(self,self.txtuser.get().upper()),font=("helvetica",14,"bold"),bd=3,relief=RIDGE,fg="white",bg="teal")
        btn3.place(x=110,y=445,width=350,height=35)

        btn4=Button(frame,text="CAESER Cipher",command=lambda: caesercr(self,self.txtuser.get().upper(),2),font=("helvetica",14,"bold"),bd=3,relief=RIDGE,fg="white",bg="deepskyblue4")
        btn4.place(x=110,y=495,width=350,height=35)

        btn5=Button(frame,text="PIGLATIN Cipher",command=lambda: pigscr(self,self.txtuser.get().upper()),font=("helvetica",14,"bold"),bd=3,relief=RIDGE,fg="white",bg="teal")
        btn5.place(x=110,y=545,width=350,height=35)

        btn6=Button(frame,text="VIGENERE Cipher",command=lambda: vigscr(self,self.txtuser.get().upper(),"CARAD"),font=("helvetica",14,"bold"),bd=3,relief=RIDGE,fg="white",bg="deepskyblue4")
        btn6.place(x=110,y=595,width=350,height=35)

        btn7=Button(self.root,text="Send Email",command=lambda: linkmail(),font=("helvetica",14,"bold"),bd=3,relief=RIDGE,fg="white",bg="deepskyblue4",borderwidth=6)
        btn7.place(x=980,y=295,width=250,height=80)

        

        def atbascr(self,message):
            mess=self.txtuser.get()
            file1= open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\fill.txt","a")
            file1.write("\t"+mess+"\n")
            atbashf.atbash(message)
        
        def baconianscr(self,message):
            mess=self.txtuser.get()
            file1= open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\fill.txt","a")
            file1.write("\t"+mess+"\n")
            baconian.encrypt(message)
        
        def morsescr(self,message):
            mess=self.txtuser.get()
            file1= open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\fill.txt","a")
            file1.write("\t"+mess+"\n")
     
            morse.eng_to_morse(message)

        def caesercr(self,message,key):
            mess=self.txtuser.get()
            file1= open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\fill.txt","a")
            file1.write("\t"+mess+"\n")
   
            caeser.caesar_encrypt(message,key)

        def pigscr(self,message):
            mess=self.txtuser.get()
            file1= open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\fill.txt","a")
            file1.write("\t"+mess+"\n")
            pig.pigLatin(message)
        
        def vigscr(self,message,key):
            mess=self.txtuser.get()
            file1= open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\fill.txt","a")
            file1.write("\t"+mess+"\n")
            vigenere.cipherText(message,key)

        def linkmail():
            self.new_window3=Toplevel(self.root)
            self.app=mail.mail(self.new_window3)

if __name__=="__main__":
    main()