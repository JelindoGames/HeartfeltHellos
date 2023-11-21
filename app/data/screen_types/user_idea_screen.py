from app.data.screen_types.idea_screen import IdeaScreen
from app.data.data_types.idea import Idea
from kivy.app import App


class UserIdeaScreen(IdeaScreen):

    def get_ideas(self):
        selected_tag = App.get_running_app().stored_data.temp_selected_tag
        # TODO something much more advanced
        if selected_tag == "sports":
            return [Idea("Do you still play soccer?", 4.2, ["Tag 1", "Tag 2"]),
                    Idea("Did you see the game last Sunday?", 3.9, ["Tag 3", "Tag 4"]),
                    Idea("What's your favorite team lately?", 3.5, ["Tag 3", "Tag 4"])]
        elif selected_tag == "movies":
            return [Idea("Have you seen the FNAF movie?", 4.1, ["Tag 1", "Tag 2"]),
                    Idea("What movies are you interested in seeing soon?", 3.8, ["Tag 1", "Tag 2"])]
        elif selected_tag == "books":
            return [Idea("Read any good books lately?", 3.7, ["Tag 1", "Tag 2"]),
                    Idea("What's the worst book you've ever read?", 3.2, ["Tag 1", "Tag 2"])]
        else:
            return []

    def get_header(self):
        return "User Ideas"

    def get_idea_screen_name(self):
        return "User_Idea_Screen"

    def is_top_level_idea_screen(self):
        return True

    def reset_selected_person(self):
        return False
