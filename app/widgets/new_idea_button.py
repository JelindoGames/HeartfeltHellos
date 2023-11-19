from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton
from app.data.data_types.idea import Idea
from kivy.graphics import Color
from kivy.graphics import Rectangle


class HeartfeltHellosNewIdeaButton(BoxLayout):

    def __init__(self, idea, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint_y = None
        self.height = 300
        self.button = HeartfeltHellosButton(text=idea.prompt, size_hint_y=None, height=250, background_color=(0, 0, 0, 0))
        self.button.text_size = 400, None
        self.label = Label(text="Rating: 1 Star")
        self.add_widget(self.button)
        self.add_widget(self.label)
        with self.canvas.before:
            Color(0.5, 0.5, 0.5, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print("Pressed New Idea Button")
