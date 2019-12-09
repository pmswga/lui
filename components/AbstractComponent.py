

class AbstractComponent:
    def __init__(self):
        self.name = None
        self.x = None
        self.y = None
        self.relx = None
        self.rely = None
        self.anchor = None
        self.position = None
        self.width = None
        self.height = None

    def __str__(self):
        return self.name
