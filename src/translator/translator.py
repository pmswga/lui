
from translator.preprocessor.preprocessor import *
from translator.lexer.lexer import *
from translator.syntaxer.syntaxer import *
from translator.generator.generator import *
from translator.postprocessor.postprocessor import *


class LuiTranslator:
    def __init__(self):
        self.code = ""
        self.preprocessor = Preprocessor()
        self.lexer = Lexer()
        self.syntaxer = Syntaxer()
        self.generator = TkGenerator()
        self.postprocessor = Postprocessor()
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
        self.generator.user_code, self.lexer.lui_code = self.preprocessor.parse(self.code)
        self.preprocessor.exec()

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

        #if self.is_debug:
        #    self.generator.debug()

        self.postprocessor.code = code
        self.postprocessor.defines = self.preprocessor.defines
        self.postprocessor.createFile()
