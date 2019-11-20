
from tkinter import *

window = Tk()

label = Label()
label['text'] = "Hello"


print(label.keys())

button = Button()

label.pack(side=RIGHT, padx=2, pady=2)
button.pack()

window.mainloop()

