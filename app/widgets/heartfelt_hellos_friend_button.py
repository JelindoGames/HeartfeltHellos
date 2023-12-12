from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton
from app.data.data_types.friend import Friend


class HeartfeltHellosFriendButton(BoxLayout):

    def __init__(self, friend: Friend, main_callback, edit_callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.size_hint_y = None
        self.height = "80dp"
        self.main_button = HeartfeltHellosButton(text=friend.name, size_hint_x=0.8, on_press=lambda w: main_callback(friend))
        self.edit_button = HeartfeltHellosButton(text="Edit", size_hint_x=0.2, on_press=lambda w: edit_callback(friend))
        self.edit_button.background_color = (0.6, 0.6, 0.6)
        self.edit_button.font_size = '24dp'
        self.add_widget(self.main_button)
        self.add_widget(self.edit_button)

