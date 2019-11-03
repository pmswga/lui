from translator.lexer.token import TokenType
from translator.lui_definition import *


class ComponentNode:
    def __init__(self, name):
        self.name = name
        self.properties = {}
        self.components = []

    def toString(self, i):
        string = self.name

        for property in self.properties:
            string += "\n"
            for t in range(i):
                string += "\t"
            string += "Property[" + str(self.properties[property]) + "]"

        for component in self.components:
            string += "\n"
            for t in range(i):
                string += "\t"
            string += component.toString(i + 1)

        return string

    def __str__(self):
        return self.toString(1)


class Syntaxer:
    def __init__(self):
        self.tokens = []
        self.st = ComponentNode("")

    def error(self, code=None):
        # print("LUI syntax error")
        raise Exception("LUI syntax error")

    def parseComponent(self, component):
        token = self.tokens.pop()
        if token.type is not TokenType.OBRACE:
            self.error()

        self.parseProperty(component)

        token = self.tokens.pop()
        while token.type is TokenType.COMPONENT:
            subComponent = ComponentNode(token.data)

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
            property = token.data

            token = self.tokens.pop()
            if token.type in [TokenType.PROPERTY_NUMBER_VALUE, TokenType.PROPERTY_STRING_VALUE,
                              TokenType.PROPERTY_VAR_VALUE]:
                component.properties[property] = token.data

            token = self.tokens.pop()

        self.tokens.append(token)

    def parse(self):
        token = self.tokens.pop()
        if token.type is not TokenType.COMPONENT or token.data not in components["windowComponent"].keys():
            self.error()

        self.st.name = token.data

        token = self.tokens.pop()
        if token.type is not TokenType.OBRACE:
            self.error()

        self.parseProperty(self.st)

        token = self.tokens.pop()
        while token.type is TokenType.COMPONENT:
            component = ComponentNode(token.data)

            self.parseComponent(component)

            self.st.components.append(component)
            token = self.tokens.pop()

        if token.type is not TokenType.CBRACE:
            self.error()

        return self.st

    def debug(self):
        print(self.st)
