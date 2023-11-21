from kivy.uix.label import Label
from kivy.metrics import cm


class HeartfeltHellosLabel(Label):

    def __init__(self, **kwargs):
        super(HeartfeltHellosLabel, self).__init__(**kwargs)
        self.font_name="Raleway"
        self.text_size=(cm(9),None)
        self.size_hint_y=None
        self.color=(0, 0, 0)
