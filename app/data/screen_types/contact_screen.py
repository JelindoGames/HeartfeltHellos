from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.app import App
from kivy.utils import get_color_from_hex
from app.main import ShowcaseScreen
from app.widgets.heartfelt_hellos_step_progression_button import HeartfeltHellosStepProgressionButton

class ContactList(ShowcaseScreen):
    scroll_view = None
    grid_layout = None
    search_input = None

    def __init__(self, **kwargs):
        super(ContactList, self).__init__(**kwargs)
        
        # Initialize GridLayout for contacts
        self.grid_layout = GridLayout(cols=1, spacing="2dp", size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))
        
        # Initialize the search bar at the top
        self.search_input = TextInput(hint_text='Search', size_hint_y=None, height="48dp", multiline=False)
        self.grid_layout.add_widget(self.search_input)
        
        # Initialize ScrollView
        self.scroll_view = ScrollView(do_scroll_y=True) # (size_hint=(1, None), size=(Window.width, Window.height))
        self.scroll_view.add_widget(self.grid_layout)
        
        # Add the ScrollView to the screen
        self.add_widget(self.scroll_view)

        # Populate the grid with contact sections
        self.populate_contacts()

    def populate_contacts(self):
        # Helper function to add sections for contacts
        def add_contacts_section(letter, names):
            # Add a letter label to the left and a line divider
            lbl = Label(
                text=letter, 
                size_hint_y=None, 
                height="30dp", 
                halign='left',
                color=(255,255,255))
            lbl.bind(size=lbl.setter('text_size'))  # To align text to the left
            self.grid_layout.add_widget(lbl)
            self.grid_layout.add_widget(Widget(size_hint_y=None, height="1dp"))

            # Add buttons for each name
            for name in names:
                self.grid_layout.add_widget(Button(text=name, size_hint_y=None, height="50dp"))

        # Call the helper function for each contact section
        add_contacts_section('  A', ['Name 1', 'Name 2'])
        add_contacts_section('  B', ['Name 3'])
        add_contacts_section('  J', ['Name 4'])
        add_contacts_section('  M', ['Name 5', 'Name 6'])

    def on_pre_enter(self, *args):
        # Clear the grid and re-populate it when the screen is about to be shown
        self.grid_layout.clear_widgets()
        self.populate_contacts()
