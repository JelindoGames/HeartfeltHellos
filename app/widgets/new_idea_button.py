from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.app import App
from kivy.metrics import dp


class HeartfeltHellosNewIdeaButton(BoxLayout):

    do_something_on_touch_down = True

    def __init__(self, idea, idea_screen_name, **kwargs):
        super().__init__(**kwargs)
        self.idea = idea
        self.idea_screen_name = idea_screen_name
        self.orientation = "vertical"
        self.size_hint_y = None
        self.height = "250dp"
        self.button = HeartfeltHellosButton(text=idea.prompt, size_hint=(1, None), height="150dp", background_color=(0, 0, 0, 0))
        self.button.color = (0.1, 0.1, 0.1)
        self.button.background_color = (0.4, 0.4, 0.4)
        self.button.font_size = "36dp"
        self.button.text_size = dp(300), None
        self.star_image = Image(source="data/icons/star.png", size_hint=(1, None), height="50dp")
        self.label = Label(text=str(idea.rating), color=(0, 0, 0))
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
        if not self.do_something_on_touch_down:
            return
        if self.collide_point(*touch.pos):
            App.get_running_app().stored_data.idea_screen_history.append(self.idea_screen_name)
            App.get_running_app().stored_data.idea_history.append(self.idea)
            App.get_running_app().stored_data.temp_selected_idea = self.idea
            if App.get_running_app().stored_data.temp_selected_person is None:
                App.get_running_app().go_screen("Friend_List_For_General_Ideas", "left")
            else:
                App.get_running_app().go_screen("Idea_Share_Rate_Screen", "left")

    def do_nothing_on_touch_down(self):
        self.do_something_on_touch_down = False
