from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

class MyMobileApp(FloatLayout):
    def __init__(self, **kwargs):
        super(MyMobileApp, self).__init__(**kwargs)

        # Title Label
        title_label = Label(text='Welcome', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'top': 0.95})
        self.add_widget(title_label)

        # Name Input
        self.name_input = TextInput(hint_text='Name', multiline=False, size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'top': 0.85})
        self.add_widget(self.name_input)

        # Email Input
        self.email_input = TextInput(hint_text='Email', multiline=False, size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'top': 0.75})
        self.add_widget(self.email_input)

        # City Dropdown
        self.city_dropdown = Spinner(
            text='Select City',
            values=['Boston', 'New York', 'San Francisco'],
            size_hint=(None, None),
            size=(300, 50),
            pos_hint={'center_x': 0.5, 'top': 0.65}
        )
        self.add_widget(self.city_dropdown)

        # Submit Button
        submit_button = Button(text='Submit', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5, 'y': 0.45})
        submit_button.bind(on_press=self.show_popup)
        self.add_widget(submit_button)

    def show_popup(self, instance):
        content = BoxLayout(orientation='vertical')

        popup_label = Label(text=f"\n\nName: {self.name_input.text}\nEmail: {self.email_input.text}\nCity: {self.city_dropdown.text}", size_hint=(None, None), size=(400, 150))
        content.add_widget(popup_label)

        # Add some spacing
        content.add_widget(Label(size_hint_y=None, height=20))

        close_button = Button(text="Close", size_hint=(None, None), size=(100, 50))
        close_button.bind(on_press=self.reset_entries)
        content.add_widget(close_button)

        popup = Popup(title="Submission Details", content=content, size_hint=(None, None), size=(450, 250))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def reset_entries(self, instance):
        # Reset text inputs and spinner
        self.name_input.text = ''
        self.email_input.text = ''
        self.city_dropdown.text = 'Select City'

class MyApp(App):
    def build(self):
        return MyMobileApp()

if __name__ == '__main__':
    MyApp().run()
