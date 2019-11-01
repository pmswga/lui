# lui Lexer

import enum
import re


class TokenTypes(enum.Enum):
    COMPONENT = 1
    PROPERTY = 2
    VALUE = 3
    OBRACE = 4
    CBRACE = 5

class Token:
    def __init__(self, type, data):
        self.type = type
        self.data = data

    def __str__(self):
        return "<" + str(self.type) + ", " + str(self.data) + ">"

class LexerError(enum.Enum):
    INCORRECT_COMPONENT = 0
    INCORRECT_PROPERTY = 1
    INCORRECT_VALUE = 2
    UNCLOSED_BRACE = 3

class LexerException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class Lexer:
    def __init__(self, code=""):
        self.tokens = []
        self.code = code
        self.code = re.sub("\n", " ", self.code)
        self.code = re.sub("\t", " ", self.code)
        self.code = re.sub(" +", " ", self.code)
        self.code = self.code.strip()

    def isComponentName(self, componentName):
        return re.match("^[A-Z][a-z]+$", componentName) is not None

    def isProperty(self, property):
        return re.match("^[a-z]+:$", property) is not None

    def isPropertyIntValue(self, propertyValue):
        return re.match("\d+", propertyValue) is not None

    def isPropertyStrValue(self, propertyValue):
        return re.match("^\"[\S\w ]+\"$", propertyValue) is not None

    def isPropertyVarValue(self, propertyValue): # TODO: Add regex of property var
        return re.match("^[a-zA-z]+[a-zA-Z0-9_]*$", propertyValue) is not None

    def error(self, code, data): #TODO: По идеи, на этапе лексического анализа надо проверять ошибки
        if code is LexerError.INCORRECT_COMPONENT:
            raise LexerException("Incorrect component name: " + data)
        elif code is LexerError.INCORRECT_PROPERTY:
            raise LexerException("Incorrect property name: " + data)
        elif code is LexerError.INCORRECT_VALUE:
            raise LexerException("Incorrect property value: " + data)
        elif code is LexerError.UNCLOSED_BRACE:
            raise LexerException("Unclosed brace" + data)

    def parseBraces(self):
        stackBraces = []
        for c in self.code:
            if c is "{":
                stackBraces.append("{")
            elif c is "}":
                stackBraces.pop()

        return len(stackBraces) == 0

    def parse(self):
        token = ""

        if self.parseBraces() is False: # TODO: Реализовать нормальную проверку на ошибки
            self.error(LexerError.UNCLOSED_BRACE, "")

        isQuotes = False
        for c in self.code:

            if c is "{":
                self.tokens.append(Token(TokenTypes.OBRACE, "{"))
                token = ""

            if c is "}":
                self.tokens.append(Token(TokenTypes.CBRACE, "}"))
                token = ""

            if c is "\"":
                isQuotes = not isQuotes if True else False

            if not isQuotes and c is " ":
                token = token.lstrip(" ")

                if self.isComponentName(token):
                    self.tokens.append(Token(TokenTypes.COMPONENT, token))
                elif self.isProperty(token):
                    self.tokens.append(Token(TokenTypes.PROPERTY, token[:-1]))
                elif self.isPropertyStrValue(token):
                    self.tokens.append(Token(TokenTypes.VALUE, token))
                elif self.isPropertyIntValue(token):
                    self.tokens.append(Token(TokenTypes.VALUE, int(token)))
                elif self.isPropertyVarValue(token):
                    self.tokens.append(Token(TokenTypes.VALUE, token))

                token = ""

            token += c

        return self.tokens
"""
try:

    with open("../examples/basic_1.lui") as f:
        code = ""
        for line in f.readlines():
            code += line

    lexer = Lexer(code)
    tokens = lexer.parse()

    for token in tokens:
        print(token)
except LexerException as e:
    print(e)
"""