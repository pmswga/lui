
from translator.lexer.token import TokenType
from translator.lui_definition import *


class ComponentProperty:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def __str__(self):
        return self.name + ": " + str(self.value)


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
            string += "\n"
            for t in range(i):
                string += "\t"
            string += component.toString(i + 1)

        return string

    def __str__(self):
        return self.toString(1)


class Syntaxer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokens.reverse()
        self.ast = ComponentNode("", [], [])

    def error(self, code=None):
        #print("LUI syntax error")
        raise NameError("LUI syntax error")

    def parseComponent(self, component):
        token = self.tokens.pop()
        if token.type is not TokenType.OBRACE:
            self.error()

        self.parseProperty(component)

        token = self.tokens.pop()
        while token.type is TokenType.COMPONENT:
            subComponent = ComponentNode(token.data, [], [])

            self.parseComponent(subComponent)

            component.components.append(subComponent)
            token = self.tokens.pop()

        self.tokens.append(token)

        token = self.tokens.pop()
        if token.type is not TokenType.CBRACE:
            self.error()

    def parseProperty(self, component):
        token = self.tokens.pop()
        while token.type is TokenType.PROPERTY_NAME:
            property = ComponentProperty(token.data)

            token = self.tokens.pop()
            if token.type in [TokenType.PROPERTY_NUMBER_VALUE, TokenType.PROPERTY_STRING_VALUE, TokenType.PROPERTY_VAR_VALUE]:
                property.value = token.data

            component.properties.append(property)
            token = self.tokens.pop()

        self.tokens.append(token)

    def parse(self):
        token = self.tokens.pop()
        if token.type is not TokenType.COMPONENT or token.data not in components["windowComponent"].keys():
            self.error()

        self.ast.name = token.data

        token = self.tokens.pop()
        if token.type is not TokenType.OBRACE:
            self.error()

        self.parseProperty(self.ast)

        token = self.tokens.pop()
        while token.type is TokenType.COMPONENT:
            component = ComponentNode(token.data, [], [])

            self.parseComponent(component)

            self.ast.components.append(component)
            token = self.tokens.pop()

        if token.type is not TokenType.CBRACE:
            self.error()

        return self.ast

    def debug(self):
        print(self.ast)


"""
c = ComponentProperty("caption", "Caption")
propertiesLabel = [c]
l = ComponentNode("Label", propertiesLabel)

cButton = ComponentProperty("caption" , "Caption")
propertiesButton = [cButton]
b = ComponentNode("Button", propertiesButton)


row = ComponentNode("Row", [], [l, b])

grid2 = ComponentNode("Grid", [], [row])

t = ComponentProperty("title", "Title")
w = ComponentProperty("width", 150)
h = ComponentProperty("height", 150)

propertiesWindow = [t, w, h]
m = ComponentNode("Window", propertiesWindow, [grid2])
"""
