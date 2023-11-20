from app.data.screen_types.idea_screen import IdeaScreen
from app.data.data_types.idea import Idea


class SubIdeaScreen(IdeaScreen):

    def get_ideas(self):
        return [Idea("Sub Idea 1", ["Tag 1", "Tag 2"]), Idea("Sub Idea 2", ["Tag 3", "Tag 4"])]

    def get_header(self):
        return "Sub-Ideas"
