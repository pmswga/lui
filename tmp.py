import lst
import random

listModel   = lst.List()
lstPositive = lst.List()
lstOther    = lst.List()

for i in range(10):
    listModel.append( float(random.randint(-100, 100)) )

for index in range(listModel.size):
    if listModel.at(index) > 0:
        lstPositive.append(listModel.at(index))
    else:
        lstOther.append(listModel.at(index))

list_s = []
list_p = []
list_o = []

for i in range(listModel.size):
    list_s.append(listModel.at(i))

for i in range(lstPositive.size):
    list_p.append(lstPositive.at(i))

for i in range(lstOther.size):
    list_o.append(lstOther.at(i))


from tkinter import *
window = Tk()
window.title("Lab 1")
label = Label(window)
label['text'] = "Source list"
label.pack()
listbox = Listbox(window)
for item in list_s:
	listbox.insert(END, item)
listbox.pack()
window.mainloop()