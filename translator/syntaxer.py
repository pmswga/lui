from translator.lexer import *
from enum import Enum

class ComponentProperty:
    def __init__(self, name, value = None):
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
            string += "\n"
            for t in range(i):
                string += "\t"
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
        self.ast = ComponentNode("", [], [])

    def error(self, code = None):
        raise NameError("LUI syntax error")

    def parseComponent(self, component):
        token = self.tokens.pop()
        if token.type is not TokenTypes.OBRACE:
            self.error()

        self.parseProperty(component)

        token = self.tokens.pop()
        while token.type is TokenTypes.COMPONENT:
            subComponent = ComponentNode(token.data, [], [])

            self.parseComponent(subComponent)

            component.components.append(subComponent)
            token = self.tokens.pop()

        self.tokens.append(token)

        token = self.tokens.pop()
        if token.type is not TokenTypes.CBRACE:
            self.error()


    def parseProperty(self, component):
        token = self.tokens.pop()
        while token.type is TokenTypes.PROPERTY:
            property = ComponentProperty(token.data)

            token = self.tokens.pop()
            if token.type is  TokenTypes.VALUE:
                property.value = token.data

            component.properties.append(property)
            token = self.tokens.pop()

        self.tokens.append(token)

    def parseBraces(self):
        braceTokens = self.tokens.copy()
        braceStack = []

        while len(braceTokens) > 0:
            token = braceTokens.pop()
            if token.type is TokenTypes.OBRACE:
                braceStack.append("{")
            elif token.type is TokenTypes.CBRACE:
                braceStack.pop()

        return len(braceStack) == 0

    def parse(self):
        if not self.parseBraces():
            self.error()

        token = self.tokens.pop()
        if token.type is not TokenTypes.COMPONENT or token.data not in windowComponent.keys():
            self.error()

        self.ast.name = token.data

        token = self.tokens.pop()
        if token.type is not TokenTypes.OBRACE:
            self.error()

        self.parseProperty(self.ast)

        token = self.tokens.pop()
        while token.type is TokenTypes.COMPONENT:
            component = ComponentNode(token.data, [], [])

            self.parseComponent(component)

            self.ast.components.append(component)
            token = self.tokens.pop()

        if token.type is not TokenTypes.CBRACE:
            self.error()

        return self.ast



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
