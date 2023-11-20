from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from app.main import ShowcaseScreen
from app.widgets.new_idea_button import HeartfeltHellosNewIdeaButton
from app.data.data_types.idea import Idea


class IdeaScreen(ShowcaseScreen):

    scroll_view = None
    grid_layout = None

    def __init__(self, test=None, **kwargs):
        super(IdeaScreen, self).__init__(**kwargs)
        if test is not None:
            print(test)
        self.grid_layout = GridLayout(spacing='20dp', padding='20dp', cols=1, size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter("height"))
        self.scroll_view = ScrollView(do_scroll_y=True)
        self.add_widget(self.scroll_view)
        self.scroll_view.add_widget(self.grid_layout)

    def on_pre_enter(self, *args):
        self.grid_layout.clear_widgets()
        for idea in self.get_ideas():
            new_dynamic_widget = HeartfeltHellosNewIdeaButton(idea, on_press=lambda x: print("Pressed Idea Button"))
            self.grid_layout.add_widget(new_dynamic_widget)

    def on_leave(self, *args):
        self.grid_layout.clear_widgets()

    def get_ideas(self) -> list:
        # Default: Give general ideas (can be overridden in subclasses)
        return [Idea("Do you have a cat?", ["Tag 1", "Tag 2"]),
                Idea("Do you like video games?", ["Tag 3", "Tag 4"]),
                Idea("Seen any good movies?", ["Tag 3", "Tag 4"]),
                Idea("Learned any interesting facts lately?", ["Tag 3", "Tag 4"]),
                Idea("What's changed since I last heard from you?", ["Tag 3", "Tag 4"]),
                Idea("If you could be any animal, what would you be?", ["Tag 3", "Tag 4"])]

    def get_header(self):
        return "General Ideas"
