from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.app import App
from app.widgets.new_idea_button import HeartfeltHellosNewIdeaButton
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton


class MessageScreen(Screen):

    master_layout = None
    name_layout = None
    message_layout = None
    writing_layout = None

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.master_layout = BoxLayout(orientation='vertical')
        self.name_layout = BoxLayout(size_hint_y=0.1, orientation='horizontal')
        self.message_layout = BoxLayout(size_hint_y=0.8, orientation='vertical')
        self.writing_layout = BoxLayout(size_hint_y=0.1, orientation='horizontal')
        self.add_widget(self.master_layout)
        self.master_layout.add_widget(self.name_layout)
        self.master_layout.add_widget(self.message_layout)
        self.master_layout.add_widget(self.writing_layout)
        self.name_layout.add_widget(Label(text=App.get_running_app().stored_data.temp_selected_person.name))
        self.writing_layout.add_widget(TextInput(text=App.get_running_app().stored_data.temp_selected_idea.prompt, size_hint_x=0.8))
        self.writing_layout.add_widget(HeartfeltHellosButton(text="Send", size_hint_x=0.2))

    def send_message(self, message):
        print(message)
