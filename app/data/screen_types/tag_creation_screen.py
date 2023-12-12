from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from app.main import ShowcaseScreen
from app.widgets.heartfelt_hellos_step_progression_button import HeartfeltHellosStepProgressionButton


class TagCreationScreen(ShowcaseScreen):
    scroll_view = None
    grid_layout = None
    progress_grid = None
    next_button = None
    newest_tag = ""

    def __init__(self, **kwargs):
        super(TagCreationScreen, self).__init__(**kwargs)
        self.tags = App.get_running_app().stored_data.tags
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
        self.grid_layout.add_widget(Label(text="What is the tag called?", font_name="Raleway", font_size="20dp", height="50dp", color=(255, 255, 255), size_hint_y=None))

        # text box
        textinput = TextInput(hint_text="Enter Tag Here", font_name="Raleway", height="50dp", font_size="24dp", size_hint_y=None, multiline=False)
        textinput.bind(text=self.on_name_entered)
        self.grid_layout.add_widget(textinput)
        # self.name = textinput.text

    def on_name_entered(self, attribute, value):
        self.newest_tag = value
        if value != "":
            self.consider_add_next_button()
        else:
            self.progress_grid.remove_widget(self.next_button)
            self.next_button = None

    def consider_add_next_button(self):
        if self.next_button is not None:
            return
        self.next_button = HeartfeltHellosStepProgressionButton(text="create\ntag", on_press=self.on_create_tag_pressed)
        if self.progress_grid is None:
            self.progress_grid = GridLayout(spacing='10dp', padding='10dp', cols=3, size_hint_y=None)
            self.progress_grid.add_widget(Label())
            self.progress_grid.add_widget(Label())
            self.grid_layout.add_widget(self.progress_grid)
        self.progress_grid.add_widget(self.next_button)
        

    def on_create_tag_pressed(self, arg):
        App.get_running_app().stored_data.tags.append(self.newest_tag)
        next_screen = App.get_running_app().stored_data.idea_screen_history[-1]
        App.get_running_app().stored_data.idea_screen_history = App.get_running_app().stored_data.idea_screen_history[:-1]
        App.get_running_app().go_screen(next_screen, "left")

