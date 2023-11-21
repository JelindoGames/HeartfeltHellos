from kivy.uix.button import Button


class HeartfeltHellosButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0.3, 0.3, 0.3)
        self.font_name = "Raleway"
        self.halign="center"
        self.font_size = "33dp"
        self.color = (1, 1, 1, 1)
