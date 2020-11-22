# Live Facial-Recognition using Python
1. Face-Recognition is a method of identifying or verifying the identity of an individual using their face. 
2. Face Recognition systems can be used to identify people in photos, video, or in real-time.
3. Law enforcement agencies use the technology to uncover criminals or to find missing children or seniors

Today, it’s used in a variety of ways from allowing you to unlock your phone, go through security at the airport, purchase products at stores, etc.

# Libraries
1. OpenCV
2. face-recognition-models
3. numpy
4. dlib

OpenCV is a huge open-source library for computer vision, machine learning, and image processing. 
It can process images and videos to identify objects, faces, or even the handwriting of a human.

# Steps used in this project.
1. Finding all the Faces
2. Posing and Projecting Faces
3. Encoding Faces
4. Finding the person’s name from the encoding
5. Storing the detected person's name and the time in Attendance.csv file.

# 1. Finding all the faces 
     Find all the list of faces.
     There are two file
     1. Images (It contains 3 images, one is Virat Kohli and the other two are of Mahendra Singh Dhoni).
     A) "MSDhoniTest" and "ViratKohli" named image is used for Testing, and
     B) "MSDhoni" is used for Training the image.
  
     2. ImagesAttendance (It contain 5 images named: "Harbhajan Singh", "Mark Zuckerberg", "MSDhoni", "Virat Kohli", and "You(me)")

# 2. Posing and Projecting Faces
     Draw the rectangle on the detected face.

# 3. Encode Face
     For face recognition, the algorithm notes certain important measurements on the face like the color and size and slant of eyes, 
     the gap between eyebrows, etc. All these put together define the face encoding the information obtained out of the image that is used to identify the particular face.

# 4. Finding the person name  the
     Obtaining the name of the person after successfully performing the encoding and finding the shortest distance between the actual image and detected images.

# 5. Storing the detected person name and the time in the Attendance.csv file
     Store the name and what time the person is detected in a CSV file named Attendance.csv.

# Technologies used
  1. Python 
  2. Machine Learning
