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
        title_lbl = Label(self.root, text="TRAIN DATASETS",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=55)

       

        # image top label
        img_top = Image.open('./Images/face_recog_3.png')
        img_top = img_top.resize((1500,300), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        bg_img = Label(self.root, image=self.photoimg_top)
        bg_img.place(x=0,y=55,width=1500,height=300)

        # button
        b1_1 = Button(self.root,text='TRAIN DATA',cursor='hand2',command=self.train_classifier, font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=350,width=1530,height=50)


        # image buttom label
        img_bottom = Image.open('./Images/training1.jpg')
        img_bottom = img_bottom.resize((1500,300), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        bg_img = Label(self.root, image=self.photoimg_bottom)
        bg_img.place(x=0,y=400,width=1500,height=300)

    # # Training codes
    # global path
    # path = 'dataset'
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