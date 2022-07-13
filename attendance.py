from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox as msg
from openpyxl import Workbook
import cv2
import numpy as np 
import os
import sqlite3
import datetime
from datetime import date
import time
import pandas as pd
import csv
from tkinter import filedialog
from send import Message

mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x850")
        self.root.title("Face Recognition System")

        
        #variables
        self.var_std_index=StringVar()
        self.var_std_name=StringVar()
        self.var_std_program=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_status=StringVar()

        # background image
        img3 = Image.open('C:/Users/adoma/Desktop/another_/opencv_face_recognition-master/Tkinter/Images/bg.jpg')
        img3_resize = img3.resize((1530,640), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3_resize)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=650)

        title_lbl = Label(bg_img, text="ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="red",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=55)

        # main frame
        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=0,y=55,width=1530,height=600)

        # left label frame
        left_frame = LabelFrame(main_frame, bd=3, relief=RIDGE,text='Student Details',font=("times new roman",20,"bold"))
        left_frame.place(x=0,y=10,width=600,height=500)

        # label and entry details
        # student name
        fullname_label = Label(left_frame,text="Full Name: ",font=("times new roman",13,"bold"))
        fullname_label.grid(row=0,column=0,sticky=W, pady=10)

        
        fullname_entry =ttk.Entry(left_frame, width=40,textvariable=self.var_std_name, font=("times new roman",13,"bold"))
        fullname_entry.grid(row=0,column=1, padx=5,pady=10, sticky=W)

        # index 
        studentId_label = Label(left_frame,text="Index Number: ", font=("times new roman",13,"bold"))
        studentId_label.grid(row=1,column=0,padx=2, sticky=W)

        studentId_entry =ttk.Entry(left_frame, width=40,textvariable=self.var_std_index, font=("times new roman",13,"bold"))
        studentId_entry.grid(row=1,column=1, padx=5,pady=30, sticky=W)   

        # Programme
        programme_label = Label(left_frame,text="Programme: ",font=("times new roman",13,"bold"))
        programme_label.grid(row=2,column=0,padx=2, sticky=W)

        programme_entry =ttk.Entry(left_frame, width=40,textvariable=self.var_std_program, font=("times new roman",13,"bold"))
        programme_entry.grid(row=2,column=1, padx=5,pady=30, sticky=W)

        #Date
        dateLabel=Label(left_frame,text="Date: ",font=("times new roman",13,"bold"))
        dateLabel.grid(row=3,column=0,padx=2, sticky=W)

        atten_date=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        atten_date.grid(row=3,column=1,pady=20,sticky=W)

        #attendance status
        dateLabel=Label(left_frame,text="Attendance Status: ",font=("times new roman",13,"bold"))
        dateLabel.grid(row=3,column=0,padx=2, sticky=W)

        atten_date=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_status,font=("times new roman",13,"bold"))
        atten_date.grid(row=3,column=1,pady=20,sticky=W)

        #buttonsframe
        btn_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=35,y=320,width=490,height=35)

        # import button
        import_btn=Button(btn_frame,text="Import Excel File",command=self.importExcel, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        # Send Via Email button
        send_btn=Button(btn_frame,text="Send Via Email",width=17,command=self.send_message, font=("times new roman",13,"bold"),bg="blue",fg="white")
        send_btn.grid(row=0,column=1)

        # reset button
        reset_btn=Button(btn_frame,text="Reset",width=15,command=self.reset_data, font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=2)



        #right label frame
        Right_frame=LabelFrame(main_frame,bd=3,relief=RIDGE,text="Attendance Details",font=("times new roman",20,"bold"))
        Right_frame.place(x=620,y=10,width=730,height=500) 

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=7,y=5,width=710,height=455)

       
        #scroll bar table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

       
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","name","programme","time","date","attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        self.AttendanceReportTable.heading("id",text="Index Number")
        self.AttendanceReportTable.heading("name",text="Student Name")
        self.AttendanceReportTable.heading("programme",text="Programme")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("programme",width=100)
        self.AttendanceReportTable.column("time",width=60)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind ("<ButtonRelease>",self.get_cursor)

      


    #fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import excel
    def importExcel(self):
        global mydata
        mydata.clear()
        file=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open ExcelFile",filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent=self.root)
        with  open(file) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in  csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # get cursor 
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_std_index.set(rows[0])
        self.var_std_name.set(rows[1])
        self.var_std_program.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_status.set(rows[5])


    # reset function
    def reset_data(self):
        self.var_atten_date.set("")
        self.var_atten_time.set("")
        self.var_std_index.set ("")
        self.var_std_name.set("")
        self.var_std_program.set("")
        self.var_atten_status.set("")

    def send_message(self):
        self.new_window = Toplevel(self.root)
        self.app = Message(self.new_window)
        self.new_window.grab_set()    

if __name__ == '__main__':
    root = Tk()
    obj = Attendance(root)
    root.mainloop()        