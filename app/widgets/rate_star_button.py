from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics import Color
from kivy.graphics import Rectangle


class HeartfeltHellosRateStarButton(BoxLayout):

    img = None

    def __init__(self, touch_callback, **kwargs):
        super().__init__(**kwargs)
        self.touch_callback = touch_callback
        self.img = Image(source="data/icons/open-star.png")
        self.add_widget(self.img)
        with self.canvas.before:
            Color(0.75, 0.75, 0.8)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.touch_callback(self)

    def fill(self):
        self.img.source = "data/icons/star.png"

    def unfill(self):
        self.img.source = "data/icons/open-star.png"

