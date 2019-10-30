from tkinter import *
window = Tk()
window.title("Window app")
window['width'] = 500
window['height'] = 500
label = Label(window)
label['text'] = "Hello, Lui"
label.pack()
window.mainloop()