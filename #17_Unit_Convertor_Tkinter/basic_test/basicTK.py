import tkinter

window = tkinter.Tk()
window.title("Test")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label")
# This going to take the my_label and display in the middle of the screen with top margin  = 0
my_label.pack()

# Changing the text of my_label
# my_label["text"] = "New Text "
# or
# my_label.config(text="New Text")

# my_second_label = tkinter.Label(text="I am a Second Label", font=("Arial", 24, "bold"))
# my_second_label.pack(side="left")


from tkinter import *


def button_clicked():
    my_label["text"] = input.get()
    print("I got clicked")


button = Button(text="Click ME", command=button_clicked)  # or //--> button_one = tkinter.Button()
button.pack()

# Entry
input = Entry(width=10)
input.insert(END, string="Write 123")
#  Layout Manager
input.pack()
# input.place(x = int ,y = int)
# input.grid(column = int , row = int)

window.mainloop()
