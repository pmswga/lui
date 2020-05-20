from tkinter import *

window_1 = Tk()
window_1.title("Window app")
frame_1=Frame(window_1)
frame_1['width'] = 200
frame_1['height'] = 200
frame_1.pack()

button_1=Button(frame_1)
button_1['text'] = "Click"
button_1.pack(side=LEFT,)

label_1=Label(frame_1)
label_1['text'] = "It's mine label"
label_1.place(x=100,y=100)
label_1.pack()

label_2=Label(window_1)
label_2['text'] = "Test"
label_2.pack()

window_1.mainloop()