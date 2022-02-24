import re


class Preprocessor:
    def __init__(self):
        '''
        Constructor.

        Returns:
            void
        '''
        
        self.user_code = ""
        self.defines = {}
        self.vars = {}

    def parse(self, code):
        '''
        Split code on user and lui code.

        Parameters:
            code - source code of .lui file

        Returns:
            string
        '''
        
        lui_code = ""

        filename_def = re.search("#FILENAME=\S+", code)
        if filename_def is not None:
            bpos, epos = filename_def.span()
            self.defines["filename"] = code[bpos:epos].split("=")[1]

        version_def = re.search("#VERSION=\S+", code)
        if version_def is not None:
            bpos, epos = version_def.span()
            self.defines["version"] = code[bpos:epos].split("=")[1]

        lui_def = re.search("#LUI", code)
        if lui_def is not None:
            tmp_code = code.split("#LUI")
            if len(tmp_code) > 0:
                self.user_code = tmp_code[0]
                lui_code = tmp_code[1]
            else:
                lui_code = tmp_code[0]
        else:
            lui_code = code

        lui_code = re.sub("#FILENAME=\S+", "", lui_code)
        lui_code = re.sub("#VERSION=\S+", "", lui_code)

        lui_code = re.sub("\n", " ", lui_code)
        lui_code = re.sub("\t", " ", lui_code)
        lui_code = re.sub(" +", " ", lui_code)
        lui_code = lui_code.strip()

        return self.user_code, lui_code

    def exec(self):
        '''
        Execute user code.

        Returns:
            void
        '''
        
        if len(self.user_code) != 0:
            code = "import sys"
            code += '\n'
            code += "sys.path.append(\".\")"
            code += '\n'
            code += self.user_code

            exec(code)
            self.vars = locals()
