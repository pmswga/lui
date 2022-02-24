import unittest
from src.translator.token import *
from src.translator.syntaxer.syntaxer import *

class TestSyntaxer(unittest.TestCase):
    def testGetST(self):
        base_tokens = [
            Token(TokenType.COMPONENT, "Window"),
            Token(TokenType.OBRACE, "{"),
            Token(TokenType.PROPERTY_NAME, "title"),
            Token(TokenType.PROPERTY_STRING_VALUE, '"Window title"'),
            Token(TokenType.PROPERTY_NAME, "width"),
            Token(TokenType.PROPERTY_NUMBER_VALUE, 150),
            Token(TokenType.PROPERTY_NAME, "height"),
            Token(TokenType.PROPERTY_NUMBER_VALUE, 150),
            Token(TokenType.CBRACE, "}"),
        ]
        base_tokens.reverse()

        base_st = ComponentNode("Window")
        base_st.properties["title"] = '"Window title"'
        base_st.properties["width"] = 150
        base_st.properties["heoght"] = 150

        syntaxer = Syntaxer()
        syntaxer.tokens = base_tokens
        st = syntaxer.parse()

        self.assertEqual(str(st), str(base_st))

    def testErrorBraces(self):
        base_tokens = [
            Token(TokenType.COMPONENT, "Window"),
            Token(TokenType.PROPERTY_NAME, "title"),
            Token(TokenType.PROPERTY_STRING_VALUE, '"Window title"'),
            Token(TokenType.PROPERTY_NAME, "width"),
            Token(TokenType.PROPERTY_NUMBER_VALUE, 150),
            Token(TokenType.PROPERTY_NAME, "height"),
            Token(TokenType.PROPERTY_NUMBER_VALUE, 150),
            Token(TokenType.CBRACE, "}"),
        ]
        base_tokens.reverse()

        syntaxer = Syntaxer()
        syntaxer.tokens = base_tokens

        try:
            st = syntaxer.parse()
        except Exception as e:
            self.assertEqual(str(e), "Syntax error: unclosed brace")


unittest.main()
