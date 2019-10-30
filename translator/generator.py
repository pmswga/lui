
#Generator

from translator.syntaxer import ComponentNode
from translator.syntaxer import ComponentProperty

class TkGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.code = []

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

        for component in self.ast.components:
            if component.name == "Label":
                self.genLabel(component)


    def generate(self):
        self.code.append("from tkinter import *")

        self.code.append("window = Tk()")

        self.genWindow()

        self.code.append("window.mainloop()")

        with open("tmp.py", "w") as f:
            f.write("\n".join(self.code))
