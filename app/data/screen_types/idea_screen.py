from kivy.uix.boxlayout import BoxLayout
from app.main import ShowcaseScreen
from app.widgets.heartfelt_hellos_idea_button import HeartfeltHellosIdeaButton
from app.data.data_types.idea import Idea
from abc import abstractmethod


class IdeaScreen(ShowcaseScreen):

    box_layout = None

    def __init__(self, **kwargs):
        super(IdeaScreen, self).__init__(**kwargs)
        self.box_layout = BoxLayout(orientation="vertical")
        self.add_widget(self.box_layout)

    def on_pre_enter(self, *args):
        self.box_layout.clear_widgets()
        for idea in self.get_ideas():
            new_dynamic_widget = HeartfeltHellosIdeaButton(idea, on_press=lambda x: print("Pressed Idea Button"))
            self.box_layout.add_widget(new_dynamic_widget)

    def on_leave(self, *args):
        self.box_layout.clear_widgets()

    def get_ideas(self) -> list:
        # Default: Give general ideas (can be overridden in subclasses)
        return [Idea("General Idea 1", ["Tag 1", "Tag 2"]), Idea("General Idea 2", ["Tag 3", "Tag 4"])]
