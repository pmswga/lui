from translator.syntaxer.syntax_error import *
from translator.token import TokenType
from translator.lui_definition import *


class ComponentNode:
    def __init__(self, name):
        self.name = name
        self.properties = {}
        self.components = []

    def toString(self, i=1):
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
        return self.toString()


class Syntaxer:
    def __init__(self):
        self.tokens = []
        self.st = ComponentNode("")

    def error(self, code=None, data=None):
        message = "Syntax error: "

        if code is SyntaxerError.UNCLOSED_BRACE:
            message += "unclosed brace"
        elif code is SyntaxerError.COMPONENT_NOT_EXISTS:
            message += "component '" + data + "' is not exists"
        elif code is SyntaxerError.PROPERTY_NOT_EXISTS:
            message += "component '" + data[0] + "' doesn't have property '" + data[1] + "'"

        raise Exception(message)

    def parseComponent(self, component):
        token = self.tokens.pop()
        if token.type is not TokenType.OBRACE:
            self.error()

        self.parseProperty(component)

        token = self.tokens.pop()
        while token.type is TokenType.COMPONENT:

            if token.data not in components.keys():
                self.error(SyntaxerError.COMPONENT_NOT_EXISTS, token.data)

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

            if token.data not in components.get(component.name):
                self.error(SyntaxerError.PROPERTY_NOT_EXISTS, [component.name, token.data])


            property = token.data

            token = self.tokens.pop()
            if token.type in [TokenType.PROPERTY_NUMBER_VALUE, TokenType.PROPERTY_STRING_VALUE,
                              TokenType.PROPERTY_VAR_VALUE]:
                component.properties[property] = token.data

            token = self.tokens.pop()

        self.tokens.append(token)

    def checkBraces(self):
        countOBraces = 0
        countCBraces = 0
        tokens = self.tokens.copy()

        for token in tokens:
            if token.type is TokenType.OBRACE:
                countOBraces += 1

            if token.type is TokenType.CBRACE:
                countCBraces += 1

        return countOBraces == countCBraces

    def parse(self):
        if not self.checkBraces():
            self.error(SyntaxerError.UNCLOSED_BRACE)

        token = self.tokens.pop()
        if token.type is not TokenType.COMPONENT or token.data not in components.keys():
            self.error(SyntaxerError.COMPONENT_NOT_EXISTS, token.data)

        self.st.name = token.data

        token = self.tokens.pop()
        if token.type is not TokenType.OBRACE:
            self.error()

        self.parseProperty(self.st)

        token = self.tokens.pop()
        while token.type is TokenType.COMPONENT:

            if token.data not in components.keys():
                self.error(SyntaxerError.COMPONENT_NOT_EXISTS, token.data)

            component = ComponentNode(token.data)

            self.parseComponent(component)

            self.st.components.append(component)
            token = self.tokens.pop()

        if token.type is not TokenType.CBRACE:
            self.error()

        return self.st

    def debug(self):
        print(self.st)
