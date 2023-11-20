from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.core.window import Window  # Make sure to import Window
from kivy.app import App

class ContactScreen(Screen):
    def __init__(self, **kwargs):
        super(ContactScreen, self).__init__(**kwargs)  # Make sure this is called
        self.layout = GridLayout(cols=1, spacing=2, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))

        # Fake contacts
        contacts = ["Anna", "Bernard", "Charlie", "Diana", "Ethan", "Fiona", "Michael", "Nora", "Oliver", "Pamela"]
        for contact in contacts:
            btn = Button(text=contact, size_hint_y=None, height=dp(50))
            btn.bind(on_press=self.go_to_next_screen)
            self.layout.add_widget(btn)

        # ScrollView
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        scroll_view.add_widget(self.layout)
        self.add_widget(scroll_view)

    def go_to_next_screen(self, instance):
        if instance.text == "Michael":
            App.get_running_app().go_screen('Next_Screen_Name', 'left')
        else:
            print(f"Contact {instance.text} selected, but no action taken.")
