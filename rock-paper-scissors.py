import random
options = ["Rock", "Paper", "Scissors"]
while True:
    option = random.choice(options)
    user_choice = input("Choose rock, paper or scissors: ").lower()
    if user_choice == "rock":
        if option.lower() == "rock":
            print(f"The computer chose {option}. Tie!")
        elif option.lower() == "paper":
            print(f"The computer chose {option}. You lose!")
        else:
            print(f"The computer chose {option}. You win!")
    elif user_choice == "scissors":
        if option.lower() == "rock":
            print(f"The computer chose {option}. You lose!")
        elif option.lower() == "paper":
            print(f"The computer chose {option}. You win!")
        else:
            print(f"The computer chose {option}. Tie!")
    elif user_choice == "paper":
        if option.lower() == "rock":
            print(f"The computer chose {option}. You win!")
        elif option.lower() == "paper":
            print(f"The computer chose {option}. Tie!")
        else:
            print(f"The computer chose {option}. You lose!")
    else:
        print("Invalid input. Please select between rock, paper or scissors.")
    answer = input("Would you like to play again? Enter yes if you do: ").lower()
    if answer != "yes":
        print("Thanks for playing!")
        break