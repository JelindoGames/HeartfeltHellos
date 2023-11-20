from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.app import App
from app.widgets.new_idea_button import HeartfeltHellosNewIdeaButton
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton


class ShareRateScreen(Screen):

    box_layout = None
    rating_layout = None

    def __init__(self, **kwargs):
        super(ShareRateScreen, self).__init__(**kwargs)
        self.box_layout = BoxLayout(orientation="vertical", padding="10dp", spacing="10dp")
        idea = App.get_running_app().stored_data.temp_selected_idea
        idea_button = HeartfeltHellosNewIdeaButton(idea)
        idea_button.do_nothing_on_touch_down()
        self.box_layout.add_widget(idea_button)
        friend = App.get_running_app().stored_data.temp_selected_person
        self.box_layout.add_widget(HeartfeltHellosButton(text=f"Share with {friend.name}", size_hint_y=None, height='50dp', on_press=self.on_share_pressed))
        self.box_layout.add_widget(Label(text="Rate this idea", font_size='30dp', color=(0, 0, 0)))
        self.rating_layout = GridLayout(cols=5, size_hint_y=None, height='40dp')
        self.box_layout.add_widget(self.rating_layout)
        for i in range(5):
            self.rating_layout.add_widget(HeartfeltHellosButton(text=str(i+1)))
        self.box_layout.add_widget(HeartfeltHellosButton(text="View Follow-Up Ideas", size_hint_y=None, height='40dp', on_press=self.on_follow_up_pressed))
        self.add_widget(self.box_layout)

    def on_share_pressed(self, arg):
        App.get_running_app().go_screen("Message_Screen", "left")

    def on_follow_up_pressed(self, arg):
        App.get_running_app().go_screen("Sub_Idea_Screen", "left")

    def share_idea(self):
        # Logic to share the idea
        pass

    def rate_idea(self, rating):
        # Logic to rate the idea
        print(f'Idea rated as: {rating}')
