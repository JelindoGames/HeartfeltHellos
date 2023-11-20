from app.data.screen_types.idea_screen import IdeaScreen
from app.data.data_types.idea import Idea


class UserIdeaScreen(IdeaScreen):

    def get_ideas(self):
        return [Idea("Do you still play soccer?", ["Tag 1", "Tag 2"]),
                Idea("Did you see the game last Sunday?", ["Tag 3", "Tag 4"]),
                Idea("What's your favorite team lately?", ["Tag 3", "Tag 4"])]

    def get_header(self):
        return "User Ideas"
