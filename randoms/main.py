from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for ques in question_data:
    new_ques = Question(ques["text"],ques["answer"])
    question_bank.append(new_ques)
#print(question_bank[0].text)
quiz = QuizBrain(question_bank)
while quiz.continue_to_show_ques():
    #quiz.next_question()
    quiz.check_answer()
    
