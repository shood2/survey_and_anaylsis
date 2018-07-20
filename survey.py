import json

class survey_answer:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

class survey_question:
    def __init__(self, question, hasAnswers, answers, answerType):
        self.question = question
        self.hasAnswers = hasAnswers
        if(self.hasAnswers):
            self.answers = answers
        else:
            self.answers = ""
        self.answerType = answerType
        self.reply = ""

    def display(self):
        print(self.question)
        if(self.hasAnswers):
            for x in range(0, len(self.answers)):
                print(str(int(x) + 1) + ": " + self.answers[x] + "\n")

    def verify_answer(self, input):
        if(self.hasAnswers):
            if(not(input.isdigit())):
                return False
            else:
                if(int(input) < 1 or int(input) > len(self.answers) + 1):
                    return False
                else:
                    return True
        else:
            if(self.answerType == "string"):
                if(input.isdigit()):
                    return False
                else:
                    return True
            elif(self.answerType == "int"):
                if(input.isdigit()):
                    return True
                else:
                    return False
            elif(self.answerType == "bool"):
                if(input.lower() == "true" or input.lower() == "false" or input.lower() == "t" or input.lower() == "f" or input.lower() == "1" or input.lower() == "0"):
                    return True
                else:
                    return False
            else:
                return False

    def ask_question(self):
        self.display()
        inp = input("Answer: ")
        while(self.verify_answer(inp) != True):
            self.display()
            inp = input("Answer: ")
        self.reply = inp
        return inp

def load_survey():
    file = open("question.json", "r")
    list_of_questions_json = json.load(file)
    file.close()
    list_of_questions = []

    for questions in list_of_questions_json:
        list_of_questions.append(survey_question(questions["question"], questions["hasAnswers"], questions["answers"], questions["answerType"]))

    return list_of_questions

def survey(end):
    survey_answers = []
    question_count = 0
    list_of_questions = load_survey()
    for question in list_of_questions:
        question.ask_question()

    survey_answers.append(survey_answer(list_of_questions[1].reply, list_of_questions[2].reply, list_of_questions[3].reply))

    file = open("dump.json", "a")
    file.write("\t")
    json.dump(vars(survey_answers[0]), file)
    if(end == False):
        file.write(", \n")
    file.close()

def conduct_survey():
    file = open("dump.json", "w")
    file.write("[ \n")
    file.close()
    survey(False)
    survey(False)
    survey(True)
    file = open("dump.json", "a")
    file.write("\n ]")
    file.close()
