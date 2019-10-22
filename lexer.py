
import re

keywords_components = ["Window", "Label", "List"]
keywords_variables  = ["width", "height", "title", "caption", "data"]
keywords_syntax = ["{", "}"]

token_types = ["component", "variable", "obarce", "cbrace"]

class Token:
    def __init__(self, type, value):
        self.type  = type
        self.value = value

class Lexer:
    def __init__(self, code = ""):
        self.tokens = []

        code = code.replace("\n", " ")
        code = code.strip(" ")
        code = re.sub(" +", " ", code)
        
        word = ""
        for c in code:
            if c is "{":
                self.tokens.append(Token("obrace", c))

            if c is "}":
                self.tokens.append(Token("cbrace", c))
            
            if c is " ": 
                if word in keywords_components:
                    self.tokens.append(Token("component", word.strip()))
                elif word[:-1] in keywords_variables:
                    self.tokens.append(Token("variable", word.strip()))
                elif word.isdigit():
                    self.tokens[len(self.tokens)-1].value += word
                elif word not in keywords_syntax:
                    self.tokens[len(self.tokens)-1].value += " " + word

                word = ""
            else:
                word += c
        

        self.tokens.reverse()

    def nextToken(self):
        return self.tokens.pop()


