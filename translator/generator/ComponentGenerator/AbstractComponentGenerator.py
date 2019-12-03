
class AbstractComponentGenerator:
    def __init__(self, component):
        self.component = component
        self.code = ""

    def genInitial(self):
        pass

    def genProperties(self):
        pass

    def genLayout(self):
        pass

    def generate(self):
        pass
