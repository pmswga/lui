from enum import Enum


class TokenType(Enum):
    COMPONENT = 1
    PROPERTY_NAME = 2
    PROPERTY_NUMBER_VALUE = 3
    PROPERTY_STRING_VALUE = 4
    PROPERTY_VAR_VALUE = 5
    OBRACE = 6
    CBRACE = 7


class Token:
    def __init__(self, type, data):
        self.type = type
        self.data = data

    def __str__(self):
        return "<" + str(self.type) + ", " + str(self.data) + ">"
