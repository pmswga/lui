import unittest
from src.translator.lexer.lexer import *


class TestLexer(unittest.TestCase):
    def getCode(self, file):
        lui_code = ""

        with open(file) as f:
            code = ""
            for line in f.readlines():
                code += line

        if code.find("#LUI") != -1:
            user_code = code.split("#LUI")[0]
            lui_code = code.split("#LUI")[1]
        else:
            lui_code = code

        lui_code = re.sub("\n", " ", lui_code)
        lui_code = re.sub("\t", " ", lui_code)
        lui_code = re.sub(" +", " ", lui_code)
        lui_code = lui_code.strip()

        return lui_code

    def testParse(self):
        lexer = Lexer()
        lexer.lui_code = self.getCode("../examples/basic_1.lui")
        tokens = lexer.parse()

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

        for i in range(len(tokens)):
            self.assertEqual(tokens[i].type, base_tokens[i].type)
            self.assertEqual(tokens[i].data, base_tokens[i].data)

    def testGetTokens(self):
        lexer = Lexer()
        lexer.lui_code = self.getCode("../examples/basic_2.lui")
        tokens = lexer.parse()

        self.assertEqual(len(tokens), 14)


unittest.main()
