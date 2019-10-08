from tkinter import *

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

root = Tk()
root.title("Title")
root.geometry("150x150");

label = Label(width=20)
label['text'] = "It's mine label"

lbox = Listbox(width=15, height=8)

for i in lst:
    lbox.insert(0, i)


label.pack()
lbox.pack()

root.mainloop()