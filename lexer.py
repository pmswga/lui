

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

        isValueAssigned = True
        
        for line in code.strip().split("\n"):
            for word in line.split(" "):
                if word in keywords_components:
                    self.tokens.append(Token("component", word))

                if word == "{":
                    self.tokens.append(Token("obrace", word))

                if isValueAssigned is not True:
                    self.tokens[len(self.tokens)-1].value += word
                    isValueAssigned = True
                
                if word[:-1] in keywords_variables:
                    self.tokens.append(Token("variable", word))
                    isValueAssigned = False


                if word == "}":
                    self.tokens.append(Token("cbrace", word))

        self.tokens.reverse()

    def nextToken(self):
        return self.tokens.pop()



code = """

Window {
    title: "Title”
    width:150
    height: 150

    Label { 
        caption: "It's mine label"
    }
}

"""

lexer = Lexer(code)

for i in range(len(lexer.tokens)):
    token = lexer.nextToken()
    print("<" + token.type + ", " + token.value + ">")

