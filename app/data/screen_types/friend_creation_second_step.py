from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from app.main import ShowcaseScreen
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton
from app.widgets.heartfelt_hellos_step_progression_button import HeartfeltHellosStepProgressionButton
from app.data.data_types.friend import Friend


class FriendCreationScreenSecondStep(ShowcaseScreen):
    master_layout = None
    scroll_view = None
    grid_layout = None
    progress_layout = None
    tags_selected = []

    def __init__(self, **kwargs):
        super(FriendCreationScreenSecondStep, self).__init__(**kwargs)
        self.master_layout = GridLayout(spacing='10dp', padding='10dp', cols=1)
        self.master_layout.add_widget(
            Label(text="Step 2: What are their interests?", font_name="Raleway", font_size="20dp", height="50dp", color=(255, 255, 255),
                  size_hint_y=None))
        textinput = TextInput(hint_text="Search Tag here", font_name="Raleway", height="50dp", font_size="24dp", size_hint_y=None)
        textinput.bind(text=lambda a, v: self.refresh_tags(v))
        self.master_layout.add_widget(textinput)
        self.add_widget(self.master_layout)

        self.grid_layout = GridLayout(spacing='10dp', padding='10dp', cols=1, size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter("height"))
        self.scroll_view = ScrollView(do_scroll_y=True)
        self.master_layout.add_widget(self.scroll_view)
        self.scroll_view.add_widget(self.grid_layout)

        self.progress_layout = GridLayout(rows=1, size_hint_y=0.2)
        self.master_layout.add_widget(self.progress_layout)

    def on_pre_enter(self, *args):
        self.tags = App.get_running_app().stored_data.tags
        self.tags_selected = []
        self.refresh_tags()
        self.refresh_progress_layout()

    def refresh_tags(self, tag_filter=""):
        self.grid_layout.clear_widgets()
        for tag in self.tags:
            if tag_filter in tag:
                bg = (0, 0.5, 1) if tag in self.tags_selected else (.678, .847, 0.902)
                tag_button = HeartfeltHellosButton(text=tag, size_hint_y=None, height='60dp', on_press=lambda x: self.pressTag(x.text))
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
        create_person_button = HeartfeltHellosStepProgressionButton(text="Create Friend", on_press=self.createFriend)
        self.progress_layout.add_widget(Label())  # Filler
        self.progress_layout.add_widget(create_person_button)

    def createFriend(self, _):
        new_friend = Friend(App.get_running_app().stored_data.temp_friend_name, self.tags_selected)
        App.get_running_app().stored_data.friends.append(new_friend)
        App.get_running_app().go_screen(App.get_running_app().stored_data.previous_friend_list_screen, "left")

    def on_leave(self, *args):
        self.grid_layout.clear_widgets()
