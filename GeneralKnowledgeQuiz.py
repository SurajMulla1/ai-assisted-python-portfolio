import random

def display_prize_money(prize):
    print(f"Congratulations! You have won ${prize}.")

def generate_random_question(difficulty_level):
    questions_by_level = {
        1: ("What is the capital of France?", "d", "a. London", "b. Rome", "c. Berlin", "d. Paris"),
        2: ("What is the chemical symbol for water?", "a", "a. H2O", "b. CO2", "c. O2", "d. H2SO4"),
        3: ("Who wrote the play 'Romeo and Juliet'?", "a", "a. William Shakespeare", "b. Charles Dickens", "c. Mark Twain", "d. Jane Austen"),
        4: ("What is the currency of Japan?", "c", "a. Dollar", "b. Euro", "c. Yen", "d. Pound"),
        5: ("Which country is known as the 'Land of the Rising Sun'?", "b", "a. China", "b. Japan", "c. Thailand", "d. South Korea"),
        6: ("In which year did World War II end?", "b", "a. 1939", "b. 1945", "c. 1955", "d. 1965"),
        7: ("Which famous scientist developed the theory of relativity?", "b", "a. Isaac Newton", "b. Albert Einstein", "c. Galileo Galilei", "d. Charles Darwin"),
        8: ("Which river is the longest in the world?", "b", "a. Amazon River", "b. Nile", "c. Yangtze River", "d. Mississippi River"),
        9: ("What is the largest ocean on Earth?", "c", "a. Atlantic Ocean", "b. Indian Ocean", "c. Pacific Ocean", "d. Arctic Ocean"),
        10: ("Who painted the Mona Lisa?", "c", "a. Michelangelo", "b. Vincent van Gogh", "c. Leonardo da Vinci", "d. Pablo Picasso")
    }

    if difficulty_level <= len(questions_by_level):
        return questions_by_level[difficulty_level]
    else:
        return questions_by_level[len(questions_by_level)]

def quiz():
    prize = 0
    correct_answers = 0
    difficulty_level = 1

    random.seed()

    for question_number in range(1, 11):
        question, correct_answer, option_a, option_b, option_c, option_d = generate_random_question(difficulty_level)

        print(f"Question {question_number} (Difficulty Level {difficulty_level}):")
        print(question)
        print(option_a)
        print(option_b)
        print(option_c)
        print(option_d)

        answer = input("Enter your option (a, b, c, d): ").lower()

        if answer == correct_answer:
            correct_answers += 1
            print("Correct!\n")
            prize = 100 * 2**(correct_answers - 1)
            difficulty_level += 1
        else:
            print("Incorrect!\n")
            break

    if correct_answers > 0:
        display_prize_money(prize)
    else:
        print("You didn't win any prize. Better luck next time!")

if __name__ == "__main__":
    print("Welcome to the Quiz! You have a chance to win increasing prize money.")
    print("For each correct answer, your prize money will be doubled.")
    print("If you answer incorrectly, you will leave with $0.")
    print("Let's start!\n")

    quiz()
