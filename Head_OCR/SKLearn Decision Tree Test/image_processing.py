from PIL import Image 
import numpy as np 
import matplotlib.pyplot as plt
import resizeimage
import os

def open_color(file_name): # open an image with the original colors
    image = Image.open(file_name)
    return image
 
def open_gray(file_name): # open an image in gray scale
    image = Image.open(file_name).convert('LA')
    return image

def resize(image): # set the size 1024x1024
    resized = resizeimage.resize_cover(image, [1024, 1024]) #validade = False
    return resized

def grayscale(image): #Function responsible for converting the colors of the image to black and white. Colors based on the RGB parameter.
    coluna=0 #image column
    linha=0 #Imagem Line
    width, height = image.size
    print('LOADING', end="")
    while coluna < width:
        while linha < height:
            pixel = image.getpixel((linha,coluna))
            R = pixel[0]
            G = pixel[1]
            B = pixel[2]
            pixel = round((R+G+B)/3)
            image.putpixel((linha,coluna), (pixel,pixel,pixel))
            linha+=1
        coluna+=1
        linha=0
        print('.', end="")
    return image

def show(matrix): # show the current image
    plt.figure(figsize=(5,5))
    plt.imshow(matrix, aspect='auto')
    plt.axis('off')
    plt.show()

def save(image, name): # save the current image
    name=(str(name)+'.jpg')
    plt.figure(figsize=(5,5))
    plt.imshow(image, aspect='auto')
    plt.axis('off')
    plt.savefig(name, format='jpg', bbox_inches='tight', pad_inches = 0)
    
def image_to_matrix(image): 
    # image = np.asarray(image, dtype=np.float32)/255 # turn into a matrix 0 to 1
    matrix = np.asarray(image, dtype=np.float32) # turn into a matrix 0 to 255
    return matrix

def matrix_size(matrix):
    try:
        print('linha = ',len(matrix))
    except:
        print('LINE ERROR')
    try:    
        print('coluna = ',len(matrix[0]))
    except:
        print('COLUMN ERROR')
    try:
        print('camada = ',len(matrix[0][0]))
    except:
        print('LAYER ERROR')
        
def threeD_twoD(matrix):
    matrix = matrix[:,:,0]
    return matrix

def twoD_oneD(matrix):
    lista = []
    for linha in matrix:
        for coluna in linha:
            lista.append(coluna)
    return lista