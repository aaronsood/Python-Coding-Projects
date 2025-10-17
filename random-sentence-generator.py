import random
people = ["Jake", "Lily", "Brian"]
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
fruit = random.choice(fruits)
person = random.choice(people)
number = random.choice(numbers)
print(f"{person} ate {number} {fruit}s.")
