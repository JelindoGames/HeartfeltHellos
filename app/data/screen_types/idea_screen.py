from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.app import App
from app.main import ShowcaseScreen
from app.widgets.new_idea_button import HeartfeltHellosNewIdeaButton
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton
from app.data.data_types.idea import Idea


class IdeaScreen(ShowcaseScreen):

    scroll_view = None
    grid_layout = None

    def __init__(self, **kwargs):
        super(IdeaScreen, self).__init__(**kwargs)
        self.grid_layout = GridLayout(spacing='20dp', padding='20dp', cols=1, size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter("height"))
        self.scroll_view = ScrollView(do_scroll_y=True)
        self.add_widget(self.scroll_view)
        self.scroll_view.add_widget(self.grid_layout)
        if self.is_top_level_idea_screen():
            App.get_running_app().stored_data.idea_screen_history = []
            App.get_running_app().stored_data.idea_history = []
        self.consider_reset_selected_person()

    def on_pre_enter(self, *args):
        self.grid_layout.clear_widgets()
        post_idea_button = HeartfeltHellosButton(text="+ Post Idea", font_size="20dp", size_hint_y=None, on_press=lambda x: self.on_create_idea_pressed())
        post_idea_button.background_color = (0.5, 0.5, 0.8)
        self.grid_layout.add_widget(post_idea_button)
        if (len(self.get_ideas()) > 0):
            for idea in self.get_ideas():
                new_dynamic_widget = HeartfeltHellosNewIdeaButton(idea, self.get_idea_screen_name())
                self.grid_layout.add_widget(new_dynamic_widget)
        else:
            new_label = Label(text="There seems to be a lack of ideas. Perhaps you could add your own and help others!",
                              size_hint_y=None, text_size=(dp(320), None), color=(0,0,0), font_size="18dp", font_name="Raleway", halign="center", valign="middle")
            self.grid_layout.add_widget(new_label)

    def on_leave(self, *args):
        self.grid_layout.clear_widgets()

    def get_ideas(self) -> list:
        ideas = App.get_running_app().stored_data.ideas
        # Default: Give general ideas (can be overridden in subclasses)
        general_ideas = []
        for idea in ideas:
            isAdded = False
            if (idea.hasTag("general")) :
                # adding to sort
                if (len(general_ideas) != 0):
                    # compare rating and place in the right spot
                    for gen_idea in general_ideas:
                        if (gen_idea.get_rating() < idea.get_rating()):
                            general_ideas.insert(general_ideas.index(gen_idea), idea)
                            isAdded = True
                            break

                if (not isAdded):              
                    general_ideas.append(idea)
                    isAdded = True

        return general_ideas

    def get_header(self):
        return "General Ideas"

    def get_idea_screen_name(self):
        return "General_Idea_Screen"

    def on_create_idea_pressed(self):
        App.get_running_app().remove_on_back_pressed_callback()
        App.get_running_app().stored_data.idea_screen_history.append(self.get_idea_screen_name())
        App.get_running_app().go_screen("Idea_Creation_First_Step", "left")

    def is_top_level_idea_screen(self):
        return True

    def consider_reset_selected_person(self):
        if self.reset_selected_person():
            App.get_running_app().stored_data.temp_selected_person = None

    def reset_selected_person(self):
        return True
