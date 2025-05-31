import cv2
import sys
import numpy
import os
from tkinter import *
from tkinter import messagebox

global sub_data, w

def end():
    w.destroy()

def create():
    sub_data = E.get()
    if len(sub_data) != 0:
        p = os.getcwd()
        f1 = os.path.join(p, r'datasets')
        haar_file = os.path.join(p, r'haarcascade_frontalface_default.xml')

        if not os.path.exists(f1):
            os.mkdir(f1)

        datasets = f1
        path = os.path.join(datasets, sub_data)

        if not os.path.isdir(path):
            os.mkdir(path)

        (width, height) = (130, 100)
        face_cascade = cv2.CascadeClassifier(haar_file)
        webcam = cv2.VideoCapture(0)
        count = 1

        while count <= 50:
            (_, im) = webcam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 4)

            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
                face = gray[y:y + h, x:x + w]
                face_resize = cv2.resize(face, (width, height))
                cv2.imwrite('%s/%s.png' % (path, count), face_resize)
                count += 1

            cv2.imshow('OpenCV', im)
            key = cv2.waitKey(10)

            if key == 27:
                break

        webcam.release()
        cv2.destroyAllWindows()
        end()
    else:
        messagebox.showerror('', 'Please Enter The Name')

w = Tk()
w.geometry('275x175')
Label().pack()
L = Label(w, text='Enter the name of the person').pack()
E = Entry(w)
E.pack()
Label().pack()
B = Button(w, text='Okay', command=create)
B.pack()
Label().pack()
Label(w, text='*The name given here gets saved as the folder' + "\n" +
              ' name of the training images of that person').pack()
Label().pack()
w.mainloop()
