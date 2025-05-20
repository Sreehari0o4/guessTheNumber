print("\nWelcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.\n")

import random 
number = random.randint(1,100)

level_text = '''Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
'''
print(level_text)

diff = input("Enter your choice:")

print("")

match diff:
    case '1':
        chances = 10
        print("Great! You have selected the Easy difficulty level.\n")
    case '2':
        chances = 5
        print("Great! You have selected the Medium difficulty level.\n")
    case '3':
        chances = 3
        print("Great! You have selected the Hard difficulty level.\n")
    case _:
        print("Invalid input, defaulting to easy level.\n")
        chances = 10

for i in range(chances):
    guess = int(input(f"Enter your guess : "))
    if guess == number:
        print(f"Congratulations! You guessed the number in {i+1} attempts\n")
        break
    elif guess < number:
        print(f"Incorrect! The number is greater than {guess}\n")
    else :
        print(f"Incorrect! The number is less than {guess}\n")
