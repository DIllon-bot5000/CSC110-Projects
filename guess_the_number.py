from os import _exit as exit

correctAnswer = input("Enter number to be guessed between 1 and 100, inclusive: \n")

if correctAnswer.isnumeric() != True:
    print(correctAnswer, "is not an acceptable value.")
    exit(0)
    
correctAnswer = int(correctAnswer)
if correctAnswer < 1 or correctAnswer > 100:
    print(correctAnswer, "is not 1-100, inclusive.")
    exit(0)
    
guess1 = input("First guess: \n")

if guess1.isnumeric() != True:
    print(guess1, "is not an acceptable value.")
    exit(0)
    
guess1 = int(guess1)
if guess1 < 1 or guess1 > 100:
    print(guess1, "is not 0-100, inclusive.")
    exit(0)
    
if guess1 == correctAnswer:
    print(guess1, "is correct! Ending game.")
    exit(0)
if guess1 != correctAnswer:
    print(guess1, "is incorrect.")
    
guess2 = input("Second guess: \n")

if guess2.isnumeric() != True:
    print(guess2, "is not an acceptable value.")
    exit(0)
    
guess2 = int(guess2)
if guess2 < 1 or guess2 > 100:
    print(guess2, "is not 1-100, inclusive.")
    exit(0)

if guess2 == correctAnswer:
    print(guess2, "is correct! Ending game.")
    exit(0)
if guess2 != correctAnswer:
    print(guess2, "is incorrect.")
    print("You did not guess the number within 2 attempts.")
    print("The target number was", correctAnswer)
    print("Your guesses were", guess1, "and",guess2)
    