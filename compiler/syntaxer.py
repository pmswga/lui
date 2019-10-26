from compiler.lexer import *
from enum import Enum

class ComponentProperty:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return self.name + " " + str(self.value)


class ComponentNode:
    def __init__(self, name, properties, components=None):
        if components is None:
            components = []
        self.name = name
        self.properties = properties
        self.components = components

    def toString(self, i):
        string = self.name

        for property in self.properties:
            string += "\n"
            for t in range(i):
                string += "\t"
            string += "Property[" + str(property) + "]"

        for component in self.components:
            for t in range(i):
                string += "\n\t"
            string += component.toString(i+1)

        return string

    def __str__(self):
        return self.toString(1)

# Types of component

windowComponent = {
    "Window": ["title", "width", "height"]
}

viewComponent = {
    "Label": ["caption"]
}


# ==========================


class Syntaxer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokens.reverse()

    def error(self):
        raise NameError("LUI sytanx error")

    def parseComponent(self):

        component = ComponentNode("", [], [])

        return component

    def parseProperty(self):

        if len(self.tokens) == 0:
            return []

        property = ComponentProperty("", "")

        token = tokens.pop()
        if token.type is TokenTypes.PROPERTY:
            property.name = token.data

        token = self.tokens.pop()
        if token.type is  TokenTypes.VALUE:
            property.value = token.data

        return [property]

    def parse(self):
        ast = None

        token = self.tokens.pop()

        if token.type is not TokenTypes.COMPONENT and token.data not in windowComponent.keys():
            self.error()

        ast = ComponentNode(token.data, [], [])

        token = self.tokens.pop()
        if token.type is not TokenTypes.OBRACE:
            self.error()

        ast.properties = self.parseProperty()
        ast.components = self.parseComponent()

        token = self.tokens.pop()
        if token.type is not TokenTypes.CBRACE:
            pass
            # self.error()

        print("Create base component with properties and sub componenents")

        return ast




c = ComponentProperty("caption", "Caption")
propertiesLabel = [c]

l = ComponentNode("Label", propertiesLabel)

t = ComponentProperty("title", "Title")
w = ComponentProperty("width", 150)
h = ComponentProperty("height", 150)

propertiesWindow = [t, w, h]
m = ComponentNode("Window", propertiesWindow, [l])

with open("../examples/basic_1.lui") as f:
    code = ""
    for line in f.readlines():
        code += line

lexer = Lexer(code)
tokens = lexer.parse()

syntaxer = Syntaxer(tokens)
#print(syntaxer.parse())

print(m)

