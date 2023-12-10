from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.app import App
from app.widgets.new_idea_button import HeartfeltHellosNewIdeaButton
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton


class ShareRateScreen(Screen):

    # Property
    previous_screen = None

    box_layout = None
    idea = None

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
        self.rating_popup = Popup(title="Rate")
        self.rating_popup_close_button = HeartfeltHellosButton(text="Close", on_press=lambda w: self.rating_popup.dismiss())
        self.rating_popup.add_widget(self.rating_popup_close_button)
        self.box_layout.add_widget(HeartfeltHellosButton(text="Rate Idea", height='40dp', on_press=lambda w: self.rating_popup.open()))
        self.box_layout.add_widget(HeartfeltHellosButton(text="View Follow-Up Ideas", size_hint_y=None, height='40dp', on_press=self.on_follow_up_pressed))
        #self.box_layout.add_widget(self.rating_popup)
        self.add_widget(self.box_layout)

    def on_share_pressed(self, arg):
        App.get_running_app().go_screen("Message_Screen", "left")
        App.get_running_app().remove_on_back_pressed_callback()

    def on_follow_up_pressed(self, arg):
        App.get_running_app().go_screen("Sub_Idea_Screen", "left")
        App.get_running_app().remove_on_back_pressed_callback()

    def on_rating_pressed(self, widget):
        pass
        #for rating_widget in self.rating_widgets:
        #    if rating_widget == widget:
        #        rating_widget.background_color = (0, 0, 1)
        #    else:
        #        rating_widget.background_color = (.678, .847, 0.902)

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
