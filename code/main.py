# Import backend file
import backend
import pathlib
# Imports the various modules
from kivy.config import Config
from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import kivy
kivy.require('2.1.0')


# Forcible set the window size of the application to 800x600
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
# Set the applications base background to black
Window.clearcolor = (0, 0, 0, 0)
# Class that manages the Screens for the application


class firstWindow(Screen):
    pass


class secondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass
# Class that calls the question generator file allows the application to use the data


class generateFromJSON():
    filePath = ""
    concepts = {}

    def __init__(self) -> None:

        self.filePath = str(pathlib.Path("FinalJSON.json").parent.absolute())
        self.concepts = backend.init(self.filePath+"\FinalJSON.json")

    def getConceptList(self) -> dict:
        return self.concepts

    def getJSONFilePath(self) -> str:
        return self.filePath

# Class that generates the Title Window


# class titleWindow(BoxLayout):
#     pass
# Class that generates the Exam Window


# class examWindow(BoxLayout, GridLayout, generateFromJSON):
#     fileObj = None

#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.fileObj = generateFromJSON()
#         # print(self.fileObj.getConceptList())
#         # print(self.fileObj.getJSONFilePath())

#     def selection(self, instance, value):
#         pass

# Class that contains the appdata itself
# kv = Builder.load_file("main.kv")


class mainApp(App):
    pass


# Driver Code for the app
if __name__ == "__main__":
    mainApp().run()
