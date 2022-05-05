from cgitb import text
from tkinter import *
from PIL import Image

# filen = r'linux.png'
# img = Image.open(filen)
# img.save('linux.ico', format = 'ICO', sizes=[(16,16)])
root = Tk()
root.title("My Menu")
root.geometry("500x500")

img = PhotoImage(file='linux.ico')
root.tk.call('wm', 'iconphoto', root._w, img)

# Create clicked function
def clicked():
    input = e.get()
    app1_label = Label(root, text="Hello " + input)
    app1_label.pack()

# Add image
#img = PhotoImage(file='Linux-icon.png')
#root.tk.call('wm', 'iconphoto', root._w, img)
# Create Labels
my_label =Label(root, text="Apps to open", fg="#3437eb", font=("Helvetica", 25))
my_label.pack(pady=10)
app1_label =Label(root, text="Enter filename to open", relief="groove", fg="#2da61f", font=("Helvetica", 15),height=2, width=30)
app1_label.pack()

# Create entry widget
#e = Entry(root, width=25, font=("Helvetica", 20))
e=Entry(root, width=25, font=("Helvetica", 15))
e.pack(pady=20)

# Create buttons
my_button = Button(root, text="Open sub-menu", command=clicked)
my_button.pack(pady=20)






root.mainloop()