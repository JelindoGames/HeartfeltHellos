from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from app.main import ShowcaseScreen
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton


class CreatePersonOptionsScreen(ShowcaseScreen):

    scroll_view = None
    grid_layout = None

    def __init__(self, **kwargs):
        super(CreatePersonOptionsScreen, self).__init__(**kwargs)
        self.grid_layout = GridLayout(spacing='10dp', padding='10dp', cols=1, size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter("height"))
        from_scratch = HeartfeltHellosButton(text="Create from Scratch", size_hint_y=None, height="80dp",
                                             on_press=lambda w: App.get_running_app().go_screen("Friend_Creation_First_Step"))
        from_contact = HeartfeltHellosButton(text="Create from Contact", size_hint_y=None, height="80dp",
                                             on_press=lambda w: App.get_running_app().go_screen("Contact_List"))
        self.grid_layout.add_widget(from_scratch)
        self.grid_layout.add_widget(from_contact)
        self.scroll_view = ScrollView(do_scroll_y=True)
        self.add_widget(self.scroll_view)
        self.scroll_view.add_widget(self.grid_layout)
