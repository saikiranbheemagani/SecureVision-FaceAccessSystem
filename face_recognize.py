import sys
import cv2
import numpy as np
import os
from tkinter import messagebox

def recognize_faces():
    size = 4
    p = os.getcwd()
    datasets = os.path.join(p, 'datasets')
    haar_file = os.path.join(p, 'haarcascade_frontalface_default.xml')
    (images, labels, names, id) = ([], [], {}, 0)

    for subdir in os.listdir(datasets):
        names[id] = subdir
        subject_path = os.path.join(datasets, subdir)
        for filename in os.listdir(subject_path):
            path = os.path.join(subject_path, filename)
            label = id
            images.append(cv2.imread(path, 0))
            labels.append(int(label))
        id += 1

    (width, height) = (130, 100)
    (images, labels) = [np.array(lst) for lst in [images, labels]]

    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(images, labels)
    face_cascade = cv2.CascadeClassifier(haar_file)

    cap = cv2.VideoCapture(0)  # Use default camera (laptop camera)

    recognized_faces = set()  # To store recognized faces

    while True:
        ret, im = cap.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (width, height))

            prediction = model.predict(face_resize)
            print('prediction:', prediction)

            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
            print(prediction)

            if prediction[1] < 70:
                person_name = names[prediction[0]]
                if person_name not in recognized_faces:
                    welcome_message = f"Face matched, welcome {person_name}"
                    messagebox.showinfo("Face Recognition", welcome_message)
                    cap.release()
                    cv2.destroyAllWindows()
                    return
                else:
                    break
            else:
                cv2.putText(im, 'Intruder detected, alerting security', (x - 10, y - 10),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
                cv2.imshow("OpenCV", im)
                # cv2.waitKey(5000)  # Add a 5-second delay
                # cap.release()
                # cv2.destroyAllWindows()
                # sys.exit()
                # break

        cv2.imshow("OpenCV", im)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_faces()
