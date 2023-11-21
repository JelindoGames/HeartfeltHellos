from app.data.screen_types.idea_screen import IdeaScreen
from app.data.data_types.idea import Idea


class SubIdeaScreen(IdeaScreen):

    def get_ideas(self):
        return [Idea("Why don't you play anymore?", 4.0, ["Tag 1", "Tag 2"]),
                Idea("How'd your latest game go?", 3.6, ["Tag 3", "Tag 4"])]

    def get_header(self):
        return "Sub-Ideas"

    def get_idea_screen_name(self):
        return "Sub_Idea_Screen"

    def is_top_level_idea_screen(self):
        return False

    def reset_selected_person(self):
        return False
