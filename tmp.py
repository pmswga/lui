from tkinter import *

window = Tk()
window.title("Window app")
window['width'] = 200
window['height'] = 200
button = Button(window)
button['text'] = "Click"
button.pack()
label['text'] = "It's mine label"
label.pack()
label.place(x=100,y=100)

window.mainloop()