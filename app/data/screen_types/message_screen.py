from kivy.uix.screenmanager import Screen

class MessageScreen(Screen):
    def send_message(self):
        # Logic to send the message
        message = self.ids.message_input.text
        print(f'Message sent: {message}')
