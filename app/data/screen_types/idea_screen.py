from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from app.main import ShowcaseScreen
from app.widgets.heartfelt_hellos_idea_button import HeartfeltHellosIdeaButton
from app.data.data_types.idea import Idea


class IdeaScreen(ShowcaseScreen):

    scroll_view = None
    box_layout = None

    def __init__(self, **kwargs):
        super(IdeaScreen, self).__init__(**kwargs)
        self.scroll_view = ScrollView(do_scroll_x=lambda _: False, do_scroll_y=lambda _: True)
        self.box_layout = BoxLayout(orientation="vertical", spacing='10dp', padding='10dp')
        self.add_widget(self.scroll_view)
        self.scroll_view.add_widget(self.box_layout)

    def on_pre_enter(self, *args):
        self.box_layout.clear_widgets()
        for idea in self.get_ideas():
            new_dynamic_widget = HeartfeltHellosIdeaButton(idea, on_press=lambda x: print("Pressed Idea Button"))
            self.box_layout.add_widget(new_dynamic_widget)

    def on_leave(self, *args):
        self.box_layout.clear_widgets()

    def get_ideas(self) -> list:
        # Default: Give general ideas (can be overridden in subclasses)
        return [Idea("General Idea 1", ["Tag 1", "Tag 2"]), Idea("General Idea 2", ["Tag 3", "Tag 4"]),
                Idea("General Idea 3", ["Tag 3", "Tag 4"]), Idea("General Idea 4", ["Tag 3", "Tag 4"]),
                Idea("General Idea 5", ["Tag 3", "Tag 4"])]
