
from lexer import *

class ComponentProperty:
    def __init__(self, name, value):
        self.name  = name
        self.value = value

class ComponentNode:
    def __init__(self, name, variables, components = []):
        self.name       = name
        self.variables  = variables
        self.components = components


class Syntaxer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokens.reverse()
        

    def error(self):
        raise NameError("LUI sytanx error")

    def parseComponent(self, tokens):
        component = ""
        token = self.tokens.pop()

        print("Current token -> <" + token.type + ", " + token.value + ">")

        if token.type == "variable":
            component = "var, "
            print("Create property node...")
            component += self.parseComponent(self.tokens)

        if token.type == "component":
            token = self.tokens.pop()

            print("Current token -> <" + token.type + ", " + token.value + ">")
            if token.type != "obrace":
                self.error()

            component = "comp, "
            print("Create component node...")
            component += self.parseComponent(self.tokens)

            #if token.type != "cbrace":
                #self.error()

        if self.tokens:
            return component

    def parseProperty(self, tokens):
        #check [varname]:[value]
        
        return None

    def parse(self):
        gui = ""

        token = self.tokens.pop()

        print("Current token -> <" + token.type + ", " + token.value + ">")

        if token.type == "component":
            
            token = self.tokens.pop()
            if token.type != "obrace":
                self.error()

            print("Current token -> <" + token.type + ", " + token.value + ">")

            print("Create component node...")
            gui = "comp, "
            gui += self.parseComponent(self.tokens)

            token = self.tokens.pop()

            print("Current token -> <" + token.type + ", " + token.value + ">")
            
            if token.type != "cbrace":
                self.error()
            
        else:
            self.error()

        return gui


t = ComponentProperty("title", "Title")
w = ComponentProperty("width", 150)
h = ComponentProperty("height", 150)

properties = [t, w, h]

m = ComponentNode("Window", properties)


code = """
            Window {
                title: "Title is mine”
                width:  150
     height: 150
     Label {

     }
    }
"""

lexer = Lexer(code)
#lexer.debug()

syntaxer = Syntaxer(lexer.tokens)

print(syntaxer.parse())
