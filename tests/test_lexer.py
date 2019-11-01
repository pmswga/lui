
import unittest

from translator.lexer.lexer import *


class TestLexer(unittest.TestCase):

    def testParse(self):
        with open("../examples/basic_1.lui") as f:
            code = ""
            for line in f.readlines():
                code += line

        lexer = Lexer(code)
        tokens = lexer.parse()

        base_tokens = [
            Token(TokenTypes.COMPONENT, "Window"),
            Token(TokenTypes.OBRACE, "{"),
            Token(TokenTypes.PROPERTY, "title:"),
            Token(TokenTypes.VALUE, '"Window title"'),
            Token(TokenTypes.PROPERTY, "width:"),
            Token(TokenTypes.VALUE, 150),
            Token(TokenTypes.PROPERTY, "height:"),
            Token(TokenTypes.VALUE, 150),
            Token(TokenTypes.CBRACE, "}"),
        ]

        self.assertEqual(len(tokens), len(base_tokens))
        for i in range(len(tokens)):
            self.assertEqual(tokens[i].type, base_tokens[i].type)
            self.assertEqual(tokens[i].data, base_tokens[i].data)


    def testGetTokens(self):
        with open("../examples/basic_2.lui") as f:
            code = ""
            for line in f.readlines():
                code += line

        lexer = Lexer(code)
        tokens = lexer.parse()

        self.assertEqual(len(tokens), 14)



unittest.main()
