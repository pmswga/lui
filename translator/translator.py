
from translator.lexer.lexer import *
from translator.syntaxer import *
from translator.generator import *

class LuiTranslator:
    def __init__(self):
        self.code = ""
        self.lexer = Lexer()
        self.syntaxer = Syntaxer()
        self.generator = TkGenerator(None, "")
        self.is_debug = False

    def debugTokens(self):
        print("\nTokens:\n")
        self.lexer.debug()
        print("\n")

    def debugST(self):
        print("\nSyntax tree:\n")
        self.syntaxer.debug()
        print("\n")

    def run(self):
        if self.code.find("#LUI") != -1:
            self.lexer.user_code = self.code.split("#LUI")[0]
            self.lexer.lui_code = self.code.split("#LUI")[1]
        else:
            self.lexer.lui_code = self.code

        self.lexer.lui_code = re.sub("\n", " ", self.lexer.lui_code)
        self.lexer.lui_code = re.sub("\t", " ", self.lexer.lui_code)
        self.lexer.lui_code = re.sub(" +", " ", self.lexer.lui_code)
        self.lexer.lui_code = self.lexer.lui_code.strip()
        tokens = self.lexer.parse()

        if self.is_debug:
            self.debugTokens()

        self.syntaxer.tokens = tokens
        st = self.syntaxer.parse()

        if self.is_debug:
            self.debugST()

        self.generator.ast = st
        self.generator.other_code = self.lexer.user_code
        self.generator.generate()

        if self.is_debug:
            self.generator.debug()
