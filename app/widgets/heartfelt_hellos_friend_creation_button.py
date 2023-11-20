from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton


class HeartfeltHellosFriendCreationButton(HeartfeltHellosButton):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.width = 25
        self.height = 50
        self.font_size = 20

