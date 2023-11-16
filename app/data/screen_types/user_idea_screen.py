from app.data.screen_types.idea_screen import IdeaScreen
from app.data.data_types.idea import Idea


class UserIdeaScreen(IdeaScreen):

    def get_ideas(self):
        return [Idea("User Idea 1", ["Tag 1", "Tag 2"]), Idea("User Idea 2", ["Tag 3", "Tag 4"])]
