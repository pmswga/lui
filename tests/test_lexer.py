
import sys
import unittest

sys.path.insert(1, '../')

from lexer import *

class TestLexer(unittest.TestCase):
    def testMultilineCode(self):
        code = """
            Window {
                title: "Title is mine”
                width:  150
                height: 150
            }
        """
        lexer = Lexer(code)

        self.assertEqual(len(lexer.tokens), 6)
            
    def testInlineCode(self):
        code = """
            Window { title: "Title” width: 150 height: 150}
        """
        
        lexer = Lexer(code)
        
        self.assertEqual(len(lexer.tokens), 6)



unittest.main()
