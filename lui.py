
import sys
from  translator.lexer import *
from  translator.syntaxer import *
from  translator.generator import *


if len(sys.argv) > 1:
    path = sys.argv[1]

    with open(path) as f:
        code = ""
        for line in f.readlines():
            code += line

    lexer = Lexer(code)
    tokens = lexer.parse()

    syntaxer = Syntaxer(tokens)

    ast = syntaxer.parse()

    #print("\n\n")
    #print(ast)

    generator = TkGenerator(ast)

    generator.generate()
else:
    print("No input file")
