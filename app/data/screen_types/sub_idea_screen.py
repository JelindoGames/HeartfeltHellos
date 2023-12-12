from app.data.screen_types.idea_screen import IdeaScreen
from kivy.app import App

from app.data.data_types.idea import Idea


class SubIdeaScreen(IdeaScreen):

    def get_ideas(self):
        App.get_running_app().stored_data.previous_idea_screen = "Sub_Idea_Screen"
        return App.get_running_app().stored_data.idea_history[-1].followup

    def get_header(self):
        return "Sub-Ideas"

    def get_idea_screen_name(self):
        return "Sub_Idea_Screen"

    def is_top_level_idea_screen(self):
        return False

    def reset_selected_person(self):
        return False
