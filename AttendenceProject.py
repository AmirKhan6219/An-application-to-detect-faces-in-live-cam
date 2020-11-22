import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

#Path where the Image is located
path= 'ImagesAttendance'

images=[]
classNames= []
myList= os.listdir(path) # Grab the list of image from 'ImageAttendance' folder
print(myList)

#read the image one by one
for ele in myList:
    currImg= cv2.imread(f'{path}/{ele}') #Read Current Image, eg. 1. Harbhajan Singh.jpg
    images.append(currImg) #Append current images in the list 'images'
    classNames.append(os.path.splitext(ele)[0]) #Remove jpg and append only name in list 'classNames', eg. Harbhajan Singh
print(classNames)

#A function to encode the Images
def findEncodings(images):
    encodeList= []
    for img in images:
        img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Convert the image in RGB
        encode = face_recognition.face_encodings(img)[0] #Encode the face which has been detected and get the first element
        encodeList.append(encode)
    return encodeList

#A function for what date and time the face is detected
def markAttendance(name):
    with open('Attendance.csv', 'r+') as f: #Read and Write the file 'Attendance.csv'
        myDataList= f.readlines() #Read all the current lines of the data
        nameList=[]

        #Append all the name in the list 'nameList'
        for line in myDataList:
            entry= line.split(',') #split the line based on ','
            nameList.append(entry[0])

        #Check if the current name is present or not if not then find the time
        if name not in nameList:
            now= datetime.now() #Get date and time
            dtString= now('%H:%M:%S') #get only time
            f.writelines(f'\n{name},{dtString}') #write the current name and time in the file


encodeListKnown= findEncodings((images))
print('Encoding Complete') #When encoding is done just print 'Encode Complete'

#Get a video capture object for the camera
cap= cv2.VideoCapture(0)

#Loop to get each frame one by one
while True:
    success, img = cap.read() # Read the frame
    imgSize= cv2.resize(img, (0,0), None, 0.25, 0.25) # reduce the size as 1/4th of images in order to speed-up
    imgSize= cv2.cvtColor(imgSize, cv2.COLOR_BGR2RGB) # Convert the image into RGB
    faceCurrFrame = face_recognition.face_locations(imgSize) #Find the location of Face and get the first element of this
    encodeCurrFrame = face_recognition.face_encodings(imgSize, faceCurrFrame) #Encode by passing small smages and Face Location

    #Find the Matches by passing all the faces and encoding
    for encodeFace, faceLoc in zip(encodeCurrFrame, faceCurrFrame):
        matches= face_recognition.compare_faces(encodeListKnown,encodeFace) #Compare the faces
        faceDis= face_recognition.face_distance(encodeListKnown, encodeFace) #Face distance
        print(faceDis)
        matchIndex= np.argmin(faceDis) #Get the minimum index

        #Write the Name of the person based on the matchIndex
        if matches[matchIndex]:
            name= classNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1= faceLoc  # assign the variable
            y1, x2, y2, x1= y1*4, x2*4, y2*4, x1*4  #Regain the actual value again which was reduced 1/4th size of the image

            # Draw a rectangle on original image
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)

            # Draw a Text Strings on the image
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            #Whenever find the currect face of the person call the 'markAttendance funtion'
            #to put the name and time of the currect detected face into the csv file
            markAttendance(name)

    #Display the image on window
    cv2.imshow('Webcam', img)
    cv2.waitKey(1) #Display the frame for only 1ms
