from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from app.main import ShowcaseScreen
from app.widgets.heartfelt_hellos_add_friend_button import HeartfeltHellosAddFriendButton
from app.widgets.heartfelt_hellos_friend_button import HeartfeltHellosFriendButton
from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton


class FriendScreen(ShowcaseScreen):

    scroll_view = None
    grid_layout = None

    def __init__(self, **kwargs):
        super(FriendScreen, self).__init__(**kwargs)
        self.grid_layout = GridLayout(spacing='10dp', padding='10dp', cols=1, size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter("height"))
        self.scroll_view = ScrollView(do_scroll_y=True)
        self.add_widget(self.scroll_view)
        self.scroll_view.add_widget(self.grid_layout)

    def on_pre_enter(self, *args):
        self.grid_layout.clear_widgets()
        App.get_running_app().stored_data.previous_friend_list_screen = self.title
        
        # add friend button rendering
        add_friend_widget = HeartfeltHellosAddFriendButton(on_press=lambda x: self.pressed_add_friend())
        self.grid_layout.add_widget(add_friend_widget)

        for friend in self.get_friends():
            friend_name_widget = HeartfeltHellosFriendButton(friend, self.pressed_friend, self.pressed_edit_friend, self.pressed_remove_friend)
            self.grid_layout.add_widget(friend_name_widget)

    def pressed_add_friend(self):
        # pressed add friend, go to correct screen
        App.get_running_app().go_screen("Create_Person_Options", "left")

    def pressed_friend(self, friend):
        App.get_running_app().stored_data.temp_selected_person = friend
        App.get_running_app().go_screen(self.next_screen, "left")

    def pressed_edit_friend(self, friend):
        App.get_running_app().stored_data.temp_selected_person = friend
        App.get_running_app().go_screen("Friend_Editing_First_Step", "left")

    def pressed_remove_friend(self, friend):
        self.confirm_popup = Popup(title="Remove Friend?", size_hint_y=0.2)
        confirm_layout = BoxLayout(orientation="horizontal", spacing="10dp")
        confirm_layout.add_widget(HeartfeltHellosButton(text="No", on_press=lambda w: self.on_remove_canceled()))
        confirm_layout.add_widget(HeartfeltHellosButton(text="Yes", on_press=lambda w: self.on_remove_confirmed(friend)))
        self.confirm_popup.add_widget(confirm_layout)
        self.confirm_popup.open()

    def on_remove_canceled(self):
        self.confirm_popup.dismiss()

    def on_remove_confirmed(self, friend):
        App.get_running_app().stored_data.friends.remove(friend)
        self.confirm_popup.dismiss()
        self.on_pre_enter()

    def on_leave(self, *args):
        self.grid_layout.clear_widgets()

    def get_friends(self) -> list:
        return App.get_running_app().stored_data.friends
