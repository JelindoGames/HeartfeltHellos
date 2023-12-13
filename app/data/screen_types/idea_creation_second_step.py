from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from app.main import ShowcaseScreen
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton
from app.widgets.heartfelt_hellos_step_progression_button import HeartfeltHellosStepProgressionButton
from app.data.data_types.friend import Friend
from app.data.data_types.idea import Idea



class IdeaCreationScreenSecondStep(ShowcaseScreen):
    master_layout = None
    scroll_view = None
    grid_layout = None
    progress_layout = None
    tags_selected = []

    def __init__(self, **kwargs):
        super(IdeaCreationScreenSecondStep, self).__init__(**kwargs)
        #self.friends = []
        self.master_layout = GridLayout(spacing='10dp', padding='10dp', cols=1)
        self.master_layout.add_widget(
            Label(text="What tags are related to the idea?", font_name="Raleway", font_size="20dp", height="50dp", color=(255, 255, 255),
                  size_hint_y=None))
        # search tag text box
        textinput = TextInput(hint_text="Search Tag here", font_name="Raleway", height="50dp", font_size="24dp", size_hint_y=None)
        textinput.bind(text=lambda a, v: self.refresh_tags(v))
        self.master_layout.add_widget(textinput)
        # adding tag button
        add_tag_button = HeartfeltHellosButton(text="add tag", height="50dp", on_press=self.add_tag, size_hint_y=None)
        add_tag_button.background_color = (0.5, 0.5, 0.8)
        self.master_layout.add_widget(add_tag_button)
        self.add_widget(self.master_layout)

        # tags
        self.grid_layout = GridLayout(spacing='10dp', padding='10dp', cols=1, size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter("height"))
        self.scroll_view = ScrollView(do_scroll_y=True)
        self.master_layout.add_widget(self.scroll_view)
        self.scroll_view.add_widget(self.grid_layout)

        # next button
        self.progress_layout = GridLayout(rows=1, size_hint_y=0.2)
        self.master_layout.add_widget(self.progress_layout)

    def on_pre_enter(self, *args):
        self.tags_selected = []
        self.tags = []
        self.tags.append("general")
        for tag in App.get_running_app().stored_data.tags: 
            isAdded = False
            if (len(self.tags) != 0):
                # compare tag lexiconically and place in the right spot
                    for ordered_tag in self.tags:
                        if (ordered_tag > tag):
                            self.tags.insert(self.tags.index(ordered_tag), tag)
                            isAdded = True
                            break
            
            if (not isAdded):              
                self.tags.append(tag)
                isAdded = True

        # self.tags = []
        # self.tags.append("general")
        # for tag in App.get_running_app().stored_data.tags: 
        #     self.tags.append(tag)

        self.refresh_tags()
        self.refresh_progress_layout()

    def refresh_tags(self, tag_filter=""):
        self.grid_layout.clear_widgets()
        for tag in self.tags:
            if tag_filter in tag:
                bg = (0, 0.5, 1) if tag in self.tags_selected else (.678, .847, 0.902)
                tag_button = HeartfeltHellosButton(text=tag, height="50dp", on_press=lambda x: self.pressTag(x.text),
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
        create_idea_button = HeartfeltHellosStepProgressionButton(text="Post Idea", on_press=self.create_post)
        self.progress_layout.add_widget(Label())  # Filler
        self.progress_layout.add_widget(create_idea_button)

    def add_tag(self, _): 
        self.grid_layout.clear_widgets()
        App.get_running_app().stored_data.idea_screen_history.append("Idea_Creation_Second_Step")
        App.get_running_app().go_screen("Tag_Creation_Screen", "left")


    def create_post(self, _):
        # create and add idea to stored list of ideas
        App.get_running_app().stored_data.ideas.append(Idea(App.get_running_app().stored_data.temp_prompt, [], self.tags_selected, "Hey, long time no see!"))
        next_screen = App.get_running_app().stored_data.idea_screen_history[-1]
        App.get_running_app().stored_data.idea_screen_history = App.get_running_app().stored_data.idea_screen_history[:-1]
        App.get_running_app().go_screen(next_screen, "left")

    def on_leave(self, *args):
        self.grid_layout.clear_widgets()