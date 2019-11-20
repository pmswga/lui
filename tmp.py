from tkinter import *

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


window = Tk()
window.title("Window app")
window['width'] = 500
window['height'] = 500
label_1 = Label(window)
label_1['text'] = "List values"
label_1.pack(side=LEFT)
label_2 = Label(window)
label_2['text'] = "list values"
label_2.pack(side=RIGHT)
listbox = Listbox(window)
for item in lst:
	listbox.insert(END, item)
listbox.pack()
window.mainloop()