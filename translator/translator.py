
from translator.preprocessor.preprocessor import *
from translator.lexer.lexer import *
from translator.syntaxer.syntaxer import *
from translator.generator.generator import *


class LuiTranslator:
    def __init__(self):
        self.code = ""
        self.preprocessor = Preprocessor()
        self.lexer = Lexer()
        self.syntaxer = Syntaxer()
        self.generator = TkGenerator()
        self.is_debug = False

    def debugLexer(self):
        print("Tokens:")
        self.lexer.debug()
        print("\n")

    def debugSyntaxer(self):
        print("Syntax tree:")
        self.syntaxer.debug()
        print("\n")

    def debugTranslator(self):
        self.generator.debug()

    def run(self):
        codes = self.code.split("#LUI")

        self.preprocessor.user_code = codes[0]
        self.preprocessor.exec()

        if len(codes) > 0:
            self.generator.user_code = codes[0]
            self.lexer.lui_code = codes[1]
        else:
            self.lexer.lui_code = self.code

        self.lexer.lui_code = re.sub("\n", " ", self.lexer.lui_code)
        self.lexer.lui_code = re.sub("\t", " ", self.lexer.lui_code)
        self.lexer.lui_code = re.sub(" +", " ", self.lexer.lui_code)
        self.lexer.lui_code = self.lexer.lui_code.strip()
        tokens = self.lexer.parse()

        if self.is_debug:
            self.debugLexer()

        self.syntaxer.tokens = tokens
        st = self.syntaxer.parse()

        if self.is_debug:
            self.debugSyntaxer()

        self.generator.locals = self.preprocessor.vars
        self.generator.st = st
        code = self.generator.generate()

        with open("tmp.py", "w") as f:
            f.write("\n".join(code))

        #if self.is_debug:
        #    self.generator.debug()
