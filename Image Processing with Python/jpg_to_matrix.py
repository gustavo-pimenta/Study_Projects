from PIL import Image 
import numpy as np 

#read the image 
image = Image.open("image.jpg")

def jpg_to_matrix(image):

    # transform the image into a matrix 
    matrix = np.asarray (image, dtype=np. float32) /255
    return matrix

matrix = jpg_to_matrix(image)