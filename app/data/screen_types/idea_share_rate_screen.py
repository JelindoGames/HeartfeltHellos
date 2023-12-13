import copy

import app.constants as constants
from app.data.data_types.idea import Idea
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from app.widgets.new_idea_button import HeartfeltHellosNewIdeaButton
from app.widgets.rate_star_button import HeartfeltHellosRateStarButton
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton
from app.data.data_types.friend import Friend


class ShareRateScreen(Screen):

    # Property
    previous_screen = None

    box_layout = None
    rating_buttons = None
    idea = None
    current_rating = None

    def __init__(self, **kwargs):
        super(ShareRateScreen, self).__init__(**kwargs)
        # Setup
        App.get_running_app().set_on_back_pressed_callback(self.on_back_pressed)
        self.idea = App.get_running_app().stored_data.idea_history[-1]
        App.get_running_app().stored_data.viewed_ideas.add(self.idea)
        self.previous_screen = App.get_running_app().stored_data.idea_screen_history[-1]
        self.clear_widgets()
        self.box_layout = BoxLayout(orientation="vertical", padding="10dp", spacing="10dp")
        self.idea_button = HeartfeltHellosNewIdeaButton(self.idea, None)
        self.idea_button.do_nothing_on_touch_down()
        self.box_layout.add_widget(self.idea_button)
        self.box_layout.add_widget(HeartfeltHellosButton(text=f"Share Idea", on_press=self.on_share_pressed))
        # Rating Button / Popup
        self.rating_popup = Popup(title="Rate", size_hint_y=0.25)
        self.rating_layout = BoxLayout(orientation="vertical", spacing="10dp")
        self.rating_buttons_layout = GridLayout(cols=5)
        self.rating_buttons = []
        for i in range(5):
            new_button = HeartfeltHellosRateStarButton(touch_callback=self.on_rating_pressed)
            self.rating_buttons.append(new_button)
            self.rating_buttons_layout.add_widget(new_button)
        self.rating_layout.add_widget(self.rating_buttons_layout)
        self.rating_popup_close_button = HeartfeltHellosButton(text="Rate", on_press=lambda w: self.rate_and_close_rating_popup())
        self.rating_popup_close_button.background_disabled_normal = ""
        self.rating_popup_close_button.background_color = (0, 0, 0, 0)
        self.rating_popup_close_button.disabled = True
        self.rating_popup_close_button.color = (0, 0, 0, 0)
        self.rating_layout.add_widget(self.rating_popup_close_button)
        self.rating_popup.add_widget(self.rating_layout)
        self.rate_idea_button = HeartfeltHellosButton(text="Rate Idea", height='40dp', on_press=lambda w: self.open_rating_popup())
        self.box_layout.add_widget(self.rate_idea_button)
        self.refresh_rating_display()
        # Final Setup
        self.box_layout.add_widget(Label(text=""))  # Filler space
        self.box_layout.add_widget(HeartfeltHellosButton(text="View Follow-Up Ideas", on_press=self.on_follow_up_pressed))
        self.add_widget(self.box_layout)

    def on_share_pressed(self, arg):
        if App.get_running_app().stored_data.temp_selected_person is not None:
            App.get_running_app().stored_data.message_recipient = App.get_running_app().stored_data.temp_selected_person
            App.get_running_app().go_screen("Message_Screen", "left")
        else:
            share_selection_layout = BoxLayout(orientation="vertical", spacing="10dp", padding="10dp", size_hint_y=None)
            share_selection_layout.bind(minimum_height=share_selection_layout.setter('height'))
            share_selection_scroll = ScrollView(do_scroll_y=True)
            share_selection_popup = Popup(title="Share with...", size_hint_y=0.6)
            if len(App.get_running_app().stored_data.friends) > 0:
                share_selection_layout.add_widget(Label(text="HeartfeltHellos Friends"))
            for friend in App.get_running_app().stored_data.friends:
                button = HeartfeltHellosButton(text=friend.name, size_hint_y=None, height="40dp", on_press=lambda w: self.on_recipient_selected_from_friend(w, share_selection_popup))
                button.background_color = (0.1, 1, 0.4)
                share_selection_layout.add_widget(button)
            if len(App.get_running_app().stored_data.friends) > 0:
                share_selection_layout.add_widget(Label(text="Contacts"))
            for letter, name_list in constants.contacts:
                for name in name_list:
                    button = HeartfeltHellosButton(text=name, size_hint_y=None, height="40dp", on_press=lambda w: self.on_recipient_selected_from_contact(w, share_selection_popup))
                    share_selection_layout.add_widget(button)
            share_selection_scroll.add_widget(share_selection_layout)
            share_selection_popup.add_widget(share_selection_scroll)
            share_selection_popup.open()

    def on_recipient_selected_from_contact(self, widget, popup):
        popup.dismiss()
        App.get_running_app().stored_data.message_recipient = Friend(widget.text, [])
        App.get_running_app().go_screen("Message_Screen", "left")

    def on_recipient_selected_from_friend(self, widget, popup):
        popup.dismiss()
        for friend in App.get_running_app().stored_data.friends:
            if friend.name == widget.text:
                App.get_running_app().stored_data.message_recipient = friend
                App.get_running_app().go_screen("Message_Screen", "left")
                return

    def on_follow_up_pressed(self, arg):
        App.get_running_app().remove_on_back_pressed_callback()
        App.get_running_app().go_screen("Sub_Idea_Screen", "left")

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

    def refresh_rating_display(self):
        if self.idea is None or self.idea.my_rating is None:
            self.rate_idea_button.text = "Rate Idea"
        else:
            self.rate_idea_button.text = f"Your Rating: {self.idea.my_rating}"


    def open_rating_popup(self):
        self.rating_popup.open()

    def rate_and_close_rating_popup(self):
        self.rating_popup.dismiss()
        self.idea.set_my_rating(self.current_rating)
        self.refresh_rating_display()
        self.idea_button.update_rating()

    def on_back_pressed(self):
        if len(App.get_running_app().stored_data.idea_screen_history) > 0:
            del App.get_running_app().stored_data.idea_screen_history[-1]
        if len(App.get_running_app().stored_data.idea_history) > 0:
            del App.get_running_app().stored_data.idea_history[-1]
