from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock

class WishApp(App):
    def build(self):
        self.wish_text = TextInput(hint_text='Enter your wish here', size_hint=(1, 0.2))
        self.progress_bar = ProgressBar(max=100, size_hint=(1, 0.2))
        self.message_label = Label(size_hint=(1, 0.2))

        submit_button = Button(text='Next', on_press=self.start_loading, size_hint=(1, 0.2))
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.wish_text)
        self.layout.add_widget(submit_button)
        self.layout.add_widget(self.progress_bar)
        self.layout.add_widget(self.message_label)

        return self.layout

    def start_loading(self, instance):
        self.progress_bar.value = 0
        self.message_label.text = ""
        self.wish = self.wish_text.text
        Clock.schedule_interval(self.update_progress, 0.1)

    def update_progress(self, dt):
        if self.progress_bar.value < 100:
            self.progress_bar.value += 1
        else:
            Clock.unschedule(self.update_progress)
            self.message_label.text = f"Fuck you and your wish: {self.wish}"

if __name__ == '__main__':
    WishApp().run()
