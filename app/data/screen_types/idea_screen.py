from app.main import ShowcaseScreen
from app.widgets.heartfelt_hellos_idea_button import HeartfeltHellosIdeaButton


class IdeaScreen(ShowcaseScreen):

    def on_pre_enter(self, *args):
        print("PreEnter")
        new_dynamic_widget = HeartfeltHellosIdeaButton()
        new_dynamic_widget.text = "Dynamic Button"
        self.ids.Test.add_widget(new_dynamic_widget)
        #self.ids.Test.remove_widget(new_dynamic_widget)
