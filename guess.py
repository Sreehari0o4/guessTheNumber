print("\nWelcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.\n")

import time

strt = True

while strt:
    import random 
    number = random.randint(1,100)
    print(number)

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

    start_time = time.time()

    for i in range(chances+1):
        if i == chances:
            print(f"Sorry! You've used all your chances you dumbass. The number was {number}.\n")
            break
        guess = int(input(f"Enter your guess : "))
        if guess == number:
            end_time = time.time()
            elapsed_time = end_time - start_time
            if i==0:
                print("Damn dude, you got it right. You are a damn good guesser.")
                print(f"Time taken: {elapsed_time:.2f} seconds\n")
            else:
                print(f"Congratulations! You got it in {i+1} attempts.")
                print(f"Time taken: {elapsed_time:.2f} seconds\n")
            break
        elif guess < number:
            print(f"Incorrect! The number is greater than {guess} ({chances-i-1} attempts left)\n")
        else :
            print(f"Incorrect! The number is less than {guess} ({chances-i-1} attempts left)\n")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        strt = False
        print("Thank you for playing! Goodbye!\n")
    else:
        print("\nStarting a new game...\n")

