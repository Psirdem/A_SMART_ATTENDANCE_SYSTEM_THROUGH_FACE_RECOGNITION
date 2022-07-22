from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox as msg
import sqlite3
import cv2
import numpy as np 
import os

image_path = './Images/'

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1550x850+0+0")
        self.root.title("Face Recognition System")

        self.var_name =StringVar()
        self.var_std = StringVar()
        self.var_prog = StringVar()
        

        
        title_lbl = Label(self.root, text="KWAME NKRUMAH UNIVERSITY OF SCIENCE AND TECHNOLOGY",font=("Montserrat",30,"bold"),bg="white",fg="gold")
        title_lbl.place(x=0,y=0,width=1360,height=120)


        
        # background image
        img3 = Image.open('./Images/bg1.jpg')
        img3_resize = img3.resize((1530,640), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3_resize)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=85,width=1530,height=650)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=55)

        # main frame
        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1330,height=600)

        # left label frame
        left_frame = LabelFrame(main_frame, bd=3, relief=RIDGE,text='Student Details',font=("times new roman",20,"bold"))
        left_frame.place(x=400,y=20,width=550,height=460)

      

        # fullname
        
        fullname_label = Label(left_frame,text="Full Name: ",font=("times new roman",13,"bold"))
        fullname_label.grid(row=1,column=0,padx=2, sticky=W)

        fullname_entry =ttk.Entry(left_frame, width=40,textvariable=self.var_name, font=("times new roman",13,"bold"))
        fullname_entry.grid(row=1,column=1, padx=5,pady=35, sticky=W)


        # index 
        studentId_label = Label(left_frame,text="Index Number: ", font=("times new roman",13,"bold"))
        studentId_label.grid(row=0,column=0,padx=2, sticky=W)

        studentId_entry =ttk.Entry(left_frame, width=40,textvariable=self.var_std, font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1, padx=5,pady=35, sticky=W)   

        # Programme
        programme_label = Label(left_frame,text="Programme: ",font=("times new roman",13,"bold"))
        programme_label.grid(row=2,column=0,padx=2, sticky=W)

        programme_entry =ttk.Entry(left_frame, width=40,textvariable=self.var_prog, font=("times new roman",13,"bold"))
        programme_entry.grid(row=2,column=1, padx=5,pady=35, sticky=W)
   

        
        # take photo button
        TakePhoto_button = Button(left_frame,text="Take Photo Sample",command=self.generate_dataset, font=("times new roman",13,"bold"),bg='blue',fg='white')
        TakePhoto_button.place(x=200,y=280,width=170,height=40)

        # # Update photo button
        # UpdatePhoto_button = Button(left_frame,text="Update Photo Sample",font=("times new roman",13,"bold"),bg='blue',fg='white')
        # UpdatePhoto_button.place(x=300,y=280,width=180,height=40)
        

        # save button
        save_button = Button(left_frame,command=self.add_data, text="Save Details",font=("times new roman",13,"bold"),bg='blue',fg='white')
        save_button.place(x=5,y=350,width=110,height=40)

        # Update button
        update_button = Button(left_frame,text="Update Details",command=self.update_data, font=("times new roman",13,"bold"),bg='blue',fg='white')
        update_button.place(x=130,y=350,width=150,height=40)

        # delete button
        delete_button = Button(left_frame,text="Reset Details",command=self.reset, font=("times new roman",13,"bold"),bg='blue',fg='white')
        delete_button.place(x=300,y=350,width=150,height=40)

        





    # function declaration
    def add_data(self):
        if not self.var_name.get():
            msg.showerror("Error", "All field are required")
        elif not self.var_std.get():
            msg.showerror("Error", "All field are required")    
        elif not self.var_prog.get():
            msg.showerror("Error", "All field are required")
                
        else:
            try:
                conn = sqlite3.connect("Database.db")
                c = conn.cursor()
                c.execute("INSERT into StudentDetails (name,index_no,programme) values(?,?,?)",(self.var_name.get(),self.var_std.get(),self.var_prog.get()))
                conn.commit()
                conn.close()

                msg.showinfo("SUCCESS", "Student Details have been added successfully!")
            except sqlite3.IntegrityError:
                msg.showerror("Error","Details Already exist in Database!")
                
    # reset         
    def reset(self):
        self.var_name.set("")
        self.var_prog.set("")
        self.var_std.set("")
        return

    # update
    def update_data(self):
        if not self.var_name.get():
            msg.showerror("Error", "All field are required")
        elif not self.var_std.get():
            msg.showerror("Error", "All field are required")    
        elif not self.var_prog.get():
            msg.showerror("Error", "All field are required")
        else:
            update = msg.askyesno("Update","Do you want to update this student details")                  
            if update>0:
                conn = sqlite3.connect("Database.db")
                c = conn.cursor()
                c.execute("UPDATE StudentDetails SET name=?,programme=? WHERE index_no =?",(self.var_name.get(),self.var_prog.get(),self.var_std.get()))
                conn.commit()
                conn.close()
            else:
                if not update:
                    return
            msg.showinfo("Success","Student details successfully updated")        


    # generate dataset
    def generate_dataset(self):
        if not self.var_name.get():
            msg.showerror("Error", "All field are required")
        elif not self.var_std.get():
            msg.showerror("Error", "All field are required")    
        elif not self.var_prog.get():
            msg.showerror("Error", "All field are required")
        else:
            conn = sqlite3.connect('Database.db')
            if not os.path.exists('./dataset'):
                os.makedirs('./dataset')

            c = conn.cursor()
          		

            # CascadeClassifier
            face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')

            cap = cv2.VideoCapture(0)

            # taking student details
            Fullname = self.var_name.get()
            Index_number = self.var_std.get()
            Programme = self.var_prog.get()

            # initializing counter
            counter = 0

            while True:
                ret, img = cap.read()
                
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(gray,1.3,5)

                for (x,y,w,h) in faces:
                    counter += 1
                    cv2.imwrite(f"dataset/{Fullname}."+ str(Index_number) +"."+str(counter)+".jpg",gray[y:y+h,x:x+w])
                    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)
                    cv2.waitKey(100)
                cv2.imshow('img',img)
                if cv2.waitKey(10)== ord('q'):
                    break

                if counter == 100:
                    break
            cap.release()
            conn.commit()
            conn.close()
            cv2.destroyAllWindows()
            msg.showinfo("Result","Generating datasets completed!!!")
if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()