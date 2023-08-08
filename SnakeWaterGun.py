import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (Snake/Water/Gun): ").strip().lower()
        if user_choice in ["snake", "water", "gun"]:
            return user_choice
        else:
            print("Invalid choice. Please choose between Snake, Water, or Gun.")

def get_computer_choice():
    choices = ["snake", "water", "gun"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "snake":
        return "You win!" if computer_choice == "water" else "Computer wins!"
    elif user_choice == "water":
        return "You win!" if computer_choice == "gun" else "Computer wins!"
    elif user_choice == "gun":
        return "You win!" if computer_choice == "snake" else "Computer wins!"

def play_game():
    print("Welcome to Snake - Water - Gun game!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

    print("Thank you for playing!")

if __name__ == "__main__":
    play_game()
