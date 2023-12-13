from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from app.data.data_types.idea import Idea
from app.main import ShowcaseScreen
from app.widgets.heartfelt_hellos_step_progression_button import HeartfeltHellosStepProgressionButton


class IdeaCreationScreenFirstStep(ShowcaseScreen):
    scroll_view = None
    grid_layout = None
    progress_grid = None
    next_button = None
    newest_idea = ""

    def __init__(self, **kwargs):
        super(IdeaCreationScreenFirstStep, self).__init__(**kwargs)
        App.get_running_app().set_on_back_pressed_callback(self.on_back_pressed)
        self.previous_screen = App.get_running_app().stored_data.idea_screen_history[-1]
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
        self.grid_layout.add_widget(Label(text="What's your conversation idea?", font_name="Raleway", font_size="20dp", size_hint_y=None, height="50dp", color=(255, 255, 255)))
        self.grid_layout.add_widget(Label())

        # text box
        textinput = TextInput(hint_text="Are you still into sports?", font_name="Raleway", font_size="24dp", size_hint_y=None, multiline=True)
        textinput.bind(text=self.on_idea_entered)
        self.grid_layout.add_widget(textinput)
        

    def on_idea_entered(self, attribute, value):
        self.newest_idea = value
        if value != "":
            self.consider_add_next_button()
        else:
            self.progress_grid.remove_widget(self.next_button)
            self.next_button = None

    def consider_add_next_button(self):
        if self.next_button is not None:
            return
        self.next_button = HeartfeltHellosStepProgressionButton(text="next", on_press=self.on_next_pressed)
        if App.get_running_app().stored_data.idea_screen_history[-1] == "Sub_Idea_Screen":
            self.next_button.text = "create\npost"
        if self.progress_grid is None:
            self.progress_grid = GridLayout(spacing='10dp', padding='10dp', cols=3, size_hint_y=None)
            self.progress_grid.add_widget(Label())
            self.progress_grid.add_widget(Label())
            self.grid_layout.add_widget(self.progress_grid)
        self.progress_grid.add_widget(self.next_button)

    def on_next_pressed(self, arg):        
        # storing idea prompt temporarily
        App.get_running_app().remove_on_back_pressed_callback()
        App.get_running_app().stored_data.temp_prompt = self.newest_idea
        # if in followups, use prev followup tags
        if App.get_running_app().stored_data.idea_screen_history[-1] == "Sub_Idea_Screen":
            App.get_running_app().stored_data.temp_selected_idea.followup.append(
                Idea(App.get_running_app().stored_data.temp_prompt, [],
                     App.get_running_app().stored_data.temp_selected_idea.tags, []))
            App.get_running_app().stored_data.idea_screen_history = App.get_running_app().stored_data.idea_screen_history[:-1]
            App.get_running_app().go_screen("Sub_Idea_Screen", "left")
        else:  
            # else, go to tag selection
            App.get_running_app().go_screen("Idea_Creation_Second_Step", "left")

    def on_back_pressed(self):
        del App.get_running_app().stored_data.idea_screen_history[-1]


