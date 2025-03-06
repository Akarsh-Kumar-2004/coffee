class QuizBrain:

    
    def __init__(self,q_list):
        self.question_list = q_list
        self.question_number = 0
        self.ques_number2 = 0
    def continue_to_show_ques(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    # def next_question(self):
    #     current_question = self.question_list[self.question_number]
    #     self.question_number+=1
        #input(f"Q.{self.question_number} :{current_question.text} (T/F)")
    
    def check_answer(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_input = input(f"Q.{self.question_number} :{current_question.text} (T/F) :")
        #print(current_question.answer)
        score = 0
        if current_question.answer.lower() == user_input.lower():
            # print("yes")
            score+=1
            print(score)


        
        