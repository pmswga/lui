# Generator

dicOfMatching = {
    "x": "x",
    "y": "y",
    "width": "width",
    "height": "height",
    "caption": "text",
    "background-color": "bg",
    "position": "side"

}


# TODO: ПЕРЕПИСАТЬ ВСЁ К ЧЕРТЯМ СОБАЧИМ!

class TkGenerator:
    def __init__(self,):
        self.st = None
        self.code = []
        self.locals = {}
        self.user_code = ""
        self.components_counter = {}

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
        component_name = "label_" + str(self.components_counter.get(component.name))
        position_options = ""

        self.code.append(component_name + " = Label(window)")
        for property in component.properties.keys():
            if property == "position":
                position_options = "side=" + component.properties.get(property).upper()
            else:
                self.code.append(component_name + "['" + dicOfMatching[property] + "'] = " + component.properties.get(property))


        self.code.append(component_name + ".pack(" + position_options + ")")

    def genWindow(self):
        component_name = "window"

        for property in self.st.properties.keys():
            if property == "title":
                self.code.append(component_name + ".title(" + self.st.properties[property] + ")")
            elif property == "position":
                pass
            else:
                self.code.append(component_name + "['" + dicOfMatching[property] + "'] = " + str(self.st.properties[property]))

        for component in self.st.components:
            self.components_counter[component.name] = self.components_counter.get(component.name, 0) + 1;

            if component.name == "Label":
                self.genLabel(component)
            if component.name == "Button":
                self.genButton(component)
            if component.name == "List":
                self.getList(component)

    def generate(self):
        if self.st is not None:
            self.code.append("from tkinter import *")
            self.code.append(self.user_code)
            self.code.append("window = Tk()")

            self.genWindow()

            self.code.append("window.mainloop()")

            return self.code
        else:
            raise Exception("Generate code error")