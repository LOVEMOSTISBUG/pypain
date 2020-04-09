class question():
    """分类问题及其答案"""
    def __init__(self,question):
        self.question = question
        self.answer = []

    def show_question(self):
        """显示问题"""
        print(self.question)

    def save_answer(self,new_answer):
        """储存新答案"""
        self.answer.append(new_answer)

    def get_answer(self):
        """显示所有答案"""
        return self.answer

if __name__ == '__main__':
    pass

