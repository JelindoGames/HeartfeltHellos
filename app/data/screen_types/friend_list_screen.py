from  kivy.uix.label import Label
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
        #self.friends = friends
        self.grid_layout = GridLayout(spacing='10dp', padding='10dp', cols=1, size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter("height"))
        self.scroll_view = ScrollView(do_scroll_y=True)
        self.add_widget(self.scroll_view)
        self.scroll_view.add_widget(self.grid_layout)

    def on_pre_enter(self, *args):
        self.grid_layout.clear_widgets()
        
        # add friend button rendering
        add_friend_widget = HeartfeltHellosAddFriendButton(on_press=lambda x: self.pressed_add_friend())
        self.grid_layout.add_widget(add_friend_widget)

        # divider rendering
        line = Label(text="__________________", halign="center", color=(255,255,255))
        self.grid_layout.add_widget(line)

        for friend in self.get_friends():
            friend_name_widget = HeartfeltHellosFriendButton(friend, on_press=lambda x: self.pressed_friend(x.text))
            self.grid_layout.add_widget(friend_name_widget)

    def pressed_add_friend(self):
        # pressed add friend, go to correct screen
        print("Pressed add friend")

    def pressed_friend(self,name):
        # pressed friend, go to correct screen
        print("Pressed " + name)

    def on_leave(self, *args):
        self.grid_layout.clear_widgets()

    def get_friends(self) -> list:
        #return self.friends
        return [Friend("Michael", ["Tag 1", "Tag 2", "Tag 3"])]