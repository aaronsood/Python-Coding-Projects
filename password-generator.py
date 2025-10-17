quiz = {
    "What is the capital of Thailand?": "Bangkok", 
    "Who was the popular emperor of the Mongol Empire?": "Genghis Khan",
    "When did World War II end?": "1945"
}
restart = "yes"
while restart == "yes":
    score = 0
    for question, answer in quiz.items():
        user_answer = input(question + " ")
        if user_answer.strip().lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The answer is {answer}.")
    print(f"You got {score} out of {len(quiz)} correct!")
    restart = input("Would you like to play again? Enter yes if you want to.").lower()
    if restart != "yes":
     print("Goodbye! ")
     break