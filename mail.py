from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox
import smtplib




s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("encryptiondps@gmail.com", "encryption")

def main():
    win=Tk()
    app=mail(win)
    win.mainloop()


class mail:
    def __init__(self,root):
        self.root=root
        self.root.title("Send email")
        self.root.geometry("1800x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Shrey Kharbanda\Desktop\CSproj\bg2.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

    #FRAME
        frame=Frame(self.root,bg="black")
        frame.place(x=350,y=0,width=600,height=750)

    #HEADINGLABEL   
        HEAD_str=Label(frame, text="SEND YOUR EMAIL HERE",font=("system",31),fg= "white",bg="black")
        HEAD_str.place(x=47,y=20)

    #INPUT TEXT
        global emoi
        enter=Label(frame,text="Enter receiver's email address",font=("franklin gothic medium",17,"bold"),fg="white",bg="black")
        enter.place(x=70,y=107)


        self.txtuser=Entry(frame,font=("times",15))
        self.txtuser.place(x=40,y=147,width=500,height=50)
        emoi=self.txtuser.get()

    #ICON
        img2=Image.open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\bubble.jpg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.root.photoimage2=ImageTk.PhotoImage(img2)
        lbling1=Label(frame,image=self.root.photoimage2,bg="black",borderwidth=0)
        lbling1.place(x=40,y=113,width=25,height=25)

    #BUTTON
        btn1=Button(frame,text="Send email",command=lambda: que(self),font=("helvetica",14,"bold"),bd=3,relief=RIDGE,fg="white",bg="teal")
        btn1.place(x=110,y=300,width=350,height=35)

                # Python code to illustrate Sending mail with attachments
        # from your Gmail account

        # libraries to be imported
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders

        fromaddr = "encryptiondps@gmail.com"
        toaddr = emoi

        # instance of MIMEMultipart
        msg = MIMEMultipart()

        # storing the senders email address
        msg['From'] = fromaddr

        # storing the receivers email address
        msg['To'] = toaddr

        # storing the subject
        msg['Subject'] = "Ciphered Text"

        # string to store the body of the mail
        body = "Please find the attached text file!"

        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # open the file to be sent
        filename = "fill.txt"
        attachment = open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\fill.txt", "rb")

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

        # Converts the Multipart msg into a string
        text = msg.as_string()
    
        def que(self):
            o=0
            result = messagebox.askquestion("Email","Are you sure you want to send an email?",icon='warning')
            if result=='yes':
                s.sendmail("encryptiondps@gmail.com", self.txtuser.get() , text)
                img4=Image.open(r"C:\Users\Shrey Kharbanda\Desktop\CSproj\lol.png")
                img4=img4.resize((400,200),Image.ANTIALIAS)
                self.root.photoimage4=ImageTk.PhotoImage(img4)
                lbling1=Label(frame,image=self.root.photoimage4,bg="black",borderwidth=0)
                lbling1.place(x=100,y=400,width=400,height=200)
            if result=='no':
                confirm2=Label(frame,text="Email not sent",font=("franklin gothic medium",17,"bold italic"),fg="white",bg="black")
                confirm2.place(x=110,y=395+0)
                o+=20
                return
            
            
        



if __name__=="__main__":
    main()