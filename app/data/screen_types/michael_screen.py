from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.metrics import dp
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton



class MichaelScreen(Screen):

    box_layout = None
    tags_layout = None
    scroll_view = None

    def __init__(self, **kwargs):
        super(MichaelScreen, self).__init__(**kwargs)
        self.clear_widgets()
        self.box_layout = BoxLayout(orientation="vertical", padding="10dp")
        selected_friend = App.get_running_app().stored_data.temp_selected_person
        self.box_layout.add_widget(Label(text=f"Select one of {selected_friend.name}'s interests.", font_size="24dp", height="60dp", font_name="Raleway", text_size=(dp(300),None), size_hint_y=None, color=(0, 0, 0)))
        self.box_layout.add_widget(Label(text="_________________________", font_size="40dp", halign="center",  height="40dp", font_name="Raleway", text_size=(dp(300),None), size_hint_y=None, color=(0, 0, 0)))
        self.tags_layout = GridLayout(spacing='10dp', padding='10dp', cols=1, size_hint_y=None)
        self.tags_layout.bind(minimum_height=self.tags_layout.setter("height"))
        self.scroll_view = ScrollView(do_scroll_y=True)
        self.box_layout.add_widget(self.scroll_view)
        self.scroll_view.add_widget(self.tags_layout)
        for tag in selected_friend.tags:
            tag_button = HeartfeltHellosButton(text=tag, size_hint_y=None, height="48dp", on_press=lambda x: self.on_tag_clicked(x.text))
            self.tags_layout.add_widget(tag_button)
        self.add_widget(self.box_layout)

    def on_tag_clicked(self, value):
        App.get_running_app().stored_data.temp_selected_tag = value
        App.get_running_app().go_screen("User_Idea_Screen", "left")
