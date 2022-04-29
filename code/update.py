<<<<<<< HEAD
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class MyLayout(BoxLayout):
    def press(self) -> None:
        self.ids.labelA.text = "Hello"


# Builder.load_file("_label.kv")


class updateApp(App):
    pass


updateApp().run()
=======
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class MyLayout(BoxLayout):
    def press(self) -> None:
        self.ids.labelA.text = "Hello"


# Builder.load_file("_label.kv")


class updateApp(App):
    pass


updateApp().run()
>>>>>>> c753016bbdd1665065d4443228e234747b6f57a2
