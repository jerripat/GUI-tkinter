from tkinter import *
from PIL import ImageTk, Image
icoImg = '@linux.ico'
root = Tk()
root.title("My Menu")
root.geometry("500x500")
root.iconbitmap('linux.ico')
canvas = Canvas(root, width=500, height=500)
canvas.pack()

# Create clicked function
def clicked():
    input = e.get()
    app1_label = Label(root, text="Hello " + input)
    app1_label.pack()


# Add image
img = ImageTk.PhotoImage(Image.open(r'linux.ico'))
canvas.create_image(10, 10, anchor=NW, image=img)

# Create Labels
my_label =Label(root, text="Apps to open", fg="#3437eb", font=("Helvetica", 25))
my_label.pack(pady=10)
app1_label =Label(root, text="Enter filename to open", relief="groove", fg="#2da61f", font=("Helvetica", 15),height=2, width=30)
app1_label.pack()

# Create entry widget
e=Entry(root, width=25, font=("Helvetica", 15))
e.pack(pady=20)

# Create buttons
my_button = Button(root, text="Open sub-menu", command=clicked)
my_button.pack(pady=20)

root.mainloop()