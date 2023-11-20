from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton


class HeartfeltHellosAddFriendButton(HeartfeltHellosButton):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Add Friend"
        self.size_hint_y = None
        self.height = "128dp"

