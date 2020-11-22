# Live Facial-Recognition in Machine Learning

1. Face-Recognition is a method of identifying or veryifying the identity of an individual using their face. 
2. Face Recognition systems can be used to identify people in photos, video, or in real time.
3. Law enforcement agencies use the technology to uncover criminals or to find missing children or seniors

Today, it’s used in a variety of ways from allowing you to unlock our phone, go through security at the airport, purchase products at stores, etc.

# OpenCV
The project is implemented using opencv python library.

OpenCV is a huge open-source library for computer vision, machine learning, and image processing.
OpenCV supports a wide variety of programming languages like Python, C++, Java, etc. 
It can process images and videos to identify objects, faces, or even the handwriting of a human.

# Face Recognition — Step by Step

# Step 1: Finding all the Faces
Find all the list of faces. Goal is to figure out how dark the current pixel is compared to the pixels directly surrounding it.
Repeat that process for every single pixel in the image, you end up with every pixel being replaced by an arrow. These arrows are called gradients and they show the flow from light to dark across the entire image.

To find faces in this HOG (A method invented in 2005 called Histogram of Oriented Gradients — or just HOG for short) image, all we have to do is find the part of our image that looks the most similar to a known HOG pattern that was extracted from a bunch of other training faces
