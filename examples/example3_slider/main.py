from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder  # Import the Builder
class SliderApp(App):
    def build(self):
        return Builder.load_file('slider.kv')  # Load the kv file

if __name__ == '__main__':
    SliderApp().run()
