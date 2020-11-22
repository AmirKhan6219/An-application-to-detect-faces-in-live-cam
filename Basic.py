#Installtion of libraries

#pip install cmake
#pip install dlib
#pip install face-recognition
#pip install numpy
#pip install opencv-python

#Import Libraries
import cv2
import numpy as np
import face_recognition

# A function to load Train Images
imgMSDhoni= face_recognition.load_image_file('Images/MSDhoni.jpg')

#Covert the image into RGB
imgMSDhoni= cv2.cvtColor(imgMSDhoni, cv2.COLOR_BGR2RGB)

# A function to load Test Images
imgTest= face_recognition.load_image_file('Images/MSDhoniTest.jpg')

#Covert the image into RGB
imgTest= cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

#Detect the Face by sending the Training image in the function and get the first element of this
faceLoc= face_recognition.face_locations(imgMSDhoni)[0]
print(faceLoc) # there are 4 values (top, right, bottom & left)

#Encode the face which has been detected and get the first element
encodeMsDhoni= face_recognition.face_encodings(imgMSDhoni)[0]

#To see the dected face
cv2.rectangle(imgMSDhoni, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,255), 2)

#Detect the Face by sending the Test image in the function and get the first element of this
faceLocTest= face_recognition.face_locations(imgTest)[0]

#Encode the face which has been detected and get the first element
encodeTest= face_recognition.face_encodings(imgTest)[0]

#To see the dected face
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255,0,255), 2)

#Comparing the ecoded train and test faces and
#Finding the distance between them
results= face_recognition.compare_faces([encodeMsDhoni], encodeTest)
faceDis= face_recognition.face_distance([encodeMsDhoni], encodeTest)
print(results, faceDis)

#Draw a Text Strings on the image
cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255), 2)

#Display the images on the window
cv2.imshow('MSDhoni', imgMSDhoni)
cv2.imshow('MSDhoniTest', imgTest)
cv2.waitKey(0) #Display the window infininitely until any keypress
