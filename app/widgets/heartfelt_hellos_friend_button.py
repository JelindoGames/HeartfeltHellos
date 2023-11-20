from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton
from app.data.data_types.friend import Friend


class HeartfeltHellosFriendButton(HeartfeltHellosButton):

    def __init__(self, friend: Friend, **kwargs):
        super().__init__(**kwargs)
        self.text = friend.name
        self.size_hint_y = None
        self.height = "128dp"

