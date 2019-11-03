from tkinter import *

my = "Click me"


window = Tk()
window.title("Window app")
window['width'] = 500
window['height'] = 500
window['bg'] = "skyblue"
label = Label(window)
label['text'] = "List of values"
label.pack()
button = Button(window)
button['text'] = my
button.pack()
window.mainloop()