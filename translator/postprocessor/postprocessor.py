
class Postprocessor():
    def __init__(self):
        self.code = ""
        self.defines = {}

    def createFile(self):
        if "filename" in self.defines.keys():
            filename = self.defines["filename"]
        else:
            filename = "tmp"

        with open(filename + ".py", "w") as f:
            f.write("\n".join(self.code))

