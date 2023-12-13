from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.metrics import dp
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton



class TitleScreen(Screen):

    box_layout = None

    def __init__(self, **kwargs):
        super(TitleScreen, self).__init__(**kwargs)
        App.get_running_app().general_tab_pressed = False
        App.get_running_app().friend_tab_pressed = False
        App.get_running_app().viewed_idea_tab_pressed = False
        self.clear_widgets()
        self.box_layout = BoxLayout(orientation="vertical", padding="10dp")
        self.box_layout.add_widget(Label(text="Let's Reconnect!", font_name="Raleway", font_size="42dp", halign="center",
                                         valign="middle", text_size=(dp(400), None), color=(0, 0, 0),
                                         size_hint_y=None, height="70dp"))
        self.box_layout.add_widget(Label(text="What type of conversation ideas do you want?",font_name="Raleway",
                                         font_size="24dp", valign="middle", halign="center", text_size=(dp(325), None),
                                         color=(0, 0, 0), size_hint_y=None, height="60dp"))
        self.box_layout.add_widget(Label(text="", size_hint_y=None, height="160dp"))
        self.add_widget(self.box_layout)

    def on_viewed_ideas_clicked(self, widget):
        App.get_running_app().go_screen("Viewed_Idea_Screen", "left")
