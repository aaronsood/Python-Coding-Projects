print("Welcome to Mad Libs, a game where you can make funny stories from words!")
restart = "yes"
while restart == "yes":
 noun = input("Enter a noun: ")
 adj = input("Enter an adjective: ")
 verb = input("Enter a verb: ")
 place = input("Enter a place: ")
 print (f"One day, a {adj} {noun} decided to {verb} at {place}. Everyone was amazed!")
 restart = input("Would you like to make a new story? Enter yes if you do.").lower()
 if restart != "yes":
  print("Goodbye!")
  break