from kivy.uix.button import Button
from kivy.graphics import Color


class HeartfeltHellosButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (.678, .847, 0.902)
        self.font_name = "Raleway"
        self.halign="center"
        self.font_size = "33dp"
        self.color = (0, 0, 0, 1)
