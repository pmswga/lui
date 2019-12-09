# @package lui Lexer

from translator.token import *
import re


class Lexer:
    def __init__(self):
        self.tokens = []
        self.lui_code = ""

    def isComponentName(self, componentName):
        return re.match("^[A-Z][a-z]+$", componentName) is not None

    def isPropertyName(self, propertyName):
        return re.match("^[a-z]*[a-z-]+:$", propertyName) is not None

    def isPropertyNumberValue(self, propertyValue):
        return re.match("\d+", propertyValue) is not None

    def isPropertyStringValue(self, propertyValue):
        return re.match("^\"[\S\w ]+\"$", propertyValue) is not None

    def isPropertyVarValue(self, propertyValue):
        return re.match("^[a-zA-z]+[a-zA-Z0-9_]*$", propertyValue) is not None

    def parse(self):
        token = ""

        isQuotes = False
        for c in self.lui_code:

            if c is "{":
                self.tokens.append(Token(TokenType.OBRACE, "{"))
                token = ""

            if c is "}":
                self.tokens.append(Token(TokenType.CBRACE, "}"))
                token = ""

            if c is "\"":
                isQuotes = not isQuotes if True else False

            if not isQuotes and c is " ":
                token = token.lstrip(" ")

                if self.isComponentName(token):
                    self.tokens.append(Token(TokenType.COMPONENT, token))
                elif self.isPropertyName(token):
                    self.tokens.append(Token(TokenType.PROPERTY_NAME, token[:-1]))
                elif self.isPropertyStringValue(token):
                    self.tokens.append(Token(TokenType.PROPERTY_STRING_VALUE, token))
                elif self.isPropertyNumberValue(token):
                    self.tokens.append(Token(TokenType.PROPERTY_NUMBER_VALUE, int(token)))
                elif self.isPropertyVarValue(token):
                    self.tokens.append(Token(TokenType.PROPERTY_VAR_VALUE, token))

                token = ""

            token += c

        self.tokens.reverse()
        return self.tokens

    def debug(self):
        tokens = self.tokens.copy()
        tokens.reverse()
        for token in tokens:
            print(token)
