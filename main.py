from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from recognition import Recognition
from attendance import Attendance

class Face_Recognition_Sytem:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x850")
        self.root.title("Face Recognition System")

        # first image
        img = Image.open('./Images/knust-entrance.jpg')
        img_resize = img.resize((500,300), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img_resize)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


         # second image
        img1 = Image.open('./Images/face_recog_3.png')
        img1_resize = img1.resize((500,200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1_resize)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # third image
        img2 = Image.open('./Images/stdents2.jpg')
        img2_resize = img2.resize((500,200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2_resize)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)


        # background image
        img3 = Image.open('./Images/bg.jpg')
        img3_resize = img3.resize((1530,640), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3_resize)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=650)

        titel_lbl = Label(bg_img, text="FACE RECOGNITION SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="blue")
        titel_lbl.place(x=0,y=0,width=1530,height=50)

        
        # student button
        img4 = Image.open('./Images/dev1.jpg')
        img4_resize = img4.resize((200,200), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4_resize)

        b1 = Button( bg_img,image=self.photoimg4,command=self.student_details, cursor='hand2')
        b1.place(x=200,y=80,width=250,height=170)

        b1_1 = Button(bg_img,text='Student Details',command=self.student_details, cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=245,width=250,height=40)

       
         # Train Dataset button
        img5 = Image.open('./Images/face_detect.jpg')
        img5_resize = img5.resize((200,200), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5_resize)

        b1 = Button( bg_img,image=self.photoimg5,command=self.train_data,cursor='hand2')
        b1.place(x=500,y=80,width=250,height=170)

        b1_1 = Button(bg_img,text='Train Datasets',command=self.train_data,cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=245,width=250,height=40)

        # Recognition        
        img6 = Image.open('./Images/face_recog2.jpg')
        img6_resize = img6.resize((200,200), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6_resize)

        b1 = Button( bg_img,image=self.photoimg6,command=self.recognize_face, cursor='hand2')
        b1.place(x=800,y=80,width=250,height=170)

        b1_1 = Button(bg_img,text='Recognition',cursor='hand2',command=self.recognize_face, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=245,width=250,height=40)
       
   
        # Attendance button
        img7 = Image.open('./Images/att.png')
        img7_resize = img7.resize((200,200), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7_resize)

        b1 = Button( bg_img,image=self.photoimg7,command=self.attendance_data, cursor='hand2')
        b1.place(x=200,y=330,width=250,height=170)

        b1_1 = Button(bg_img,text='Attendance',command=self.attendance_data, cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=499,width=250,height=40)

        #  Help  button
        img8 = Image.open('./Images/help.jpg')
        img8_resize = img8.resize((200,200), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8_resize)

        b1 = Button( bg_img,image=self.photoimg8, cursor='hand2')
        b1.place(x=500,y=330,width=250,height=170)

        b1_1 = Button(bg_img,text='Help',cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white",command=self.recognize_face)
        b1_1.place(x=500,y=499,width=250,height=40)





    # functional buttons
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        self.new_window.grab_set()
           

    # train buttons
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        self.new_window.grab_set()

    # recognize button
    def recognize_face(self):
        self.new_window = Toplevel(self.root)
        self.app = Recognition(self.new_window)
        self.new_window.grab_set()

    
    # Attendance button
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
        self.new_window.grab_set()

if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition_Sytem(root)
    root.mainloop()