# Live Facial-Recognition in Machine Learning

# Installtion of libraries
1. pip install cmake
2. pip install dlib
3. pip install face-recognition
4. pip install numpy
5. pip install opencv

# Step 1: Loading the Images and converting it into RGB
We are finding all the images which is located in Images folder.
We have two Images.
1. Virat Kohli
2. Mahendra Sing Dhoni 
we have two images for Mahendra singh dhoni, one for training and another one for testing and we also use the 1st image(Virat Kohli) for testing.
We have to convert the BGR images into RGB as librararis understands the RGB.

# Step 2: Finding the faces in our Image and Finding there encoding as well
We are using the face_recognition.face_location(Train_image) function to get location of faces, and face_recognition.face_encoding(Train_image) 
function to do the encoding. 
We are using the cv2.rectangle() function to draw the rectange on the faces.
We can see the detected faces by using cv2.imshow() function.

Same we can do for testing.

# Step 3: Comparing the faces and finding the distance between them 
We are using the face_recognition.compare_faces([encodeTarain], encodeTest) to compare the both image. If the both 
faces match it will return True else False if they do not image.

In order to find how similar the both images are, we are using face_recognition.face_distance() to find the face distance.
The Lower the distance the better the match is.
