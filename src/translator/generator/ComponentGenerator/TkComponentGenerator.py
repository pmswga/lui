from components.FormComponent import *
from components.LayoutComponent import *
from components.InputComponent import *
from components.OutputComponent import *
import re

componentDictionary = {
    "Window": "Tk",
    "Grid": "Frame",
    "Frame": "Frame",
    "Button": "Button",
    "Line": "Entry",
    "Label": "Label",
}


class TkComponentFactory:
    @staticmethod
    def get(componentName):
        if componentName == "Window":
            return WindowComponent()
        elif componentName == "Grid":
            return GridComponent()
        elif componentName == "Frame":
            return FrameComponent()
        elif componentName == "Label":
            return LabelComponent()
        elif componentName == "Button":
            return ButtonComponent()


class TkComponentGenerator:
    def __init__(self, component=None, parent=None):
        self.component = component
        self.parent = parent
        self.code = ""

    def genInitial(self):
        self.code += self.component.name + "=" + componentDictionary[self.component.component]
        if self.parent:
            self.code += "(" + self.parent.name + ")"
        else:
            self.code += "()"

        self.code += "\n"

    def genProperties(self):
        properties = ""

        if self.component.width:
            properties += self.component.name + "['width'] = " + str(self.component.width)
            properties += "\n"

        if self.component.height:
            properties += self.component.name + "['height'] = " + str(self.component.height)
            properties += "\n"

        if self.component.background_color:
            properties += self.component.name + "['bg'] = " + str(self.component.background_color)
            properties += "\n"

        if isinstance(self.component, LabelComponent):
            properties += self.component.name + "['text'] = " + self.component.caption
            properties += "\n"

        if isinstance(self.component, ButtonComponent):
            properties += self.component.name + "['text'] = " + self.component.caption
            properties += "\n"

        self.code += properties

    def genPackLayout(self):
        layout = ""
        layout += self.component.name + ".pack("

        if self.component.position:
            layout += "side=" + self.component.position + ","
            layout += "\n"

        if re.search(",", layout):
            layout = layout[:-1]

        layout += ")"
        layout += "\n"

        self.code += layout

    def genGridLayout(self):
        layout = ""

        layout += self.component.name + ".grid("

        if self.parent.rows:
            layout += "row=" + str(self.parent.rows) + ","

        if self.parent.cols:
            layout += "column=" + str(self.parent.cols) + ","

        if re.search(",", layout):
            layout = layout[:-1]
        layout += ")"
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

        if self.component.x or self.component.y:
            self.genPlaceLayout()

        self.genPackLayout()

        return self.code

    def __getitem__(self, item):
        return self.__dict__[item]
