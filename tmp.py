from tkinter import *
window = Tk()
window.title("Window")
window['width'] = 500
window['height'] = 500
label = Label(window)
label['text'] = "Hello, lui"
label.pack()
window.mainloop()