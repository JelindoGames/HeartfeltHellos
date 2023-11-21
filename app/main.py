from kivy.app import App
from os.path import dirname, join

from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.properties import (
    NumericProperty,
    StringProperty,
    ListProperty,
    BooleanProperty
)
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from stored_data import StoredData

import sys
import os


class ShowcaseScreen(Screen):
    def add_widget(self, *args, **kwargs):
        if 'content' in self.ids:
            return self.ids.content.add_widget(*args, **kwargs)
        return super(ShowcaseScreen, self).add_widget(*args, **kwargs)


class ShowcaseApp(App):

    index = NumericProperty(-1)
    current_title = StringProperty()
    have_back_button = BooleanProperty(False)
    have_home_button = BooleanProperty(False)
    screen_names = ListProperty([])
    stored_data = StoredData()
    current_screen = None
    on_back_pressed_callback = None

    def add_custom_fonts(self):
        font_file = join(dirname(__file__), "assets", "Raleway-Regular.ttf")
        LabelBase.register(name='Raleway', fn_regular=font_file)

    def build(self):
        self.add_custom_fonts()
        self.title = 'Heartfelt Hellos'
        self.screens = {}
        self.available_screens = ['Title_Screen', 'General_Idea_Screen', 'Sub_Idea_Screen', 'User_Idea_Screen',
                                  'Create_Person_Options', 'Friend_List', 'Friend_Creation_First_Step',
                                  'Friend_Creation_Second_Step', 'Idea_Share_Rate_Screen', 'Contact_List',
                                  'Message_Screen', 'Idea_Creation_First_Step', 'Idea_Creation_Second_Step', 
                                  'Michael_Screen', 'Friend_List_For_General_Ideas']
        self.screen_names = self.available_screens
        curdir = dirname(__file__)
        self.available_screens = [join(curdir, 'data', 'screens',
            '{}.kv'.format(fn).lower()) for fn in self.available_screens]
        Window.size = (dp(300), dp(500))
        self.go_next_screen()

    def go_previous_screen(self):
        self.index = (self.index - 1) % len(self.available_screens)
        screen = self.load_screen(self.index)
        self.switch_to(screen, 'right')

    def go_next_screen(self):
        self.index = (self.index + 1) % len(self.available_screens)
        screen = self.load_screen(self.index)
        self.switch_to(screen, 'left')

    def go_screen(self, name, direction='left'):
        self.index = self.screen_names.index(name)
        self.switch_to(self.load_screen(self.index), direction)

    def switch_to(self, screen, direction):
        self.current_screen = screen
        self.update_back_button_status()
        self.update_home_button_status()
        self.root.ids.sm.switch_to(screen, direction=direction)
        try:
            self.current_title = screen.display_name
        except AttributeError:
            self.current_title = screen.name

    def load_screen(self, index):
        screen = Builder.load_file(self.available_screens[index], test="Test")
        self.screens[index] = screen
        return screen

    def on_back_pressed(self):
        try:
            prev_screen = self.screens[self.index].previous_screen
            if prev_screen == "":
                return
            if self.on_back_pressed_callback is not None:
                self.on_back_pressed_callback()
            self.go_screen(prev_screen, 'right')
        except AttributeError:
            return

    def update_back_button_status(self):
        try:
            prev_screen = self.screens[self.index].previous_screen
            if prev_screen == "":
                self.have_back_button = False
            self.have_back_button = True
        except AttributeError:
            self.have_back_button = False

    def update_home_button_status(self):
        self.have_home_button = self.current_screen.name != self.screen_names[0]

    def set_on_back_pressed_callback(self, cb):
        self.on_back_pressed_callback = cb

    def remove_on_back_pressed_callback(self):
        self.on_back_pressed_callback = None


if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ShowcaseApp().run()
