from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from app.main import ShowcaseScreen
from app.widgets.heartfelt_hellos_add_friend_button import HeartfeltHellosAddFriendButton
from app.widgets.heartfelt_hellos_friend_button import HeartfeltHellosFriendButton
from app.data.data_types.friend import Friend


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
        add_friend_widget = HeartfeltHellosAddFriendButton(on_press=lambda x: print("Pressed add friend"))
        self.grid_layout.add_widget(add_friend_widget)
        for friend in self.get_friends():
            friend_name_widget = HeartfeltHellosFriendButton(friend, on_press=lambda x: print("Pressed " + friend.name))
            self.grid_layout.add_widget(friend_name_widget)

    def on_leave(self, *args):
        self.grid_layout.clear_widgets()

    def get_friends(self) -> list:
        return [Friend("Michael", ["Tag 1", "Tag 2", "Tag 3"])]
