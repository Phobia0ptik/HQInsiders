from config import readFromConfig

from queue import Queue
from shutil import get_terminal_size
from threading import Thread


class Consumer(object):
    def __init__(self):
        self.debug = readFromConfig("General", "debug_mode")
        self.show_advancing_players = readFromConfig("Solver", "show_advancing_players")
        self.show_answers = readFromConfig("Solver", "show_answers")
        self.show_answerids = readFromConfig("Solver", "show_answerids")
        self.show_category = readFromConfig("Solver", "show_category")
        self.show_eliminated_players = readFromConfig("Solver", "show_eliminated_players")
        self.show_summary = readFromConfig("Solver", "show_summary")
        self.show_players_answers = readFromConfig("Solver", "show_players_answers")
        self.show_question = readFromConfig("Solver", "show_question")
        self.show_questionid = readFromConfig("Solver", "show_questionid")
        self.show_question_count = readFromConfig("Solver", "show_question_count")
        self.show_question_number = readFromConfig("Solver", "show_question_number")

    def showQuestion(self):
        print(" Question ".center(get_terminal_size()[0], "="))
        print()

        if self.show_question_count or self.show_question_number:
            tempPrint = ""
            if self.show_question_count:
                tempPrint += "Question " + str(self.question["questionNumber"])
            if self.show_question_count and self.show_question_number:
                tempPrint += "/" + str(self.question["questionCount"])
            elif self.show_question_number:
                tempPrint += "Questions: " + str(self.question["questionCount"])

            print(tempPrint.center(get_terminal_size()[0]))

        if self.show_category:
            print(("Category: " + str(self.question["category"])).rjust(get_terminal_size()[0]))
            print()

        if self.show_question or self.show_questionid:
            tempPrint = ""
            if self.show_question:
                tempPrint += str(self.question["question"])
            if self.show_question:
                tempPrint += " (" + str(self.question["questionId"]) + ")"
            elif self.show_questionid:
                tempPrint += str(self.question["questionId"])

            print(tempPrint.center(get_terminal_size()[0]))

        if self.show_answers or self.show_answerids:
            answers = self.question["answers"]
            answersCount = len(answers)

            for answer in range(answersCount):
                tempPrint = ""

                if self.show_answers:
                    tempPrint += str(answers[answer]["text"])
                if self.show_answers and self.show_answerids:
                    tempPrint += " (" + str(answers[answer]["answerId"]) + ")"
                elif self.show_answerids:
                    tempPrint += str(answers[answer]["answerId"])

                print()
                print(tempPrint.center(get_terminal_size()[0]))

        print("".center(get_terminal_size()[0], "="))
        return True

    def showSummary(self):
        print(" Question Summary ".center(get_terminal_size()[0], "="))
        print()

        if self.show_question or self.show_questionid:
            tempPrint = ""
            if self.show_question:
                tempPrint += str(self.question["question"])
            if self.show_question and self.show_questionid:
                tempPrint += " (" + str(self.question["questionId"]) + ")"
            elif self.show_questionid:
                tempPrint += str(self.question["questionId"])
            print(tempPrint.center(get_terminal_size()[0]))
            print()

        if self.show_answers or self.show_answerids or self.show_players_answers:
            answers = self.question["answerCounts"]
            answersCount = len(answers)

            for answer in range(answersCount):
                tempPrint = ""

                answerId = str(answers[answer]["answerId"])
                answerText = str(answers[answer]["answer"])
                isCorrect = answers[answer]["correct"]
                count = str(answers[answer]["count"])

                if isCorrect:
                    tempPrint += " Correct Answer"
                else:
                    tempPrint += " Wrong Answer"

                if self.show_answers:
                    tempPrint += answerText
                if self.show_answers and self.show_answerids:
                    tempPrint += " (" + answerId + ")"
                elif self.show_answerids:
                    tempPrint += answerId

                tempPrint += "\33[0m"

                print(tempPrint.center(get_terminal_size()[0]))

                if self.show_players_answers:
                    print(("Players who marked this answer: " + count).center(get_terminal_size()[0]))
                print()

            if self.show_advancing_players:
                print(("Advancing Players: " + str(self.question["advancingPlayersCount"])).center(
                    get_terminal_size()[0]))
            if self.show_eliminated_players:
                print(("Eliminated Players: " + str(self.question["eliminatedPlayersCount"])).center(
                    get_terminal_size()[0]))

            print("".center(get_terminal_size()[0], "="))
        return True
