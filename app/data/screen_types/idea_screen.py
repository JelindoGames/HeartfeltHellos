from app.main import ShowcaseScreen
from app.widgets.heartfelt_hellos_idea_button import HeartfeltHellosIdeaButton


class IdeaScreen(ShowcaseScreen):

    dynamic_widget = None

    def on_pre_enter(self, *args):
        print("PreEnter")
        self.dynamic_widget = HeartfeltHellosIdeaButton()
        self.dynamic_widget.text = "Dynamic Button"
        self.ids.Test.add_widget(self.dynamic_widget)

    def on_leave(self, *args):
        self.ids.Test.remove_widget(self.dynamic_widget)
