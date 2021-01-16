# TODO: From modules import classes
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# TODO: Create Objects from classes from above modules

question_bank = []
for q in range(len(question_data)):
    question_text = question_data[q]["text"]
    question_answer = question_data[q]["answer"]
    new_question = Question(question_text, question_answer)
    # initiating the Question class from question_model module
    # this will create question object.
    question_bank.append(new_question)
    # question_bank is the list of objects.

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"Your final score was: {quiz.score}/{quiz.question_number}")

