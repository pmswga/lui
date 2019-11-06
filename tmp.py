
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


from tkinter import *
window = Tk()
window.title("Window app")
window['width'] = 500
window['height'] = 500
label = Label(window)
label['text'] = "List values"
label.pack()
listbox = Listbox(window)
for item in lst:
	listbox.insert(END, item)
listbox.pack()
window.mainloop()