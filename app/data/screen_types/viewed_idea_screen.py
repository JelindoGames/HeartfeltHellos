from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.app import App
from app.main import ShowcaseScreen
from app.widgets.new_idea_button import HeartfeltHellosNewIdeaButton
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton
from app.data.data_types.idea import Idea


class ViewedIdeaScreen(ShowcaseScreen):

    scroll_view = None
    grid_layout = None

    def __init__(self, **kwargs):
        super(ViewedIdeaScreen, self).__init__(**kwargs)
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
        viewed_ideas = self.get_ideas()
        
        if (len(viewed_ideas) > 0):
            for idea in viewed_ideas:
                new_dynamic_widget = HeartfeltHellosNewIdeaButton(idea, self.get_idea_screen_name())
                self.grid_layout.add_widget(new_dynamic_widget)
        else:
            new_label = Label(text="\n\n\nYou haven't viewed any ideas yet! Click on an idea in the general tab below and come back here to see what you've viewed!",
                              size_hint_y=None, text_size=(dp(320), None), color=(0,0,0), font_size="25dp", font_name="Raleway", halign="center")
            self.grid_layout.add_widget(new_label)

    def on_leave(self, *args):
        self.grid_layout.clear_widgets()

    def get_ideas(self) -> list:
        ideas = App.get_running_app().stored_data.viewed_ideas
        viewed_ideas = []
        for idea in ideas:
            # isAdded = False
            # if (len(viewed_ideas) != 0):
            # # compare rating and place in the right spot
            #     for gen_idea in viewed_ideas:
            #         if (gen_idea.get_rating() < idea.get_rating()):
            #             viewed_ideas.insert(viewed_ideas.index(gen_idea), idea)
            #             isAdded = True
            #             break

            # if (not isAdded):              
            #     viewed_ideas.append(idea)
            #     isAdded = True

            # insert idea to the front of the list to be displayed in viewing order
            viewed_ideas.insert(0, idea)

        return ideas

    def get_header(self):
        return "Viewed Idea Screen"

    def get_idea_screen_name(self):
        return "Viewed_Idea_Screen"

    def is_top_level_idea_screen(self):
        return True

    def consider_reset_selected_person(self):
        if self.reset_selected_person():
            App.get_running_app().stored_data.temp_selected_person = None

    def reset_selected_person(self):
        return True
