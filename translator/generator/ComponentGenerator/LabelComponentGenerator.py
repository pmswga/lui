from translator.generator.ComponentGenerator.AbstractComponentGenerator import AbstractComponentGenerator
from components.LabelComponent import LabelComponent


class LabelComponentGenerator(AbstractComponentGenerator):
    def __init__(self, component: LabelComponent):
        super().__init__(component)
        self.code += self.component.name + " = Label()"
        self.code += "\n"

    def genProperties(self):
        properties = ""
        properties += self.component.name + "['text'] = " + self.component.caption
        properties += "\n"

        self.code += properties

    def genLayout(self):
        layout = ""
        layout += self.component.name + ".pack()"
        layout += "\n"

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
        self.genLayout()

        return self.code

    def __getitem__(self, item):
        return self.__dict__[item]
