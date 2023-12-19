import tkinter as tk
from tkinter import Button, Label
from PIL import Image, ImageTk
import cv2
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Panel")
        
        self.create_gui()

    def create_gui(self):
        # Header image
        header_image = Image.open("college_images/2213.jpg")
        header_image = header_image.resize((1366, 130), Image.LANCZOS)
        self.header_photo = ImageTk.PhotoImage(header_image)
        header_label = Label(self.root, image=self.header_photo)
        header_label.place(x=0, y=0, width=1366, height=130)

        # Background image
        background_image = Image.open("college_images/BG1223.png")
        background_image = background_image.resize((1366, 768), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(background_image)
        background_label = Label(self.root, image=self.background_photo)
        background_label.place(x=0, y=130, width=1366, height=768)

        # Title section
        title_label = Label(background_label, text="FACE RECOGNITION PANEL", font=("poppins", 30, "bold"), bg="white", fg="black")
        title_label.place(x=0, y=0, width=1366, height=45)

        # Face Detector Button
        face_detector_button = Button(background_label, text="Face Detector", command=self.face_recognition, cursor="hand2",
                                      font=("poppins", 15, "bold"), bg="white", fg="black")
        face_detector_button.place(x=600, y=350, width=180, height=45)
        
    def mark_attendance(self, i, r, n):
        # Implement attendance marking logic here
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list) and (r not in name_list) and (n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")
        
        
     
    def face_recognition(self):
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face_LBPHFaceRecognizer.create()
        clf.read("clf.xml")
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = self.recognize(img, clf, face_cascade)
            cv2.imshow("Face Detector", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

    def draw_boundray(self, img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])

            confidence = int(100 * (1 - predict / 300))

            conn = mysql.connector.connect(user='root', password='Sandy@3246', host='localhost',
                                           database='studentdatabase', port=3306)
            cursor = conn.cursor()

            cursor.execute("select Name from student where Student_ID =" + str(id))
            n = cursor.fetchone()
            if n is not None:
                n = n[0]

            cursor.execute("select Roll_No from student where Student_ID=" + str(id))
            r = cursor.fetchone()
            if r is not None:
                r = r[0]

            cursor.execute("select Student_ID from student where Student_ID=" + str(id))
            i = cursor.fetchone()
            if i is not None:
                i = i[0]
            

            if confidence > 77:
                cv2.putText(img,f"Student_ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                cv2.putText(img,f"Roll_No:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                self.mark_attendance(i,r,n)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

    def recognize(self, img, clf, faceCascade):
        self.draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
        return img

    """def mark_attendance(self, student_id, roll_no, name):
        # Implement attendance marking logic here
        pass"""
        


if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()


