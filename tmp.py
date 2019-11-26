from tkinter import *

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


window = Tk()
window.title("Window app")
window['width'] = 150
window['height'] = 200
button = Button(window)
button['text'] = "Click"
button.pack()
window.mainloop()