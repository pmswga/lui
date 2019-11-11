
from enum import Enum


class SyntaxerError(Enum):
    UNCLOSED_BRACE = 0
    COMPONENT_NOT_EXISTS = 1
    PROPERTY_NOT_EXISTS = 2
