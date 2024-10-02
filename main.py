from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in range(len(question_data)):
    q = question_data[question]["question"]
    a = question_data[question]["correct_answer"]
    que = Question(q, a)
    question_bank.append(que)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was : {quiz.score}/{quiz.question_number}")
