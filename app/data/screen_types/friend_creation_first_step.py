from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from app.main import ShowcaseScreen
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton
from app.widgets.heartfelt_hellos_step_progression_button import HeartfeltHellosStepProgressionButton
from app.data.data_types.friend import Friend


class FriendCreationScreenFirstStep(ShowcaseScreen):
    scroll_view = None
    grid_layout = None

    def __init__(self, **kwargs):
        super(FriendCreationScreenFirstStep, self).__init__(**kwargs)
        self.tags = ["books", "movies", "sports"]
        self.friends = []
        # self.progress_grid = GridLayout(spacing='10dp', padding='10dp', cols=5, size_hint_y=None)
        self.grid_layout = GridLayout(spacing='10dp', padding='10dp', cols=1, size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter("height"))
        self.scroll_view = ScrollView(do_scroll_y=True)
        self.add_widget(self.scroll_view)
        self.scroll_view.add_widget(self.grid_layout)

    def on_pre_enter(self, *args):
        self.stepOne()

    def stepOne(self):
        self.grid_layout.clear_widgets()
        self.grid_layout.add_widget(Label(text="Step 1: What is their name?", font_size=24, color=(255, 255, 255)))
        self.grid_layout.add_widget(Label())

        # text box
        textinput = TextInput(hint_text="Enter Name Here", font_size=24, size_hint_y=None, multiline=False)
        self.grid_layout.add_widget(textinput)
        # self.name = textinput.text

        # next and back button rendering
        next_button = HeartfeltHellosStepProgressionButton(text="next", on_press=lambda x: App.get_running_app().go_screen("Friend_Creation_Second_Step", "left"))
        progress_grid = GridLayout(spacing='10dp', padding='10dp', cols=3, size_hint_y=None)
        progress_grid.add_widget(Label())
        progress_grid.add_widget(Label())
        progress_grid.add_widget(next_button)
        self.grid_layout.add_widget(progress_grid)