from components import AbstractComponent
from components import LabelComponent
import re

componentDictionary = {
    "Label": "Label",
    "Line": "Entry"
}


class TkComponentGenerator:
    def __init__(self):
        self.component = None
        self.code = ""

    def genInitial(self):
        if type(self.component) is LabelComponent:
            self.code += self.component.name + " = Label()"
            self.code += "\n"

    def genProperties(self):
        properties = ""
        properties += self.component.name + "['text'] = " + self.component.caption
        properties += "\n"

        self.code += properties

    def genPackLayout(self):
        layout = ""
        layout += self.component.name + ".pack()"
        layout += "\n"

        self.code += layout

    def genPlaceLayout(self):
        layout = ""

        layout += self.component.name + ".place("

        if self.component.x:
            layout += "x=" + str(self.component.x) + ","

        if self.component.y:
            layout += "y=" + str(self.component.y) + ","

        if self.component.relx:
            layout += "relx=" + str(self.component.relx) + ","

        if self.component.rely:
            layout += "rely=" + str(self.component.rely) + ","

        if self.component.anchor:
            layout += "anchor=" + self.component.anchor + ","

        if re.search(",", layout):
            layout = layout[:-1]
        layout += ")"
        layout += "\n"

        self.code += layout

    def generate(self):
        self.genInitial()
        self.genProperties()
        self.genPackLayout()
        self.genPlaceLayout()

        return self.code

    def __getitem__(self, item):
        return self.__dict__[item]