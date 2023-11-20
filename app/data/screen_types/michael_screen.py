from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton


class MichaelScreen(Screen):

    box_layout = None
    tags_layout = None
    scroll_view = None

    def __init__(self, **kwargs):
        super(MichaelScreen, self).__init__(**kwargs)
        self.clear_widgets()
        self.box_layout = BoxLayout(orientation="vertical", padding=10)
        selected_friend = App.get_running_app().stored_data.temp_selected_person
        self.box_layout.add_widget(Label(text=f"Select one of {selected_friend.name}'s interests.", font_size=32, size_hint_y=None, height=60, color=(0, 0, 0)))
        self.box_layout.add_widget(Label(text="_________________________", font_size=40, halign="center", size_hint_y=None, height=40, color=(0, 0, 0)))
        self.tags_layout = GridLayout(spacing='10dp', padding='10dp', cols=1, size_hint_y=None)
        self.tags_layout.bind(minimum_height=self.tags_layout.setter("height"))
        self.scroll_view = ScrollView(do_scroll_y=True)
        self.box_layout.add_widget(self.scroll_view)
        self.scroll_view.add_widget(self.tags_layout)
        for tag in selected_friend.tags:
            self.tags_layout.add_widget(HeartfeltHellosButton(text=tag, size_hint_y=None, height=48))
        self.add_widget(self.box_layout)
