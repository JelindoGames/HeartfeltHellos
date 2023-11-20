from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.app import App
from app.widgets.new_idea_button import HeartfeltHellosNewIdeaButton
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton
from app.widgets.colored_label import ColoredLabel


class MessageScreen(Screen):

    master_layout = None
    name_layout = None
    message_layout = None
    message_scroll = None
    writing_layout = None
    text_input = None

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.master_layout = BoxLayout(orientation='vertical')
        self.name_layout = BoxLayout(size_hint_y=0.1, orientation='horizontal')
        self.message_layout = BoxLayout(size_hint_y=0.8, orientation='vertical', padding='10dp', spacing='10dp')
        self.writing_layout = BoxLayout(size_hint_y=0.1, orientation='horizontal')
        self.message_scroll = ScrollView(do_scroll_y=True)
        self.message_scroll.add_widget(self.message_layout)
        self.add_widget(self.master_layout)
        self.master_layout.add_widget(self.name_layout)
        self.master_layout.add_widget(self.message_scroll)
        self.master_layout.add_widget(self.writing_layout)
        self.name_layout.add_widget(ColoredLabel((0.5, 0.5, 0.5, 1), text=App.get_running_app().stored_data.temp_selected_person.name))
        self.text_input = TextInput(text=App.get_running_app().stored_data.temp_selected_idea.prompt, size_hint_x=0.8)
        self.writing_layout.add_widget(self.text_input)
        self.writing_layout.add_widget(Button(text="Send", size_hint_x=0.2, on_press=self.on_message_sent))

    def send_message(self, message):
        print(message)

    def on_message_sent(self, arg):
        self.message_layout.add_widget(ColoredLabel((0, 0.5, 1), text=self.text_input.text, size_hint_y=None, height="30dp"))
        self.message_layout.add_widget(ColoredLabel((0.4, 0.4, 0.4), text="Hey, long time no see!", size_hint_y=None, height="30dp"))
        self.text_input.text = ""
