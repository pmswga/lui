# Generator

from translator.syntaxer import ComponentNode
from translator.syntaxer import ComponentProperty


# TODO: ПЕРЕПИСАТЬ ВСЁ К ЧЕРТЯМ СОБАЧИМ!

class TkGenerator:
    def __init__(self, ast, other_code=""):
        self.ast = ast
        self.code = []
        self.other_code = other_code.split("\n")

    def isList(self, lst):
        return isinstance(lst, list)

    def getList(self, component):

        self.code.append("listbox = Listbox(window)")

        print(self.other_code[1])
        lst = eval(self.other_code[1].split("=")[1])

        if isinstance(lst, list):
            self.code.append("for item in " + component.properties[0].value + ":")
            self.code.append("\tlistbox.insert(END, item)")

        self.code.append("listbox.pack()")

    def genButton(self, component):
        self.code.append("button = Button(window)")
        self.code.append("button['text'] = " + component.properties[0].value)
        self.code.append("button.pack()")

    def genLabel(self, component):
        self.code.append("label = Label(window)")
        self.code.append("label['text'] = " + component.properties[0].value)
        self.code.append("label.pack()")

    def genWindow(self):

        for property in self.ast.properties:
            if property.name == "title":
                self.code.append("window.title(" + property.value + ")")
            elif property.name == "width":
                self.code.append("window['width'] = " + str(property.value))
            elif property.name == "height":
                self.code.append("window['height'] = " + str(property.value))
            elif property.name == "background-color":
                self.code.append("window['bg'] = " + str(property.value))

        for component in self.ast.components:
            if component.name == "Label":
                self.genLabel(component)
            if component.name == "Button":
                self.genButton(component)
            #if component.name == "List":
            #    self.getList(component)

    def generate(self):
        self.code.append("from tkinter import *")
        for line in self.other_code:
            self.code.append(line)

        self.code.append("window = Tk()")

        self.genWindow()

        self.code.append("window.mainloop()")

        with open("tmp.py", "w") as f:
            f.write("\n".join(self.code))
