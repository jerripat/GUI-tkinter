from tkinter import *
from PIL import Image

imgFile = 'linux.png'

def convertPNG(imgfile):


#filen = r'linux.png'
    filen = imgfile  
    img = Image.open(filen)
    img.save('linux2.ico', format = 'ICO', sizes=[(32,32)])
    print(filen)

convertPNG(imgFile)