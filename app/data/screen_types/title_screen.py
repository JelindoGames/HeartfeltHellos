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
        self.clear_widgets()
        self.box_layout = BoxLayout(orientation="vertical", padding="10dp")
        # viewed_ideas = App.get_running_app().stored_data.viewed_ideas
        if (len(App.get_running_app().stored_data.viewed_ideas) != 0):
            viewed_ideas_button = HeartfeltHellosButton(text="See previously\nviewed ideas", size_hint_y=None, height="96dp", on_press=self.on_viewed_ideas_clicked)
            self.box_layout.add_widget(viewed_ideas_button)
        self.box_layout.add_widget(Label(text="Let's Reconnect!", font_name="Raleway", font_size="45dp", halign="center", valign="middle", text_size=(dp(400), None), color=(0, 0, 0))) 
        self.box_layout.add_widget(Label(text="\n\n\n\nWhat type of conversation ideas do you want?",font_name="Raleway", font_size="27dp", valign="middle",
                              halign="center", text_size=(dp(325), None), color= (0, 0, 0)))
        self.add_widget(self.box_layout)

    def on_viewed_ideas_clicked(self, widget):
        # App.get_running_app().stored_data.temp_selected_tag = value
        print("viewed ideas button pressed")
        App.get_running_app().go_screen("Viewed_Idea_Screen", "left")
