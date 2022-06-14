from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
# TODO: question object w/ text and answer attributes from Question class constructor
question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))
# print(question_bank[4].text)

# TODO: bring up a question and ask user to answer
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your score was {quiz.score} / {quiz.questions_number}")

