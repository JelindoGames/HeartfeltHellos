from app.data.screen_types.idea_screen import IdeaScreen
from app.data.data_types.idea import Idea
from kivy.app import App


class UserIdeaScreen(IdeaScreen):

    def get_ideas(self):
        selected_tag = App.get_running_app().stored_data.temp_selected_tag
        App.get_running_app().stored_data.previous_idea_screen = "Idea_Share_Rate_Screen"
        return self.get_ideas_with_tag(selected_tag)
    
    def get_ideas_with_tag(self, tag: str):
        ideas_with_tag = []
        for idea in App.get_running_app().stored_data.ideas:
            isAdded = False
            if (idea.hasTag(tag)) :
                # adding to sort
                if (len(ideas_with_tag) != 0):
                    # compare rating and place in the right spot
                    for tag_idea in ideas_with_tag:
                        if (tag_idea.get_rating() < idea.get_rating()):
                            ideas_with_tag.insert(ideas_with_tag.index(tag_idea), idea)
                            isAdded = True
                            break

                if (not isAdded):              
                    ideas_with_tag.append(idea)
                    isAdded = True
            
        return ideas_with_tag

    def get_header(self):
        return "User Ideas"

    def get_idea_screen_name(self):
        return "User_Idea_Screen"

    def is_top_level_idea_screen(self):
        return True

    def reset_selected_person(self):
        return False
