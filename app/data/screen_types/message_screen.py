from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.app import App
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
        App.get_running_app().set_on_back_pressed_callback(self.on_back_pressed)
        self.master_layout = BoxLayout(orientation='vertical')
        self.name_layout = BoxLayout(size_hint_y=0.1, orientation='horizontal')
        self.message_layout = BoxLayout(size_hint_y=None, orientation='vertical', padding='10dp', spacing='10dp')
        self.message_layout.bind(minimum_height=self.message_layout.setter("height"))
        self.writing_layout = BoxLayout(size_hint_y=0.1, orientation='horizontal')
        self.message_scroll = ScrollView(do_scroll_y=True)
        self.message_scroll.add_widget(self.message_layout)
        self.add_widget(self.master_layout)
        self.master_layout.add_widget(self.name_layout)
        self.master_layout.add_widget(self.message_scroll)
        self.master_layout.add_widget(self.writing_layout)
        self.name_layout.add_widget(ColoredLabel((0.5, 0.5, 0.5, 1), text=App.get_running_app().stored_data.message_recipient.name))
        self.text_input = TextInput(text=App.get_running_app().stored_data.temp_selected_idea.prompt, size_hint_x=0.8)
        self.text_input.bind(text=self.on_text_change)
        self.writing_layout.add_widget(self.text_input)
        self.send_button = Button(text="Send", size_hint_x=0.2, on_press=self.on_message_sent)
        self.writing_layout.add_widget(self.send_button)
        self.load_initial_messages()

    def load_initial_messages(self):
        name = App.get_running_app().stored_data.message_recipient.name
        history_for_name = App.get_running_app().stored_data.message_history.get(name, None)
        if history_for_name is None:
            return
        for message in history_for_name:
            self.message_layout.add_widget(ColoredLabel(message[1], text=message[0], size_hint_y=None, height="30dp"))

    def on_text_change(self, widget, text):
        if text == "":
            self.send_button.disabled = True
        else:
            self.send_button.disabled = False

    def on_message_sent(self, arg):
        # TODO change long time no see to something custom
        if self.text_input.text == "":
            return
        idea = App.get_running_app().stored_data.temp_selected_idea
        self.message_layout.add_widget(ColoredLabel((0, 0.5, 1), text=self.text_input.text, size_hint_y=None, height="30dp"))
        self.message_layout.add_widget(ColoredLabel((0.4, 0.4, 0.4), text=idea.response, size_hint_y=None, height="30dp"))
        name = App.get_running_app().stored_data.message_recipient.name
        history_for_name = App.get_running_app().stored_data.message_history.get(name, [])
        history_for_name.append((self.text_input.text, (0, 0.5, 1)))
        history_for_name.append((idea.response, (0.4, 0.4, 0.4)))
        App.get_running_app().stored_data.message_history[name] = history_for_name
        self.text_input.text = ""

    def on_back_pressed(self):
        App.get_running_app().stored_data.message_recipient = None
        App.get_running_app().remove_on_back_pressed_callback()
