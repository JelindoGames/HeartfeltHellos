from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.app import App
from app.widgets.new_idea_button import HeartfeltHellosNewIdeaButton
from app.widgets.rate_star_button import HeartfeltHellosRateStarButton
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton


class ShareRateScreen(Screen):

    # Property
    previous_screen = None

    box_layout = None
    rating_buttons = None
    idea = None
    current_rating = None

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
        self.box_layout.add_widget(HeartfeltHellosButton(text=f"Share Idea", on_press=self.on_share_pressed))
        self.rating_popup = Popup(title="Rate", size_hint_y=0.25)
        self.rating_layout = BoxLayout(orientation="vertical", spacing="10dp")
        self.rating_buttons_layout = GridLayout(cols=5)
        self.rating_buttons = []
        for i in range(5):
            new_button = HeartfeltHellosRateStarButton(touch_callback=self.on_rating_pressed)
            self.rating_buttons.append(new_button)
            self.rating_buttons_layout.add_widget(new_button)
        self.rating_layout.add_widget(self.rating_buttons_layout)
        self.rating_popup_close_button = HeartfeltHellosButton(text="Rate", on_press=lambda w: self.rate_and_close_popup())
        self.rating_popup_close_button.background_disabled_normal = ""
        self.rating_popup_close_button.background_color = (0, 0, 0, 0)
        self.rating_popup_close_button.disabled = True
        self.rating_popup_close_button.color = (0, 0, 0, 0)
        self.rating_layout.add_widget(self.rating_popup_close_button)
        self.rating_popup.add_widget(self.rating_layout)
        self.rate_idea_button = HeartfeltHellosButton(text="Rate Idea", height='40dp', on_press=lambda w: self.open_popup())
        self.box_layout.add_widget(self.rate_idea_button)
        self.refresh_rating_display()
        self.box_layout.add_widget(Label(text=""))
        self.box_layout.add_widget(HeartfeltHellosButton(text="View Follow-Up Ideas", on_press=self.on_follow_up_pressed))
        self.add_widget(self.box_layout)

    def on_share_pressed(self, arg):
        App.get_running_app().go_screen("Message_Screen", "left")
        App.get_running_app().remove_on_back_pressed_callback()

    def on_follow_up_pressed(self, arg):
        App.get_running_app().go_screen("Sub_Idea_Screen", "left")
        App.get_running_app().remove_on_back_pressed_callback()

    def on_rating_pressed(self, widget):
        filling = True
        self.current_rating = 0
        for rating_button in self.rating_buttons:
            if filling:
                rating_button.fill()
                self.current_rating += 1
            else:
                rating_button.unfill()
            if rating_button == widget:
                filling = False
        self.rating_popup_close_button.disabled = False
        self.rating_popup_close_button.background_color = (0.5, 0.6, 0.7)
        self.rating_popup_close_button.color = (0, 0, 0)

    def share_idea(self):
        # Logic to share the idea
        pass

    def rate_idea(self, rating):
        # Logic to rate the idea
        print(f'Idea rated as: {rating}')

    def refresh_rating_display(self):
        if self.idea is None or self.idea.my_rating is None:
            self.rate_idea_button.text = "Rate Idea"
        else:
            self.rate_idea_button.text = f"Your Rating: {self.idea.my_rating}"

    def open_popup(self):
        self.rating_popup.open()

    def rate_and_close_popup(self):
        self.rating_popup.dismiss()
        self.idea.set_my_rating(self.current_rating)
        self.refresh_rating_display()

    def on_back_pressed(self):
        del App.get_running_app().stored_data.idea_screen_history[-1]
        del App.get_running_app().stored_data.idea_history[-1]
        App.get_running_app().remove_on_back_pressed_callback()
