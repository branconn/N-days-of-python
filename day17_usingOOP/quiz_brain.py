
# TODO: ask question
# TODO: check answer
# TODO: check if end of quiz

class QuizBrain:
    def __init__(self, q_list):
        self.questions_number = 0
        self.questions_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.questions_number]
        user_answer = input(f"Q.{self.questions_number}: {current_question.text} (true/false)\n").lower()
        self.questions_number += 1
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.questions_number != len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score} / {self.questions_number}\n")


