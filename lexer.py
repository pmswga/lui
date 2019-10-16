

code = """

Window {
    title:"Title"
    width: 250
    height: 250
    
}

"""

class Token:
    def __init__(self, type, value):
        self.type  = type
        self.value = value


class Lexer:
    def __init__(self, code = ""):
        self.lines   = code.strip().split()
        self.current = 0

    def nextToken(self):
        if self.current == len(self.lines):
            return None
        
        term = ""
        token = None

        for c in self.lines[self.current]:
            if c not in ["{", "}", " ", '\n']:
                term += c

                
                
            elif c == "{":
                return Token("OB", term)
            elif c == "}":
                return Token("CB", term)
            
        self.current += 1
        

class Compiler:
    def __init__(self):
        pass

    


lexer = Lexer(code)

print(lexer.nextToken())
