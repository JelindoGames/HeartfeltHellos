from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.app import App
from app.widgets.new_idea_button import HeartfeltHellosNewIdeaButton
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton


class ShareRateScreen(Screen):

    # Property
    previous_screen = None

    box_layout = None
    rating_layout = None
    idea = None
    rating_widgets = []

    def __init__(self, **kwargs):
        super(ShareRateScreen, self).__init__(**kwargs)
        App.get_running_app().set_on_back_pressed_callback(self.on_back_pressed)
        self.idea = App.get_running_app().stored_data.idea_history[-1]
        self.previous_screen = App.get_running_app().stored_data.idea_screen_history[-1]
        self.clear_widgets()
        self.box_layout = BoxLayout(orientation="vertical", padding="10dp", spacing="10dp")
        idea_button = HeartfeltHellosNewIdeaButton(self.idea, None)
        idea_button.do_nothing_on_touch_down()
        self.box_layout.add_widget(idea_button)
        friend = App.get_running_app().stored_data.temp_selected_person
        self.box_layout.add_widget(HeartfeltHellosButton(text=f"Share with {friend.name}", size_hint_y=None, height='50dp', on_press=self.on_share_pressed))
        self.box_layout.add_widget(Label(text="Rate this idea", font_size='30dp', color=(0, 0, 0)))
        self.rating_layout = GridLayout(cols=5, size_hint_y=None, height='40dp')
        self.box_layout.add_widget(self.rating_layout)
        for i in range(5):
            rating_widget = HeartfeltHellosButton(text=str(i+1), on_press=self.on_rating_pressed, background_normal="")
            self.rating_widgets.append(rating_widget)
            self.rating_layout.add_widget(rating_widget)
        self.box_layout.add_widget(HeartfeltHellosButton(text="View Follow-Up Ideas", size_hint_y=None, height='40dp', on_press=self.on_follow_up_pressed))
        self.add_widget(self.box_layout)

    def on_share_pressed(self, arg):
        App.get_running_app().go_screen("Message_Screen", "left")
        App.get_running_app().remove_on_back_pressed_callback()

    def on_follow_up_pressed(self, arg):
        App.get_running_app().go_screen("Sub_Idea_Screen", "left")
        App.get_running_app().remove_on_back_pressed_callback()

    def on_rating_pressed(self, widget):
        for rating_widget in self.rating_widgets:
            if rating_widget == widget:
                rating_widget.background_color = (0, 0, 1)
            else:
                rating_widget.background_color = (0.3, 0.3, 0.3)

    def share_idea(self):
        # Logic to share the idea
        pass

    def rate_idea(self, rating):
        # Logic to rate the idea
        print(f'Idea rated as: {rating}')

    def on_back_pressed(self):
        del App.get_running_app().stored_data.idea_screen_history[-1]
        del App.get_running_app().stored_data.idea_history[-1]
        App.get_running_app().remove_on_back_pressed_callback()
