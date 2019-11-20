
class Preprocessor:
    def __init__(self):
        self.user_code = ""
        self.vars = {}

    def exec(self):
        code = "import sys"
        code += '\n'
        code += "sys.path.append(\".\")"
        code += '\n'
        code += self.user_code

        exec(code)
        self.vars = locals()
