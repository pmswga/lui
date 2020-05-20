# Generator

from translator.generator.ComponentGenerator.TkComponentGenerator import *
from components.OutputComponent import *

dicOfMatching = {
    "x": "x",
    "y": "y",
    "width": "width",
    "height": "height",
    "caption": "text",
    "background-color": "bg",
    "position": "side"

}

class TkGenerator:
    def __init__(self, ):
        self.st = None
        self.code = []
        self.locals = {}
        self.user_code = ""
        self.components_counter = {}
        self.tkGenerator = TkComponentGenerator()

    def debug(self):
        print("Locals:")
        print(self.locals)
        print("User code:")
        print(self.user_code)

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

    def generateComponent(self, component, parent=None):
        self.components_counter[component.name] = self.components_counter.get(component.name, 0) + 1
        generatedComponent = TkComponentFactory.get(component.name)

        generatedComponent.__dict__["component"] = component.name
        generatedComponent.__dict__["name"] = component.name.lower() + "_" + str(self.components_counter[component.name])

        for property in component.properties.keys():
            generatedComponent.__dict__[property] = component.properties.get(property)

        if not isinstance(generatedComponent, WindowComponent):
            tkGenerator = TkComponentGenerator(generatedComponent, parent)
            self.code.append(tkGenerator.generate())

        for subComponent in component.components:
            parentComponent = TkComponentFactory.get(component.name)
            parentComponent.name = component.name.lower() + "_" + str(self.components_counter[component.name])

            self.generateComponent(subComponent, parentComponent)

    def generate(self):
        if self.st is not None:
            self.code.append("from tkinter import *")
            self.code.append(self.user_code)
            self.code.append("window_1 = Tk()")

            if self.st.properties.get("title"):
                self.code.append("window_1.title(" + self.st.properties.get("title") + ")")

            if len(self.st.components) > 0:
                self.generateComponent(self.st)

            self.code.append("window_1.mainloop()")

            return self.code
        else:
            raise Exception("Generate code error")
