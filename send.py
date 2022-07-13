from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox as msg
import sqlite3
import cv2
import numpy as np 
import os

# email imports
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



# my_password = "xrmomhqkojqadnoj"

class Message:
    def __init__(self,root):
        self.root = root
        self.root.geometry("900x400+0+0")
        self.root.title("Send File To Email Address")


        self.var_email = StringVar()

        # main frame
        main_frame = Frame(self.root,bd=2)
        main_frame.place(x=10,y=55,width=1330,height=600)

        # left label frame
        left_frame = LabelFrame(main_frame, bd=3, relief=RIDGE,text='Please Provide Email Address',font=("times new roman",18,"bold"))
        left_frame.place(x=170,y=10,width=550,height=200)

        # Email address
        Email_label = Label(left_frame,text="Email Address:",font=("times new roman",13,"bold"))
        Email_label.grid(row=0,column=0,padx=13, pady=40, sticky=W)

        Email_entry = ttk.Entry(left_frame,width=40,textvariable=self.var_email, font=("times new roman",13,"bold"))
        Email_entry.grid(row=0,column=1,padx=0,pady=40,sticky=W)

        # send button
        save_button = Button(left_frame,command=self.send, text="Send Email",font=("times new roman",13,"bold"),bg='blue',fg='white')
        save_button.place(x=15,y=100,width=110,height=40)

        # delete button
        delete_button = Button(left_frame,text="Reset Info",command=self.reset, font=("times new roman",13,"bold"),bg='blue',fg='white')
        delete_button.place(x=140,y=100,width=110,height=40)



    # reset         
    def reset(self):
        self.var_email.set("")
        return

    # send
    def send(self):
        if not self.var_email.get():
            msg.showerror("Error","Field cannot be empty!!!")
        else:
            try:
                subject = "An attachment of Attendance records"
                body = "This is the Attendance sheet generated!!!"
                sender_email = "adomahabubakar100@gmail.com"
                receiver_email = self.var_email.get()
                password = "xrmomhqkojqadnoj"

                # Create a multipart message and set headers
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = subject
                message["Bcc"] = receiver_email  # Recommended for mass emails

                # Add body to email
                message.attach(MIMEText(body, "plain"))

                filename = "attendance.csv"  # In same directory as script

                # Open PDF file in binary mode
                with open(filename, "rb") as attachment:
                    # Add file as application/octet-stream
                    # Email client can usually download this automatically as attachment
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())

                # Encode file in ASCII characters to send by email    
                encoders.encode_base64(part)

                # Add header as key/value pair to attachment part
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {filename}",
                )

                # Add attachment to message and convert message to string
                message.attach(part)
                text = message.as_string()

                # Log in to server using secure context and send email
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, text)
                    msg.showinfo("Results","Email successfully sent!!!")
                    return
            except smtplib.SMTPRecipientsRefused:
                msg.showerror("Error","Email Address is not valid!!!")

if __name__ == '__main__':
    root = Tk()
    obj = Message(root)
    root.mainloop()