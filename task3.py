import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        random.shuffle(self.questions)
        for question in self.questions:
            print(question["question"])
            if "choices" in question:
                self.display_choices(question["choices"])
                user_answer = input("Your choice: ")
                self.check_choice_answer(question, user_answer)
            elif "blank" in question:
                user_answer = input("Fill in the blank: ")
                self.check_blank_answer(question, user_answer)
            else:
                print("Invalid question format.")

        print("Quiz completed! Your score: {}/{}".format(self.score, len(self.questions)))

    def display_choices(self, choices):
        for index, choice in enumerate(choices, start=1):
            print("{}. {}".format(index, choice))

    def check_choice_answer(self, question, user_answer):
        correct_answer = question["correct"]
        if user_answer.isdigit():
            user_choice = int(user_answer)
            if user_choice == correct_answer:
                print("Correct!\n")
                self.score += 1
            else:
                print("Incorrect. The correct answer was {}\n".format(correct_answer))

    def check_blank_answer(self, question, user_answer):
        correct_answer = question["correct"].lower()
        user_answer = user_answer.lower()
        if user_answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print("Incorrect. The correct answer was {}\n".format(correct_answer))


# Sample quiz questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Madrid"],
        "correct": 1
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Mars", "Venus", "Jupiter", "Mercury"],
        "correct": 0
    },
    {
        "question": "The chemical symbol 'Hg' represents which element?",
        "choices": ["Hydrogen", "Helium", "Mercury", "Hassium"],
        "correct": 2
    },
    {
        "question": "The force that pulls objects towards the center of the Earth is called...",
        "blank": True,
        "correct": "gravity"
    },
    {
        "question": "Which is the hottest planet in our solar system?",
        "choices": ["Mars", "Mercury", "Venus", "Earth"],
        "correct": 2
    }
]

# Create and run the quiz game
game = QuizGame(quiz_questions)
game.run()
