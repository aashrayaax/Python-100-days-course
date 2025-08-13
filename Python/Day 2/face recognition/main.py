import cv2
import os
import sys

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Loading The Cascade File
cascade_path = os.path.join(current_dir, 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(cascade_path)

if face_cascade.empty():
    print("Error: Could not load cascade classifier")
    print(f"Looking for file at: {cascade_path}")
    sys.exit(1)

# Reading the Input Image
image_path = os.path.join(current_dir, 'test_image.png')
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Could not read image file at {image_path}")
    sys.exit(1)

if image is None:
    print("Error: Could not read image file")
    print(f"Looking for file at: {image_path}")
    sys.exit(1)

# Resizing the Image
img = cv2.resize(image, None, fx=0.3, fy=0.3)

#Converting the image into grayscale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detecting The Faces
faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)

#Pointing The Faces
for (x,y,w,h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

#Displaying The Output Image
cv2.imshow('img', img)
cv2.waitKey()