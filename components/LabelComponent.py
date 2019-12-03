from components.AbstractComponent import AbstractComponent


class LabelComponent (AbstractComponent):
    def __init__(self, name = "label"):
        super().__init__()
        self.name = name
        self.caption = ""
