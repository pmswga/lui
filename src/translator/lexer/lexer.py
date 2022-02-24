# @package lui Lexer

from ..token import *
import re


class Lexer:
    def __init__(self):
        '''
        Constructor.
        '''

        ## Token list
        self.tokens = []
        ## A code describe Lui syntax
        self.lui_code = ""


    def isComponentName(self, componentName):
        '''
        Check a component name.

        Params:
            componentName - Name of component. For example, 'Window'

        Returns:
            boolean
        '''

        return re.match("^[A-Z][a-z]+$", componentName) is not None

    def isPropertyName(self, propertyName):
        '''
        Check a property name.

        Params:
            propertyName - Name of property. For example, 'width:'

        Returns:
            boolean
        '''

        return re.match("^[a-z]*[a-z-]+:$", propertyName) is not None

    def isPropertyNumberValue(self, propertyValue):
        '''
        Checking property value for a number.

        Params:
            propertyValue - property value. For example, '600'

        Returns:
            boolean
        '''

        return re.match("\d+", propertyValue) is not None

    def isPropertyStringValue(self, propertyValue):
        '''
        Checking property value for a string.

        Params:
            propertyValue - property value. For example, '"this is string"'

        Returns:
            boolean
        '''

        return re.match("^\"[\S\w ]+\"$", propertyValue) is not None

    def isPropertyVarValue(self, propertyValue):
        '''
        Checking property value for a var_name.

        Params:
            propertyValue - property value. For example, 'var_name'

        Returns:
            boolean
        '''

        return re.match("^[a-zA-z]+[a-zA-Z0-9_]*$", propertyValue) is not None

    def parse(self):
        '''
        Get tokens from code.

        Returns:
            List of tokens
        '''

        token = ""

        isQuotes = False
        for c in self.lui_code:

            if c == "{":
                self.tokens.append(Token(TokenType.OBRACE, "{"))
                token = ""

            if c == "}":
                self.tokens.append(Token(TokenType.CBRACE, "}"))
                token = ""

            if c == "\"":
                isQuotes = not isQuotes if True else False

            if not isQuotes and c == " ":
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
        '''
        Print token list.

        Returns:
            void
        '''

        tokens = self.tokens.copy()
        tokens.reverse()
        for token in tokens:
            print(token)
