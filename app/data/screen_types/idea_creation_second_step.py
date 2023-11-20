from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from app.main import ShowcaseScreen
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton
from app.widgets.heartfelt_hellos_step_progression_button import HeartfeltHellosStepProgressionButton
from app.data.data_types.friend import Friend


class IdeaCreationScreenSecondStep(ShowcaseScreen):
    master_layout = None
    scroll_view = None
    grid_layout = None
    progress_layout = None
    tags = ["books", "movies", "sports"]
    tags_selected = []

    def __init__(self, **kwargs):
        super(IdeaCreationScreenSecondStep, self).__init__(**kwargs)
        #self.friends = []
        self.master_layout = GridLayout(spacing='10dp', padding='10dp', cols=1)
        self.master_layout.add_widget(
            Label(text="What tags are related to the idea?", height=50, color=(255, 255, 255),
                  size_hint_y=None))
        textinput = TextInput(hint_text="Search Tag here", height=50, font_size=24, size_hint_y=None)
        textinput.bind(text=lambda a, v: self.refresh_tags(v))
        self.master_layout.add_widget(textinput)
        self.add_widget(self.master_layout)

        self.grid_layout = GridLayout(spacing='10dp', padding='10dp', cols=1, size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter("height"))
        self.scroll_view = ScrollView(do_scroll_y=True)
        self.master_layout.add_widget(self.scroll_view)
        self.scroll_view.add_widget(self.grid_layout)

        self.progress_layout = GridLayout(rows=1, size_hint_y=0.1)
        self.master_layout.add_widget(self.progress_layout)

    def on_pre_enter(self, *args):
        self.tags_selected = []
        self.refresh_tags()
        self.refresh_progress_layout()

    def refresh_tags(self, tag_filter=""):
        self.grid_layout.clear_widgets()
        for tag in self.tags:
            if tag_filter in tag:
                bg = (0, 0.5, 1) if tag in self.tags_selected else (0.3, 0.3, 0.3)
                tag_button = HeartfeltHellosButton(text=tag, height=50, on_press=lambda x: self.pressTag(x.text),
                                                   size_hint_y=None)
                tag_button.background_color = bg
                self.grid_layout.add_widget(tag_button)

    def pressTag(self, name: str):
        if name not in self.tags_selected:
            self.tags_selected.append(name)
        else:
            self.tags_selected.remove(name)
        self.refresh_tags()
        self.refresh_progress_layout()

    def refresh_progress_layout(self):
        self.progress_layout.clear_widgets()
        if len(self.tags_selected) == 0:
            return
        create_person_button = HeartfeltHellosStepProgressionButton(text="Post Idea", on_press=self.create_post)
        #back_button = HeartfeltHellosStepProgressionButton(text="back", on_press=lambda x: self.stepOne())
        #self.progress_layout.add_widget(back_button)
        self.progress_layout.add_widget(Label())  # Filler
        self.progress_layout.add_widget(Label())  # Filler
        self.progress_layout.add_widget(create_person_button)

    def create_post(self, _):
        pass
        #new_friend = Friend(App.get_running_app().stored_data.temp_friend_name, self.tags)
        #App.get_running_app().stored_data.friends.append(new_friend)
        #App.get_running_app().go_screen("Friend_List", "left")
        #self.friends.append(Friend(self.name, self.tags))
        # return to friend list screen + add self.friends as input somehow

    def on_leave(self, *args):
        self.grid_layout.clear_widgets()