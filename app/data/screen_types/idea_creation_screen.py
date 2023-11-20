from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from app.main import ShowcaseScreen
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton
from app.widgets.heartfelt_hellos_step_progression_button import HeartfeltHellosStepProgressionButton
from app.data.data_types.idea import Idea


class IdeaCreationScreen(ShowcaseScreen):

    scroll_view = None
    grid_layout = None

    def __init__(self, **kwargs):
        super(IdeaCreationScreen, self).__init__(**kwargs)
        # NOTE: replace tags and ideas with global list so that it can be editted in this class
        self.tags=["books", "movies", "sports"] 
        self.ideas=[]
        #self.progress_grid = GridLayout(spacing='10dp', padding='10dp', cols=5, size_hint_y=None)
        self.grid_layout = GridLayout(spacing='10dp', padding='10dp', cols=1, size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter("height"))
        self.scroll_view = ScrollView(do_scroll_y=True)
        self.add_widget(self.scroll_view)
        self.scroll_view.add_widget(self.grid_layout)


    def on_pre_enter(self, *args):
        self.stepOne()
        

    def stepOne(self):
        self.grid_layout.clear_widgets()
        self.grid_layout.add_widget(Label(text="What is your conversation idea?", font_size=24, color=(255,255,255)))
        self.grid_layout.add_widget(Label())

        # text box
        textinput = TextInput(text="Are you still into sports?", font_size=24, size_hint_y=None, multiline=False)
        self.grid_layout.add_widget(textinput)
        #self.name = textinput.text

        # next and back button rendering
        next_button = HeartfeltHellosStepProgressionButton(text="next",on_press=lambda x: self.stepTwo(textinput.text))
        progress_grid=GridLayout(spacing='10dp', padding='10dp', cols=3, size_hint_y=None)
        progress_grid.add_widget(Label())
        progress_grid.add_widget(Label())
        progress_grid.add_widget(next_button)
        self.grid_layout.add_widget(progress_grid)


    def stepTwo(self, prompt):
        self.grid_layout.clear_widgets()
        self.prompt=prompt
        self.grid_layout.add_widget(Label(text="Search and select the tag(s)\nthat matches with your idea!", height=50, color=(255,255,255), size_hint_y=None))

        # text box
        #NOTE TO SELF: add filtering for search bar
        textinput = TextInput(text="Search Tag here", height=50, font_size=24, size_hint_y=None)
        #textinput.bind(on_text_validate=on_enter(textinput.text))
        self.grid_layout.add_widget(textinput)

        # NOTE TO SELF: add scroll bar to tags section
        #tag_grid=GridLayout(spacing='10dp', padding='10dp', cols=1, size_hint_y=None)
        for tag in self.getTags():
            tag_button = HeartfeltHellosButton(text=tag, height=50, on_press=lambda x: self.pressTag(x.text), size_hint_y=None)
            self.grid_layout.add_widget(tag_button)
        #self.grid_layout.add_widget(tag_grid)
        
        
        # next and back button rendering
        create_person_button = HeartfeltHellosStepProgressionButton(text="Create\nIdea", on_press=lambda x: self.createIdea())
        back_button = HeartfeltHellosStepProgressionButton(text="back", on_press=lambda x: self.stepOne())
        progress_grid=GridLayout(spacing='10dp', padding='10dp', cols=3, size_hint_y=None)
        progress_grid.add_widget(back_button)
        progress_grid.add_widget(Label())
        progress_grid.add_widget(create_person_button)
        self.grid_layout.add_widget(progress_grid)
    
    def pressTag(self, name: str):
        print("pressed " + str)
        if name not in self.tags:
            self.tags.append(name)
        else:
            self.tags.remove(name)

    def createIdea(self):
        print("pressed create idea")
        # NOTE: return to idea screen + add self.idea to global list of ideas as input somehow
        self.ideas.append(Idea(self.prompt, self.tags)) #place holder (something like that maybe?)

    def on_leave(self, *args):
        self.grid_layout.clear_widgets()

    def getTags(self) -> list:
        return ["sports", "books", "movies"]
