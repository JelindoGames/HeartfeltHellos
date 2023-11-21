from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle


class ColoredLabel(Label):

    def __init__(self, color, **kwargs):
        super(ColoredLabel, self).__init__(**kwargs)
        with self.canvas.before:
            Color(*color)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size
