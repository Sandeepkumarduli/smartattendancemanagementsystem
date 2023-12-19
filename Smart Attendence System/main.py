from tkinter import *
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import FaceRecognitionApp

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Smart Attendance System")
        #first
        img = Image.open(r"college_images\2213.jpg")
        img = img.resize((500, 130), Image.LANCZOS)  
        self.photoimg = ImageTk.PhotoImage(img)
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=500, height=130)
        #second
        img1 = Image.open(r"college_images\2213.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)  
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lb1 = Label(self.root, image=self.photoimg1)
        f_lb1.place(x=500, y=0, width=500, height=130)
        #third
        img2 = Image.open(r"college_images\2213.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)  
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lb1 = Label(self.root, image=self.photoimg2)
        f_lb1.place(x=1000, y=0, width=500, height=130)
        
        img3 = Image.open(r"college_images/BG1223.png")
        img3 = img3.resize((1366, 768), Image.LANCZOS)  
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # bg Image
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1366, height=768)
        
        title_lb1 = Label(bg_img,text="SMART ATTENDENCE SYSTEM",font=("poppins",30,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=1366,height=45)
        #student button
        std_img_btn = Image.open(r"college_images\buttons.png")
        std_img_btn = std_img_btn.resize((200, 180), Image.LANCZOS)  
        self.photoimg4 = ImageTk.PhotoImage(std_img_btn)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_pannels,cursor="hand2")
        b1.place(x=100,y=100,height=180)

        std_b1 = Button(bg_img,text="STUDENT DETAILS",command=self.student_pannels,cursor="hand2",font=("poppins",15,"bold"),bg="black",fg="white")
        std_b1.place(x=100,y=100,width=205,height=40)
        
        #Detect Face button
        std_img_btn2 = Image.open(r"college_images\buttons.png")
        std_img_btn2 = std_img_btn2.resize((200, 180), Image.LANCZOS)  # Use Image.LANCZOS filter
        self.photoimg12 = ImageTk.PhotoImage(std_img_btn2)
        
        b1=Button(bg_img,command=self.face_rec,image=self.photoimg12,cursor="hand2")
        b1.place(x=400,y=100,height=180)

        std_b1 = Button(bg_img,command=self.face_rec,text="FACE DETECTOR",cursor="hand2",font=("poppins",15,"bold"),bg="black",fg="white")
        std_b1.place(x=400,y=100,width=205,height=40)
        
        
        #Attendence button
        std_img_btn3 = Image.open(r"college_images\buttons.png")
        std_img_btn3 = std_img_btn3.resize((200, 180), Image.LANCZOS)  
        self.photoimg5 = ImageTk.PhotoImage(std_img_btn3)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=700,y=100,height=180)

        std_b1 = Button(bg_img,text="ATTENDENCE",cursor="hand2",font=("poppins",15,"bold"),bg="black",fg="white")
        std_b1.place(x=700,y=100,width=205,height=40)
        
        #Help Desk button
        std_img_btn4 = Image.open(r"college_images\buttons.png")
        std_img_btn4 = std_img_btn4.resize((200, 180), Image.LANCZOS)  
        self.photoimg6 = ImageTk.PhotoImage(std_img_btn4)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=1000,y=100,height=180)

        std_b1 = Button(bg_img,text="HELP DESK",cursor="hand2",font=("poppins",15,"bold"),bg="black",fg="white")
        std_b1.place(x=1000,y=100,width=205,height=40)
        
        #Train Data button
        std_img_btn5 = Image.open(r"college_images\buttons.png")
        std_img_btn5 = std_img_btn5.resize((200, 180), Image.LANCZOS) 
        self.photoimg7 = ImageTk.PhotoImage(std_img_btn5)
        
        b1=Button(bg_img,command=self.train_data,image=self.photoimg7,cursor="hand2")
        b1.place(x=100,y=350,height=180)

        std_b1 = Button(bg_img,command=self.train_data,text="TRAIN DATA",cursor="hand2",font=("poppins",15,"bold"),bg="black",fg="white")
        std_b1.place(x=100,y=350,width=205,height=40)
        
        #Photos button
        std_img_btn6 = Image.open(r"college_images\buttons.png")
        std_img_btn6 = std_img_btn6.resize((200, 180), Image.LANCZOS)  # Use Image.LANCZOS filter
        self.photoimg8 = ImageTk.PhotoImage(std_img_btn6)
        
        b1=Button(bg_img,command=self.open_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=400,y=350,height=180)

        std_b1 = Button(bg_img,command=self.open_img,text="PHOTOS",cursor="hand2",font=("poppins",15,"bold"),bg="black",fg="white")
        std_b1.place(x=400,y=350,width=205,height=40)
        
        #Our Team button
        std_img_btn7 = Image.open(r"college_images\buttons.png")
        std_img_btn7 = std_img_btn7.resize((200, 180), Image.LANCZOS)  # Use Image.LANCZOS filter
        self.photoimg9 = ImageTk.PhotoImage(std_img_btn7)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=700,y=350,height=180)

        std_b1 = Button(bg_img,text="OUR TEAM",cursor="hand2",font=("poppins",15,"bold"),bg="black",fg="white")
        std_b1.place(x=700,y=350,width=205,height=40)
        
        #Exit button
        std_img_btn8 = Image.open(r"college_images\buttons.png")
        std_img_btn8 = std_img_btn8.resize((200, 180), Image.LANCZOS)  # Use Image.LANCZOS filter
        self.photoimg10 = ImageTk.PhotoImage(std_img_btn8)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=1000,y=350,height=180)

        std_b1 = Button(bg_img,text="EXIT",cursor="hand2",font=("poppins",15,"bold"),bg="black",fg="white")
        std_b1.place(x=1000,y=350,width=205,height=40)
        
    def open_img(self):
        os.startfile("Data")
        
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceRecognitionApp(self.new_window)
        
        
       
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
