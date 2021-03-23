# @date: 23.03.2021
# @author: Şükrü Erdem Gök
# @version: Python 3.8
# @os: Windows 10
# @github: https://github.com/SukruGokk

# Face detection

# Lib
import cv2
from sys import exit

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

# Always update
while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    coors = []

    # Draw the rectangle around each face
    for (i) in faces:
        coors.append(i)

    try:

        x = coors[0][0]
        y = coors[0][1]

        w = coors[0][2]
        h = coors[0][3]

        cv2.rectangle(img, (x, y), (x + w, y+h), (255, 0, 0), 3)

        face_crop = []
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face_crop.append(img[y:y + h, x:x + w])

        for face in face_crop:
            cv2.imshow(face)

    except:pass

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

exit(0)
# Release the VideoCapture object
cap.release()
