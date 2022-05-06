from tkinter import *
from PIL import Image

imgFile = 'linux.png'

def convertPNG(imgfile):


#filen = r'linux.png'
    filen = imgfile  
    img = Image.open(filen)
    img.save('linux.ico', format = 'XBM', sizes=[(16,16)])
    print(filen)

convertPNG(imgFile)