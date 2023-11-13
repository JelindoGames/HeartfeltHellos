from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        welcome_label = Label(
            text="Welcome to the App",
            font_size=24,
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )

        start_button = Button(
            text="Start",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.5, 'y': 0.1},
            on_press=self.on_start_button_click
        )

        self.add_widget(welcome_label)
        self.add_widget(start_button)

    def on_start_button_click(self, instance):
        self.manager.current = "image1"

class Image1Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        image1 = Image(source="image_1.jpg")
        self.add_widget(image1)

        next_button = Button(
            text="Next",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.90, 'y': 0.05},
            on_press=self.on_next_button_click
        )

        self.add_widget(next_button)

    def on_next_button_click(self, instance):
        self.manager.current = "image2"

class Image2Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        image2 = Image(source="image_2.jpg")
        self.add_widget(image2)

        next_button = Button(
            text="Next",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.90, 'y': 0.05},
            on_press=self.on_next_button_click
        )

        back_button = Button(
            text="Back",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.10, 'y': 0.05},
            on_press=self.on_back_button_click
        )

        self.add_widget(next_button)
        self.add_widget(back_button)

    def on_next_button_click(self, instance):
        self.manager.current = "input_screen"

    def on_back_button_click(self, instance):
        self.manager.current = "image1"

class InputScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = GridLayout(cols=2, row_force_default=True, row_default_height=60, spacing=10, padding=30)
        # Use a Label for the description

        self.weight_input = TextInput(text='Enter Weight here (lb)')
        self.height_input = TextInput(text='Enter Height here (cm)')
        submit = Button(
            text="Submit",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'y': 0.3},
            on_press=self.submit
        )
        
        layout.add_widget(self.weight_input)
        layout.add_widget(self.height_input)
        self.add_widget(submit)

        # Use a Label for the description
        more_text_label = Label(
            text='Explain how your day is going:',
            font_size=24,
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )

        # Use a TextInput for entering the description
        self.more_text_input = TextInput(
            hint_text='Type here',
            size_hint=(None, None),
            size=(600, 200),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        next_button = Button(
            text="Next",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.90, 'y': 0.05},
            on_press=self.on_next_button_click
        )
        back_button = Button(
            text="Back",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.10, 'y': 0.05},
            on_press=self.on_back_button_click
        )
        self.add_widget(back_button)
        self.add_widget(next_button)
        self.add_widget(more_text_label)
        self.add_widget(self.more_text_input)
        self.add_widget(layout)
    def on_back_button_click(self, instance):
        self.manager.current = "image2"
    def on_next_button_click(self, instance):
        self.manager.current = "exit_window"

    def submit(self, instance):
        weight = self.weight_input.text
        height = self.height_input.text
        more_text = self.more_text_input.text
    
        # Here, you can process the submitted weight and height as needed
        # For example, you can print them to the console
        print(f"Weight: {weight}, Height: {height}, More Text: {more_text}")

class ExitWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        exit_label = Label(
            text="Do you want to exit the app?",
            font_size=24,
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )

        exit_button = Button(
            text="Exit",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.90, 'y': 0.05},
            on_press=self.on_exit_button_click
        )

        back_button = Button(
            text="Back",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.10, 'y': 0.05},
            on_press=self.on_back_button_click
        )

        self.add_widget(exit_label)
        self.add_widget(exit_button)
        self.add_widget(back_button)

    def on_exit_button_click(self, instance):
        App.get_running_app().stop()

    def on_back_button_click(self, instance):
        self.manager.current = "input_screen"

class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        welcome_screen = WelcomeScreen(name="welcome")
        image1_screen = Image1Screen(name="image1")
        image2_screen = Image2Screen(name="image2")
        input_screen = InputScreen(name="input_screen")
        exit_window = ExitWindow(name="exit_window")
        screen_manager.add_widget(welcome_screen)
        screen_manager.add_widget(image1_screen)
        screen_manager.add_widget(image2_screen)
        screen_manager.add_widget(input_screen)
        screen_manager.add_widget(exit_window)
        return screen_manager

if __name__ == '__main__':
    MyApp().run()
