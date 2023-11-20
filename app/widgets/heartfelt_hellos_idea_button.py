from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton
from app.data.data_types.idea import Idea


class HeartfeltHellosIdeaButton(HeartfeltHellosButton):

    def __init__(self, idea: Idea, **kwargs):
        super().__init__(**kwargs)
        self.text = idea.prompt
        self.color = (0, 0, 0)
        self.size_hint_y = None
        self.height = 128

