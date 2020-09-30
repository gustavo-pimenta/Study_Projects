from glob import glob
import image_processing

def ImportImage(Path):
    from PIL import Image
    import glob
    image_list = []
    for filename in glob.glob(Path +'/*.jpg'): #assuming gif
        im=Image.open(filename)        
        image_list.append(im)
    return image_list



image_processing.show(ImportImage(r'H:/OneDrive/IMAGENS/Pessoal'))

        