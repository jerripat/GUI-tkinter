from cgitb import text
from tkinter import *

root = Tk()
root.title("My Menu")
root.geometry("500x500")

# Create clicked function
def clicked():
    app1_label = Label(root, text="You clicked the button!").pack()

# Create Labels
my_label =Label(root, text="Apps to open", fg="#3437eb", font=("Helvetica", 25))
my_label.pack(pady=10)
app1_label =Label(root, text="Open Python", relief="groove", fg="#2da61f", font=("Helvetica", 20),height=2,width=15)
app1_label.pack()

# pack Options 
app2_label =Label(root, text="Open .bashrc", relief="groove", fg="#2da61f", font=("Helvetica", 20),height=2,width=15)
app2_label.pack()

# Create buttons
my_button = Button(root, text="Open sub-menu", command=clicked)
my_button.pack(pady=20)






root.mainloop()