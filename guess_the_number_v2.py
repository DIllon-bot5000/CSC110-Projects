from os import _exit as exit

correctAnswer = input("Enter number to be guessed between 1 and 100, inclusive: \n")

while correctAnswer.isnumeric() != True:
    print(correctAnswer, "is not an acceptable value.")
    correctAnswer = input("Enter number to be guessed between 1 and 100, inclusive: \n")
    
correctAnswer = int(correctAnswer)

while correctAnswer < 1 or correctAnswer > 100:
    print(correctAnswer, "is not 1-100, inclusive.")
    correctAnswer = input("Enter number to be guessed between 1 and 100, inclusive: \n")
    correctAnswer = int(correctAnswer)
    
counter = 1

guess = input("Enter guess 1: \n")

while guess.isnumeric == False:
    print(guess, "is not 1-100, inclusive.")
    guess = input("Enter a number to be guessed between 1 and 100, inclusive: \n")
    
guess = int(guess)

    
while guess != correctAnswer:
    print(guess, "is incorrect. Guess again.")
    counter += 1
    print("Enter guess", format(counter, 'd') + ":")
    guess = input()
    guess = int(guess)
    
if guess == correctAnswer:
    print(guess, "is correct! Ending game.")
    print("You used", counter, "guesses to get the correct solution.")
    print("The correct number was", format(correctAnswer, 'd') + ".")
    exit(0)
    