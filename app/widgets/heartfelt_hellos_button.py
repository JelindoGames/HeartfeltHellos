from kivy.uix.button import Button


class HeartfeltHellosButton(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 24
