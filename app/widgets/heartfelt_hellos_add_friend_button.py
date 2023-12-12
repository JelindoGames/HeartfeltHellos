from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton


class HeartfeltHellosAddFriendButton(HeartfeltHellosButton):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "+ New Friend"
        self.bold = True
        self.size_hint_y = None
        self.height = "80dp"
        self.background_color = (0.5, 0.5, 0.8)

