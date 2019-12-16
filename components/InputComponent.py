from components.AbstractComponent import *


class ButtonComponent(AbstractComponent):
    def __init__(self):
        super().__init__()
        self.onAction = None
        self.caption = None


class RadioComponent(AbstractComponent):
    def __init__(self):
        super().__init__()
        self.caption = None


class CheckBoxComponent(AbstractComponent):
    def __init__(self):
        super().__init__()
        self.checked = False