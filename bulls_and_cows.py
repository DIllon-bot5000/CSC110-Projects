#
#Author: Dillon Barr
#Course: CSC 110
#Description: This program takes two usernames and two codes and creates a guessing game.
#             After guess the program determines if correct letters were guessed in the correct spots
#             or in the word in the incorrect spot and gives clues helping the guesser win.
#

from os import _exit as exit

print("-" * 41)
print("-" * 7 + " WELCOME TO BULLS AND COWS " + "-" * 7)
print("-" * 41)

playerOneName = input("Player 1, enter your username: \n")
playerTwoName = input("Player 2, enter your username: \n")

playerOneCode = input(playerOneName + ", enter your code: \n")

if len(playerOneCode) != 3:
    print(playerOneName + ", that code is not valid. Exiting.")
    exit(0)
if playerOneCode.isalpha() == False:
    print(playerOneName + ", that code is not valid. Exiting.")
    exit(0)
if playerOneCode.islower() == False:
    print(playerOneName + ", that code is not valid. Exiting.")
    exit(0)
if playerOneCode[0] == playerOneCode[1] or playerOneCode[0] == playerOneCode[2]:
    print(playerOneName + ", that code is not valid. Exiting.")
    exit(0)
if playerOneCode[1] == playerOneCode[2]:
    print(playerOneName + ", that code is not valid. Exiting.")
    exit(0)

playerTwoCode = input(playerTwoName + ", enter your code: \n")

if len(playerTwoCode) != 3:
    print(playerTwoName + ", that code is not valid. Exiting.")
    exit(0)
if playerTwoCode.isalpha() == False:
    print(playerTwoName + ", that code is not valid. Exiting.")
    exit(0)
if playerTwoCode.islower() == False:
    print(playerTwoName + ", that code is not valid. Exiting.")
    exit(0)
if playerTwoCode[0] == playerTwoCode[1] or playerTwoCode[0] == playerTwoCode[2]:
    print(playerTwoName + ", that code is not valid. Exiting.")
    exit(0)
if playerTwoCode[1] == playerTwoCode[2]:
    print(playerTwoName + ", that code is not valid. Exiting.")
    exit(0)


while 0 < 1:
    playerOneGuess = input(playerOneName + ", enter guess: \n")
    if playerOneGuess == playerTwoCode:
        print(playerOneName + " wins!")
        exit(0)
    elif playerOneGuess != playerTwoCode:
        bulls = 0
        cows = 0
        i = 0
        while i < len(playerTwoCode):
            if playerOneGuess[i] == playerTwoCode[i]:
                bulls += 1
            j = 0
            while j < len(playerTwoCode):
                if playerOneGuess[i] == playerTwoCode[j]:
                    cows += 1
                j += 1
            i += 1
    if cows >= bulls:
        cows = cows - bulls
    print("  * bulls:", bulls, "\n  * cows: ", cows)
    
    playerTwoGuess = input(playerTwoName + ", enter guess: \n")
    if playerTwoGuess == playerOneCode:
        print(playerOneName + " wins!")
        exit(0)
    elif playerTwoGuess != playerOneCode:
        i = 0
        playerTwoBulls = 0
        playerTwoCows = 0
        while i < len(playerOneCode):
            if playerTwoGuess[i] == playerOneCode[i]:
                playerTwoBulls += 1
            j = 0
            while j < len(playerOneCode):
                if playerTwoGuess[i] == playerOneCode[j]:
                    playerTwoCows += 1
                j += 1
            i += 1
    if playerTwoCows >= playerTwoBulls:
        playerTwoCows = playerTwoCows - playerTwoBulls
    print("  * bulls:", playerTwoBulls, "\n  * cows: ", playerTwoCows)