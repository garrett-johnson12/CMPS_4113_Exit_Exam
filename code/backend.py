<<<<<<< HEAD
import json
# import random
# import os


class Question:
    def __init__(self, Question_Data):
        # print(Question_Data)
        # bool(distutils.util.strtobool(Question_Data["Visited"]))
        self.Visited = False
        self.Questions = Question_Data["Questions"]
        self.Choices = Question_Data["Choices"]
        self.Answers = Question_Data["Answers"]
        # bool(distutils.util.strtobool(Question_Data["In_Use"]))
        self.In_Use = False
        self.Explanations = Question_Data["Explanations"]
    # Checks to see if the question has already been displayed

    def is_visited(self):
        return self.Visited

    def visited(self) -> None:
        self.Visited = True

    def get_question(self, num) -> str:
        return self.Questions[num]

    def get_choices(self, num) -> str:
        # return '\n'.join(self.Choices[num])
        return self.Choices[num]

    def in_use(self) -> None:
        self.In_Use = True

    def get_answer(self, num) -> str:
        return self.Answers[num]

    def deactivate(self) -> None:
        self.In_Use = False

    def is_current(self) -> bool:
        return self.In_Use

    def get_explanation(self, num) -> str:
        return self.Explanations[num]

    def reset(self) -> None:
        self.Visited = False
        self.In_Use = False

# Represented within a dictionary
# Each concpet has a list of question classes


class Concepts:
    def __init__(self, Concept, Number_of_Questions, Question_Data):
        self.Concept = Concept
        self.Number_of_Questions = int(Number_of_Questions)
        self.Questions_info_list = []
        for q in range(self.Number_of_Questions):
            self.Questions_info_list.append(Question(Question_Data[q]))
    # This method converts a json file to a concept class and returns a class

    @classmethod
    def from_json(cls, json_string) -> 'cls':
        json_info = json.loads(json_string)
        return cls(**json_info)
    # Returns a list of question classes

    def get_question_data(self) -> list:
        return self.Questions_info_list
    # Print concepts name as class identifier

    def __repr__(self):
        return f'{self.Concept}'
    # Returns the question class that is currently in use (being displayed)

    def get_current(self) -> 'cls':
        for q in self.Questions_info_list:
            if q.is_current():
                return q
# This will display all different concepts offered


# def display_options(dict):
#     print("Please Select an Option")
#     for value in dict.values():
#         print(value)
#     print("Practice Exam")
#     print("Exit")

# Clears the console screen for visual neatness


# def clearConsole():
#     command = 'clear'
#     if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
#         command = 'cls'
#     os.system(command)

# Parse a json into python objects


def init(json_file) -> dict:
    # Create a empty list to hold concept objects
    concept = {}
    with open(json_file, 'r') as infile:
        data = json.loads(infile.read())
        for c in data:
            # Add "Concept" attribute as key with class as a value
            concept[str(c["Concept"])] = Concepts(**c)
    return concept

# This questions checks for any available questions in current session


def questions_available(c_list) -> bool:
    for q in c_list:
        if not q.is_visited():
            return True
    return False

# This will display a question


# def display_question_info(c_list, r) -> list:
#     rint = random.randint(0, len(c_list) - 1)
#     print(c_list[rint].get_question(r))
#     choices = c_list[rint].get_choices(r)
#     for c in choices:
#         print(c, '\n')
#     # print(c_list[rint].display_choices(r))
#     c_list[rint].in_use()
#     return c_list

# This question will display a question


# def redisplay_question_info(c_list, r) -> None:
#     i = 0
#     for q in c_list:
#         if q.is_current():
#             print(c_list[i].get_question(r))
#             choices = c_list[i].get_choices(r)
#             for c in choices:
#                 print(c, '\n')
#             # print(c_list[i].get_choices(r))
#         i += 1
#     return None

# This function checks the answer


def check_answer(user_choice, c_list, r) -> bool:
    for q in c_list:
        if q.is_current():
            current = q
    if current.get_answer(r) == user_choice:
        return True
    return False

# displays corresponding explanation


# def display_explanation(c_list, r) -> None:
#     for q in c_list:
#         if q.is_current():
#             print(q.get_explanation(r))
#     return

# This function the currently displayed question from the main list


def deactivate_question(c_list) -> list:
    temp = 0
    for q in c_list:
        if q.is_current():
            break
        temp += 1
    c_list[temp].deactivate()
    c_list.remove(c_list[temp])
    return c_list

# This function will combine all questions in JSON into one string


def combine_list(concept) -> list:
    temp = []
    for v in concept.values():
        temp_object_list = v.get_question_data()
        for q in temp_object_list:
            temp.append(q)
    return temp

# This will return a list of question from one concept


def combine_one_list(concept, option) -> list:
    temp = []
    #temp = concept[option].get_question_data()
    for q in concept[option].get_question_data():
        temp.append(q)
    return temp

# Returns the result of the session


def results(correct, incorrect) -> int:
    if correct == 0:
        return 0
    else:
        result = ((correct/(correct+incorrect)) * 100)
        return "{:.2f}".format(result)


def reset(Concepts) -> None:
    for v in Concepts.values():
        temp_object_list = v.get_question_data()
    for q in temp_object_list:
        q.reset()


# #TEST DRIVER CODE
# class new_test():
#   in_Session = True
#   #Concepts is a dictionary
#   #try:
#   Concepts = init("FinalJSON.json")
#   #except:
#     #print("Issue occured when parsing JSON, program will terminate")
#     #input("Enter any character to terminate program...")
#     #in_Session = False
#   while(in_Session):
#     correct = 0
#     incorrect = 0
#     valid_input = False
#     display_options(Concepts)
#     option = input()
#     while option not in Concepts and option not in ("Practice Exam", "Exit"):
#       clearConsole()
#       display_options(Concepts)
#       option = input("Option Invalid, Try Again\n\n")
#     #########################################
#     #PRACTICE EXAM SECTION
#     if option == "Practice Exam":
#       clearConsole()
#       combined_list = combine_list(Concepts)
#       while(questions_available(combined_list)):
#         r = random.randrange(2)
#         combined_list = display_question_info(combined_list, r)
#         user_choice = input("Select an Answer in the form A, B, C, D\n")
#         while user_choice not in ("A", "B", "C", "D"):
#           clearConsole()
#           redisplay_question_info(combined_list, r)
#           user_choice = input("Option Invalid, Please try again using A, B, C, D\n")
#         clearConsole()
#         if check_answer(user_choice, combined_list, r):
#           correct += 1
#         else:
#           incorrect += 1
#         combined_list = deactivate_question(combined_list)
#     ########################################
#     #EXIT SECTION
#     if option == "Exit":
#       in_Session = False
#       clearConsole()
#     elif option != "Practice Exam" and option != "Exit":
#     ########################################
#     #PRACTICE CONCEPT SECTION
#       print("Concept selected")
#       clearConsole()
#       combined_list = combine_one_list(Concepts, option)
#       while(questions_available(combined_list)):
#         r = random.randrange(2)
#         combined_list = display_question_info(combined_list, r)
#         user_choice = input("Select an Answer in the form A, B, C, D\n")
#         while user_choice not in ("A", "B", "C", "D"):
#           clearConsole()
#           redisplay_question_info(combined_list, r)
#           user_choice = input("Option Invalid, Please try again using A, B, C, D\n")
#         clearConsole()
#         if check_answer(user_choice, combined_list, r):
#           correct += 1
#         else:
#           incorrect += 1
#           display_explanation(combined_list, r)
#           input("Enter any key to go to next question...")
#         combined_list = deactivate_question(combined_list)
#     ########################################
#     reset(Concepts)
#     if option != "Exit":
#       clearConsole()
#       print("Results:", results(correct, incorrect), "%")
#       input("Enter any key to return to menu...")
#       clearConsole()
#
=======
import json
# import random
# import os


class Question:
    def __init__(self, Question_Data):
        # print(Question_Data)
        # bool(distutils.util.strtobool(Question_Data["Visited"]))
        self.Visited = False
        self.Questions = Question_Data["Questions"]
        self.Choices = Question_Data["Choices"]
        self.Answers = Question_Data["Answers"]
        # bool(distutils.util.strtobool(Question_Data["In_Use"]))
        self.In_Use = False
        self.Explanations = Question_Data["Explanations"]
    # Checks to see if the question has already been displayed

    def is_visited(self):
        return self.Visited

    def visited(self) -> None:
        self.Visited = True

    def get_question(self, num) -> str:
        return self.Questions[num]

    def get_choices(self, num) -> str:
        # return '\n'.join(self.Choices[num])
        return self.Choices[num]

    def in_use(self) -> None:
        self.In_Use = True

    def get_answer(self, num) -> str:
        return self.Answers[num]

    def deactivate(self) -> None:
        self.In_Use = False

    def is_current(self) -> bool:
        return self.In_Use

    def get_explanation(self, num) -> str:
        return self.Explanations[num]

    def reset(self) -> None:
        self.Visited = False
        self.In_Use = False

# Represented within a dictionary
# Each concpet has a list of question classes


class Concepts:
    def __init__(self, Concept, Number_of_Questions, Question_Data):
        self.Concept = Concept
        self.Number_of_Questions = int(Number_of_Questions)
        self.Questions_info_list = []
        for q in range(self.Number_of_Questions):
            self.Questions_info_list.append(Question(Question_Data[q]))
    # This method converts a json file to a concept class and returns a class

    @classmethod
    def from_json(cls, json_string) -> 'cls':
        json_info = json.loads(json_string)
        return cls(**json_info)
    # Returns a list of question classes

    def get_question_data(self) -> list:
        return self.Questions_info_list
    # Print concepts name as class identifier

    def __repr__(self):
        return f'{self.Concept}'
    # Returns the question class that is currently in use (being displayed)

    def get_current(self) -> 'cls':
        for q in self.Questions_info_list:
            if q.is_current():
                return q
# This will display all different concepts offered


# def display_options(dict):
#     print("Please Select an Option")
#     for value in dict.values():
#         print(value)
#     print("Practice Exam")
#     print("Exit")

# Clears the console screen for visual neatness


# def clearConsole():
#     command = 'clear'
#     if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
#         command = 'cls'
#     os.system(command)

# Parse a json into python objects


def init(json_file) -> dict:
    # Create a empty list to hold concept objects
    concept = {}
    with open(json_file, 'r') as infile:
        data = json.loads(infile.read())
        for c in data:
            # Add "Concept" attribute as key with class as a value
            concept[str(c["Concept"])] = Concepts(**c)
    return concept

# This questions checks for any available questions in current session


def questions_available(c_list) -> bool:
    for q in c_list:
        if not q.is_visited():
            return True
    return False

# This will display a question


# def display_question_info(c_list, r) -> list:
#     rint = random.randint(0, len(c_list) - 1)
#     print(c_list[rint].get_question(r))
#     choices = c_list[rint].get_choices(r)
#     for c in choices:
#         print(c, '\n')
#     # print(c_list[rint].display_choices(r))
#     c_list[rint].in_use()
#     return c_list

# This question will display a question


# def redisplay_question_info(c_list, r) -> None:
#     i = 0
#     for q in c_list:
#         if q.is_current():
#             print(c_list[i].get_question(r))
#             choices = c_list[i].get_choices(r)
#             for c in choices:
#                 print(c, '\n')
#             # print(c_list[i].get_choices(r))
#         i += 1
#     return None

# This function checks the answer


def check_answer(user_choice, c_list, r) -> bool:
    for q in c_list:
        if q.is_current():
            current = q
    if current.get_answer(r) == user_choice:
        return True
    return False

# displays corresponding explanation


# def display_explanation(c_list, r) -> None:
#     for q in c_list:
#         if q.is_current():
#             print(q.get_explanation(r))
#     return

# This function the currently displayed question from the main list


def deactivate_question(c_list) -> list:
    temp = 0
    for q in c_list:
        if q.is_current():
            break
        temp += 1
    c_list[temp].deactivate()
    c_list.remove(c_list[temp])
    return c_list

# This function will combine all questions in JSON into one string


def combine_list(concept) -> list:
    temp = []
    for v in concept.values():
        temp_object_list = v.get_question_data()
        for q in temp_object_list:
            temp.append(q)
    return temp

# This will return a list of question from one concept


def combine_one_list(concept, option) -> list:
    temp = []
    #temp = concept[option].get_question_data()
    for q in concept[option].get_question_data():
        temp.append(q)
    return temp

# Returns the result of the session


def results(correct, incorrect) -> int:
    if correct == 0:
        return 0
    else:
        result = ((correct/(correct+incorrect)) * 100)
        return "{:.2f}".format(result)


def reset(Concepts) -> None:
    for v in Concepts.values():
        temp_object_list = v.get_question_data()
    for q in temp_object_list:
        q.reset()


# #TEST DRIVER CODE
# class new_test():
#   in_Session = True
#   #Concepts is a dictionary
#   #try:
#   Concepts = init("FinalJSON.json")
#   #except:
#     #print("Issue occured when parsing JSON, program will terminate")
#     #input("Enter any character to terminate program...")
#     #in_Session = False
#   while(in_Session):
#     correct = 0
#     incorrect = 0
#     valid_input = False
#     display_options(Concepts)
#     option = input()
#     while option not in Concepts and option not in ("Practice Exam", "Exit"):
#       clearConsole()
#       display_options(Concepts)
#       option = input("Option Invalid, Try Again\n\n")
#     #########################################
#     #PRACTICE EXAM SECTION
#     if option == "Practice Exam":
#       clearConsole()
#       combined_list = combine_list(Concepts)
#       while(questions_available(combined_list)):
#         r = random.randrange(2)
#         combined_list = display_question_info(combined_list, r)
#         user_choice = input("Select an Answer in the form A, B, C, D\n")
#         while user_choice not in ("A", "B", "C", "D"):
#           clearConsole()
#           redisplay_question_info(combined_list, r)
#           user_choice = input("Option Invalid, Please try again using A, B, C, D\n")
#         clearConsole()
#         if check_answer(user_choice, combined_list, r):
#           correct += 1
#         else:
#           incorrect += 1
#         combined_list = deactivate_question(combined_list)
#     ########################################
#     #EXIT SECTION
#     if option == "Exit":
#       in_Session = False
#       clearConsole()
#     elif option != "Practice Exam" and option != "Exit":
#     ########################################
#     #PRACTICE CONCEPT SECTION
#       print("Concept selected")
#       clearConsole()
#       combined_list = combine_one_list(Concepts, option)
#       while(questions_available(combined_list)):
#         r = random.randrange(2)
#         combined_list = display_question_info(combined_list, r)
#         user_choice = input("Select an Answer in the form A, B, C, D\n")
#         while user_choice not in ("A", "B", "C", "D"):
#           clearConsole()
#           redisplay_question_info(combined_list, r)
#           user_choice = input("Option Invalid, Please try again using A, B, C, D\n")
#         clearConsole()
#         if check_answer(user_choice, combined_list, r):
#           correct += 1
#         else:
#           incorrect += 1
#           display_explanation(combined_list, r)
#           input("Enter any key to go to next question...")
#         combined_list = deactivate_question(combined_list)
#     ########################################
#     reset(Concepts)
#     if option != "Exit":
#       clearConsole()
#       print("Results:", results(correct, incorrect), "%")
#       input("Enter any key to return to menu...")
#       clearConsole()
#
>>>>>>> c753016bbdd1665065d4443228e234747b6f57a2
