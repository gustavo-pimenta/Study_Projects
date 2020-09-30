import image_processing as ip

# open and save the images
x=1
while x<=10:

    file=str(x)+'.jpg'
    image=ip.open_gray(file)
    name=str(x)
    # ip.show(image)
    ip.save(image, name)

    x+=1