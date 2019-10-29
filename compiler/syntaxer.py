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
        token = self.tokens.pop()

        componentList = []
        component = None

        while token.type is TokenTypes.COMPONENT:

            print("Component: " + token.data)

            token = self.tokens.pop()
            if token.type is not TokenTypes.OBRACE:
                self.error()

            self.parseProperty()

            token = self.tokens.pop()
            if token.type is TokenTypes.COMPONENT:
                self.tokens.append(token)
                self.parseComponent()
            elif token.type is not TokenTypes.CBRACE:
                self.error()

            component.components.append(component)
            token = self.tokens.pop()

        self.tokens.append(token)

        if len(componentList) > 1:
            return componentList
        else:
            component


    def parseProperty(self):
        token = tokens.pop()

        propertyList = []
        while token.type is TokenTypes.PROPERTY:
            property = ComponentProperty(token.data, "")

            print("Property: " + token.data)

            token = self.tokens.pop()
            if token.type is  TokenTypes.VALUE:
                property.value = token.data

            propertyList.append(property)
            token = self.tokens.pop()

        self.tokens.append(token)

        return propertyList

    def parse(self):
        token = self.tokens.pop()
        if token.type is not TokenTypes.COMPONENT and token.data not in windowComponent.keys():
            self.error()

        mainComponent = ComponentNode(token.data, [], [])
        print("Component: " + token.data)

        token = self.tokens.pop()
        if token.type is not TokenTypes.OBRACE:
            self.error()

        mainComponent.properties = self.parseProperty()

        token = self.tokens.pop()
        while token.type is TokenTypes.COMPONENT:
            component = ComponentNode(token.data, [], [])
            print("Component: " + token.data)

            token = self.tokens.pop()
            if token.type is not TokenTypes.OBRACE:
                self.error()

            component.properties = self.parseProperty()

            token = self.tokens.pop()
            if token.type is TokenTypes.COMPONENT:
                self.tokens.append(token)
                component.components = self.parseComponent()
            elif token.type is not TokenTypes.CBRACE:
                self.error()

            mainComponent.components.append(component)
            token = self.tokens.pop()

        self.tokens.append(token)

        if token.type is not TokenTypes.CBRACE:
            self.error()

        return mainComponent




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

ast = syntaxer.parse()

print("\n\n")
print(ast)

#print(m)

