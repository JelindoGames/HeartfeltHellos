from kivy.uix.button import Button
from app.data.data_types.idea import Idea


class HeartfeltHellosIdeaButton(Button):

    def __init__(self, idea: Idea, **kwargs):
        super().__init__(**kwargs)
        self.text = idea.prompt
        self.font_size = 24

