import pathlib
import random
import backend
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.properties import BooleanProperty
from kivy.properties import StringProperty
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder
from kivy.app import App
import kivy
kivy.require('2.1.0')


# Global variables that keep track of the question, user answers, and correct answers
questionList = []
userAnswers = []
correctAnswers = []

# Class that calls the question generator file allows the application to use the data


class generateFromJSON():
    filePath = ""
    concepts = None
    listA = None

    def __init__(self) -> None:

        self.filePath = str(pathlib.Path("FinalJSON.json").parent.absolute())
        self.concepts = backend.init(self.filePath+"\FinalJSON.json")
        self.listA = backend.combine_list(self.concepts)

    def getQuestionList(self) -> list:
        return self.listA

    def getConceptList(self) -> dict:
        return self.concepts

    def getJSONFilePath(self) -> str:
        return self.filePath


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    # Pull the questions from the JSON files
    questionList = generateFromJSON()
    listB = []
    # Push them to a new list to not change the original list
    for i in questionList.getQuestionList():
        listB.append(i)
    # Create a list of 0's and 1's to access the questions
    listC = []
    for i in range(len(listB)):
        num = random.randint(0, 1)
        listC.append(num)
    # Make a counter variable
    count = 0
    # Function that turns off the selected radio button while depositing the
    # user's answers and current question

    def resetButtons(self) -> None:
        idList = ['box_1', 'box_2', 'box_3', 'box_4']
        cnt = 0
        for id in idList:
            if(self.ids[id].state == 'down'):
                if id == 'box_1':
                    userAnswers.append('A')
                elif id == 'box_2':
                    userAnswers.append('B')
                elif id == 'box_3':
                    userAnswers.append('C')
                elif id == 'box_4':
                    userAnswers.append('D')
                self.ids[id].state = 'normal'
            elif(cnt == 4):
                userAnswers.append(None)
            else:
                cnt += 1
            # print(self.ids[id].state)

    btn_state = BooleanProperty(True)
    btn_submit = False
    # Set up the initial question and Answers

    def getInitialQuestion(self):
        return self.listB[0].get_question(self.listC[0])

    def getInitAnsA(self):
        return self.listB[0].get_choices(0)[0]

    def getInitAnsB(self):
        return self.listB[0].get_choices(0)[1]

    def getInitAnsC(self):
        return self.listB[0].get_choices(0)[2]

    def getInitAnsD(self):
        return self.listB[0].get_choices(0)[3]
    # Change the questions and answers when hitting the next button

    def changeQuestion(self) -> None:
        self.btn_state = False
        if(self.count < len(self.listB)-1 and self.btn_submit == False):
            self.count += 1

            inx = 0
            idList = ['AnswerSelection_A', 'AnswerSelection_B',
                      'AnswerSelection_C', 'AnswerSelection_D']
            self.ids['question_box'].text = self.listB[self.count].get_question(
                self.listC[self.count])
            for i in idList:
                self.ids[i].text = self.listB[self.count].get_choices(self.listC[self.count])[
                    inx]
                inx += 1

        else:
            self.ids['next'].text = 'Submit'
            self.ids['next'].background_color = "#4fc3f7"
            self.ids['next'].background_normal = ''
            if self.count == len(self.listB):
                self.btn_submit = True
            else:
                self.count += 1
    # If the user presses the submit button, move them to the summary screen

    def summary(self):
        if(self.ids['next'].text == 'Submit' and self.btn_submit == True):
            self.manager.current = 'third'
        else:
            self.manager.current = 'second'


class ThirdWindow(Screen):
    # Function that will get the correct answers from the given questions
    def getCorrectQuestions() -> int:
        pass
    # Function that call the title screen

    def mainMenu(self) -> None:
        self.manager.current = 'first'


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("_screen.kv")


class screenApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Forcible set the window size of the application to 800x600
        Config.set('graphics', 'resizable', False)
        Config.set('graphics', 'width', '800')
        Config.set('graphics', 'height', '600')
        # Set the applications base background to black
        Window.clearcolor = (0, 0, 0, 0)

    def close_application(self):
        # closing application
        App.get_running_app().stop()
        # removing window
        Window.close()

    def build(self):
        return kv


if __name__ == "__main__":
    screenApp().run()
