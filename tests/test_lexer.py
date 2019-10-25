
import unittest

from compiler.lexer import Lexer


class TestLexer(unittest.TestCase):
    def testGetTokens(self):

        with open("../examples/basic_1.lui") as f:
            code = ""
            for line in f.readlines():
                code += line

        lexer = Lexer(code)
        lexer.parse()

        self.assertEqual(len(lexer.tokens), 14)



unittest.main()
