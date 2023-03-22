# Text-Recognition-Model
## Problem Statement
The task of text recognition from images is a challenging problem in the field of computer vision. Despite the recent advancements, accurately recognizing text from images still remains a difficult task due to various factors such as image quality, font style, and lighting conditions. The problem is further compounded when the text is in handwritten form, where variations in writing styles and individual idiosyncrasies make it even more challenging. Therefore, the development of an efficient and accurate text recognition model is essential for many real-world applications, such as automatic license plate recognition, document digitization, and text translation. The primary goal of this project is to develop a robust text recognition model that can accurately recognize text from images under varying conditions, including different font styles, text sizes, and backgrounds, to improve the efficiency and accuracy of text recognition systems.
## Data Information
The test images are given along with the code.

There are three test images each with varying noise and distortions with 1.png having the least and 3.png having the most.
## Project Pipeline
* Understanding the Images: We look at the images and understand what kind of prcoessing needs to be done on the images so that it is easier for the model to understand.
* Image Preprocessing: Image preprocessing is the essential step of cleaning and transforming raw images to make it suitable for OCR model. For the current set of images, we resize and use a custom function noise_remove() to remove most of the noise in the images. Other denoising functions are used to obtain the final image which can be fed to the model.
* Model Output: The model outputs the recognized text and the final processed image with each word enclosed in a box for better understanding.
