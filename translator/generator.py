# Generator

from translator.syntaxer import ComponentNode


# TODO: ПЕРЕПИСАТЬ ВСЁ К ЧЕРТЯМ СОБАЧИМ!

class TkGenerator:
    def __init__(self,):
        self.st = None
        self.code = []
        self.locals = {}
        self.user_code = ""

    def debug(self):
        print("Locals:")
        print(self.locals)
        print("User code:")
        print(self.user_code)

    def isList(self, lst):
        return isinstance(lst, list)

    def getList(self, component):

        dataProperty = None
        for property in component.properties.keys():
            if property == "data":
                dataProperty = self.locals[component.properties[property]]

        self.code.append("listbox = Listbox(window)")

        if isinstance(dataProperty, list):
            self.code.append("for item in " + component.properties[property] + ":")
            self.code.append("\tlistbox.insert(END, item)")

        self.code.append("listbox.pack()")

    def genButton(self, component):

        self.code.append("button = Button(window)")
        for property in component.properties.keys():
            if property == "caption":
                self.code.append("button['text'] = " + component.properties.get(property))
        self.code.append("button.pack()")

    def genLabel(self, component):
        self.code.append("label = Label(window)")

        for property in component.properties.keys():
            if property == "caption":
                self.code.append("label['text'] = " + component.properties.get(property))

        self.code.append("label.pack()")

    def genWindow(self):

        for property in self.st.properties.keys():
            if property == "title":
                self.code.append("window.title(" + self.st.properties[property] + ")")
            elif property == "width":
                self.code.append("window['width'] = " + str(self.st.properties[property]))
            elif property == "height":
                self.code.append("window['height'] = " + str(self.st.properties[property]))
            elif property == "background-color":
                self.code.append("window['bg'] = " + str(self.st.properties[property]))

        for component in self.st.components:
            if component.name == "Label":
                self.genLabel(component)
            if component.name == "Button":
                self.genButton(component)
            if component.name == "List":
                self.getList(component)

    def generate(self):
        if self.st is not None:
            self.code.append(self.user_code)

            exec("import sys")
            exec("sys.path.append(\".\")")
            exec(self.user_code)
            self.locals = locals()

            self.code.append("from tkinter import *")
            self.code.append("window = Tk()")

            self.genWindow()

            self.code.append("window.mainloop()")

            with open("tmp.py", "w") as f:
                f.write("\n".join(self.code))
        else:
            raise Exception("Generate code error")