import random
amount = int(input("How many characters do you want in your password? "))
letters = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","(",")","-","_","+","=","?","<",">"]
all_chars = letters + numbers + symbols
password_chars = []
for _ in range(amount):
    password_chars.append(random.choice(all_chars))
password = "".join(password_chars)
print(f"Your password is: {password}")