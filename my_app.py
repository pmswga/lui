from tkinter import *

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


window = Tk()
window.title("Window app")
window['width'] = 200
window['height'] = 200
button = Button(window)
button['text'] = "Click"
button.pack()
label = Label()
label['text'] = "It's mine label"
label.pack()
label.place(x=100,y=100)

listbox = Listbox(window)
for item in lst:
	listbox.insert(END, item)
listbox.pack()
window.mainloop()