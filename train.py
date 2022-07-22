from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox as msg
import cv2
import numpy as np 
import os



class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1540x850")
        self.root.title("Face Recognition System")

        # title
        title_lbl = Label(self.root, text="KWAME NKRUMAH UNIVERSITY OF SCIENCE AND TECHNOLOGY",font=("Montserrat",30,"bold"),bg="white",fg="gold")
        title_lbl.place(x=0,y=0,width=1360,height=120)


        
        # background image
        img3 = Image.open('./Images/students.jpg')
        img3_resize = img3.resize((1530,640), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3_resize)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=110,width=1530,height=700)

        titel_lbl = Label(bg_img, text="TRAINING DATASETS",font=("times new roman",25,"bold"),bg="white",fg="blue")
        titel_lbl.place(x=-100,y=0,width=1530,height=60)
       
        # # button
        b1_1 = Button(self.root,text='Train Datasets',cursor='hand2',command=self.train_classifier, font=("times new roman",20,"bold"),bg="red",fg="white")
        b1_1.place(x=500,y=440,width=400,height=50)


    if not os.path.exists('./recognizer'):
        os.makedirs('./recognizer')

    def train_classifier(self):
        data_dir = ("dataset")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")  #gray scale image
            imageNp = np.array(img, "uint8")
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("training", imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.save("recognizer/trainingData.yml")
        cv2.destroyAllWindows()
        msg.showinfo("Result", "Training dataset completed!!!")


    # def getImagesWithID(self):
    #     imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    #     faces = []
    #     IDs = []
    #     for imagePath in imagePaths:
    #         faceImg = Image.open(imagePath).convert('L')
    #         faceNp = np.array(faceImg,'uint8')
    #         ID = int(os.path.split(imagePath)[-1].split('.')[1])
    #         print(ID)
    #         faces.append(faceNp)
    #         IDs.append(ID)
    #         cv2.imshow("training",faceNp)
    #         cv2.waitKey(10)
    #     return np.array(IDs), faces

    #     IDs, faces = getImagesWithID(path)
    #     recognizer = cv2.face.LBPHFaceRecognizer_create()
    #     recognizer.train(faces,IDs)
    #     recognizer.save('recognizer/trainingData.yml')
    #         # msg.showinfo("Results","Training datasets Completed!!!")   
    #     cv2.destroyAllWindows()

if __name__ == '__main__':
    root = Tk()
    obj = Train(root)
    root.mainloop()