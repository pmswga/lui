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

    def isOBrace(self, obrace):
        return obrace is "{"

    def isCBrace(self, cbrace):
        return cbrace is "}"

    def isProperty(self, property):
        return re.match("^[a-z]+:$", property) is not None

    def isPropertyIntValue(self, propertyValue):
        return re.match("\d+", propertyValue) is not None

    def isPropertyStrValue(self, propertyValue):
        return  re.match("^\"[\S\w ]+\"$", propertyValue) is not None

    def error(self, code, data): #TODO: По идеи, на этапе лексического анализа надо проверять ошибки
        if code is LexerError.INCORRECT_COMPONENT:
            raise LexerException("Incorrect component name: " + data)
        elif code is LexerError.INCORRECT_PROPERTY:
            raise LexerException("Incorrect property name: " + data)
        elif code is LexerError.INCORRECT_VALUE:
            raise LexerException("Incorrect property value: " + data)


    def parse(self):
        token = ""

        isQuotes = False
        for c in self.code:
            if c is "\"":
                isQuotes = not isQuotes if True else False

            if not isQuotes and c is " ":
                token = token.lstrip(" ")

                if self.isComponentName(token):
                    self.tokens.append(Token(TokenTypes.COMPONENT, token))

                if self.isOBrace(token):
                    self.tokens.append(Token(TokenTypes.OBRACE, token))

                if self.isProperty(token):
                    self.tokens.append(Token(TokenTypes.PROPERTY, token))

                if self.isPropertyStrValue(token):
                    self.tokens.append(Token(TokenTypes.VALUE, token))

                if self.isPropertyIntValue(token):
                    self.tokens.append(Token(TokenTypes.VALUE, int(token)))

                if self.isCBrace(token):
                    self.tokens.append(Token(TokenTypes.CBRACE, token))

                token = ""

            token += c

        if token is not "":
            token = token.lstrip(" ")
            if self.isCBrace(token):
                self.tokens.append(Token(TokenTypes.CBRACE, token))

        return self.tokens

"""

with open("../examples/basic_1.lui") as f:
    code = ""
    for line in f.readlines():
        code += line

lexer = Lexer(code)
tokens = lexer.parse()

for token in tokens:
    print(token)

"""