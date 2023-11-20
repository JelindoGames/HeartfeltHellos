from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.app import App


class HeartfeltHellosNewIdeaButton(BoxLayout):

    def __init__(self, idea, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint_y = None
        self.height = 250
        self.button = HeartfeltHellosButton(text=idea.prompt, size_hint=(1, None), height="150dp", background_color=(0, 0, 0, 0))
        self.button.color = (0.1, 0.1, 0.1)
        self.button.background_color = (0.4, 0.4, 0.4)
        self.button.font_size = "36dp"
        self.button.text_size = 500, None
        self.star_image = Image(source="data/icons/star.png", size_hint=(1, None), height="50dp")
        self.label = Label(text="2.5", color=(0, 0, 0))
        self.add_widget(self.button)
        self.add_widget(self.star_image)
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
            App.get_running_app().go_screen("Idea_Share_Rate_Screen", "left")
