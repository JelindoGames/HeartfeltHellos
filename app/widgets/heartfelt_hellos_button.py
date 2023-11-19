from kivy.uix.button import Button


class HeartfeltHellosButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = "Raleway"
        self.font_size = 48
        self.color = (1, 1, 1, 1)
