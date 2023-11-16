from kivy.uix.boxlayout import BoxLayout
from app.main import ShowcaseScreen
from app.widgets.heartfelt_hellos_idea_button import HeartfeltHellosIdeaButton
from app.data.data_types.idea import Idea


class IdeaScreen(ShowcaseScreen):

    box_layout = None

    def __init__(self, **kwargs):
        super(IdeaScreen, self).__init__(**kwargs)
        self.box_layout = BoxLayout(orientation="vertical")
        self.add_widget(self.box_layout)

    def on_pre_enter(self, *args):
        for i in range(3):
            new_dynamic_widget = HeartfeltHellosIdeaButton(Idea(f"Idea {i}", ["tag1", "tag2"]), on_press=lambda x: print("Pressed Idea Button"))
            self.box_layout.add_widget(new_dynamic_widget)

    def on_leave(self, *args):
        self.box_layout.clear_widgets()
