# Base Kivy Template

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class StartWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(10):
            btn = Button(text="{}".format(i), size=(
                10, 10), size_hint=(.25, .25))
            self.add_widget(btn)


class guiApp(App):
    pass


guiApp().run()
