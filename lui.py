
import sys
from translator.lexer.lexer import *
from translator.syntaxer import *
from translator.generator import *

# Lui cmd args
# --file=path
# --debug
# --help

path = ""
isDebug = False

if len(sys.argv) > 1:
    for arg in sys.argv:
        if arg.find("--file=") != -1:
            path = arg.split("=")[1]

        if arg.find("--debug") != -1:
            isDebug = True

        if arg.find("--help") != -1:
            print("List of lui cmd args:")
            print("\t --help        - view list of lui cmd args")
            print("\t --file=[path] - select path to *.lui file")
            print("\t --debug       - turn on debug mode")

            sys.exit(0)

    if path != "":
        with open(path) as f:
            code = ""
            for line in f.readlines():
                code += line

        if isDebug:
            print("File path: \"" + path + "\"")
            print("Debug mode: on")


        lexer = Lexer(code)
        tokens = lexer.parse()

        if isDebug:
            print("\nList of tokens:\n")
            lexer.debug()
            print("\n")

        syntaxer = Syntaxer(tokens)
        ast = syntaxer.parse()

        if isDebug:
            print("\nAbstract syntax tree of lui code:\n")
            syntaxer.debug()
            print("\n")

        #print("\n\n")
        #print(ast)

        generator = TkGenerator(ast, lexer.other_code)

        generator.generate()
    else:
        print("No input file")
else:
    print("List of lui cmd args:")
    print("\t --help        - view list of lui cmd args")
    print("\t --file=[path] - select path to *.lui file")
    print("\t --debug       - turn on debug mode")
