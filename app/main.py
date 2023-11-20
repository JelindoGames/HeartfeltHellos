from time import time
from kivy.app import App
from os.path import dirname, join

from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.properties import (
    NumericProperty,
    StringProperty,
    BooleanProperty,
    ListProperty,
)
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.screenmanager import Screen

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
    time = NumericProperty(0)
    screen_names = ListProperty([])
    hierarchy = ListProperty([])

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
                                  'Message_Screen', 'Create_Post']
        self.screen_names = self.available_screens
        curdir = dirname(__file__)
        self.available_screens = [join(curdir, 'data', 'screens',
            '{}.kv'.format(fn).lower()) for fn in self.available_screens]
        Window.size = (350, 600)
        self.go_next_screen()

    def go_previous_screen(self):
        self.index = (self.index - 1) % len(self.available_screens)
        screen = self.load_screen(self.index)
        sm = self.root.ids.sm
        self.switch_to(screen, 'right')

    def go_next_screen(self):
        self.index = (self.index + 1) % len(self.available_screens)
        screen = self.load_screen(self.index)
        sm = self.root.ids.sm
        self.switch_to(screen, 'left')

    def go_screen(self, name, direction='left'):
        self.index = self.screen_names.index(name)
        self.switch_to(self.load_screen(self.index), direction)

    def switch_to(self, screen, direction):
        self.root.ids.sm.switch_to(screen, direction=direction)
        try:
            self.current_title = screen.display_name
        except AttributeError:
            self.current_title = screen.name

    def load_screen(self, index):
        #if index in self.screens:
        #    return self.screens[index]
        screen = Builder.load_file(self.available_screens[index], test="Test")
        self.screens[index] = screen
        return screen

    def on_back_pressed(self):
        try:
            prev_screen = self.screens[self.index].previous_screen
            self.go_screen(prev_screen, 'right')
        except AttributeError:
            return


if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ShowcaseApp().run()
