from app.widgets.heartfelt_hellos_button import HeartfeltHellosButton


class HeartfeltHellosStepProgressionButton(HeartfeltHellosButton):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.width = "25dp"
        self.height = "50dp"
        self.font_size = "20dp"

