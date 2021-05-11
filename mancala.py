#
# Author: Dillon Barr
# Course: CSC 110
# Description: This program was supposed to generate a playable mancala game between
#              two players switching turns.


import sys
import os 
cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, cwd)
from graphics import graphics

def mancala_banks(gui):
    '''
    This function takes the graphics module and generates the banks used to 
    keep track of the player's scores.
    '''
    gui.text(50, 65, 'Player 1', 'black', 15)
    gui.rectangle(10, 75, 75, 210, 'green')
    gui.text(655, 65, 'Player 2', 'black', 15)
    gui.rectangle(615, 75, 75, 210, 'green')
    
def mancala_pits(gui):
    '''
    This function uses the graphics module to generate the
    pits in the middle of the board used for gameplay.
    '''
    top_x_coordinate = 105
    bottom_x_coordinate = 105
    i = 0
    j = 0
    while i < 5:
        gui.rectangle(top_x_coordinate, 75, 85, 85, 'blue')
        top_x_coordinate += 100
        i += 1
    while j < 5:
        gui.rectangle(bottom_x_coordinate, 200, 85, 85, 'green')
        bottom_x_coordinate += 100
        j += 1

def print_title(gui):
    '''
    This function takes the graphics module to generate a title for the game.
    '''
    gui.text(350, 35, 'MANCALA', 'goldenrod', 25)

def print_base_scores(gui, player2_pits, player1_pits, player_1_bank, player_2_bank):
    '''
    This function updates the board after the players make their moves and reflects the new totals.
    The pit variables refer to lists containing the contents of the players pits on the board.
    The bank variables refer to the scores of the players as they play the game.
    
    '''
    top_x_coordinate = 148
    bottom_x_coordinate = 148
    i = 0
    j = 0
    for i in player2_pits:
        gui.text(top_x_coordinate, 120, i, 'black', 45)
        top_x_coordinate += 100
        i += 1
    for j in player1_pits:
        gui.text(bottom_x_coordinate, 245, j, 'black', 45)
        bottom_x_coordinate += 100
        j += 1
    gui.text(48, 180, player_1_bank, 'black', 45)
    gui.text(650, 180, player_2_bank, 'black', 45)
    
def gameplay(gui, player2_pits, player1_pits, player_1_bank, player_2_bank):
    '''
    This function alternates asking the player for their move and then refreshes the board to match. 
    The pit variables refer to lists containing the contents of the players pits on the board.
    The bank variables refer to the scores of the players as they play the game.
    '''
    while True:
        gui.clear()
        mancala_banks(gui)
        mancala_pits(gui)
        print_title(gui)
        print_base_scores(gui, player2_pits, player1_pits, player_1_bank, player_2_bank)
        gui.update_frame(60)
        
        index = int(input("Player one: Enter position to start moving chips at: \n"))
        player_1_marble_movement(player1_pits, player_1_bank,  player2_pits, index)

        
        gui.clear()
        mancala_banks(gui)
        mancala_pits(gui)
        print_title(gui)
        print_base_scores(gui, player2_pits, player1_pits, player_1_bank, player_2_bank)
        gui.update_frame(60)
        
        player_2_index = int(input("Player two: Enter position to start moving chips at: \n"))
        player_2_marble_movement(player2_pits, player_2_bank, player1_pits, player_2_index)
        win_condition(player_2_bank, 'Player Two')

def player_1_marble_movement(player1_pits, player_1_bank, player2_pits, index):
    '''
    This function takes the input from the player and increments the following spaces. If the loop carries beyond the first list 
    it continues using the negative indexes of the other player's list.
    '''
    index -= 1
    counter = 1
    inverse_index = -1
    inverse_counter = 0
    while player1_pits[index] > 0:
        player1_pits[index] -= 1
        if index + counter > 4:
            player2_pits[inverse_index - inverse_counter] += 1
            inverse_counter += 1
            if inverse_counter > 5:
                counter = 1
        else:
            player1_pits[index + counter] += 1
        counter += 1
        if counter > 5:
            counter = 0


def player_2_marble_movement(player2_pits, player_2_bank, player1_pits, index):
    '''
    This function takes the input from the player and increments the following spaces. If the loop carries beyond the first list 
    it continues using the negative indexes of the other player's list.
    '''
    index *= -1
    counter = 1
    inverse_index = 0
    inverse_counter = 0
    while player2_pits[index] > 0:
        player2_pits[index] -= 1
        if index - counter < -5:
            player1_pits[inverse_index + inverse_counter] += 1
            inverse_counter += 1
            if inverse_counter > 5:
                counter = 1
        else:
            player2_pits[index - counter] += 1
        counter += 1
        if counter > 5:
            counter = 1
        

    
def win_condition(bank, name):
    '''
    This function checks to see if the player's score matches the winning conditions and allowed the player to exit.
    '''
    if bank >= 3:
        print(name + "you win!")
        exit = input("Press any key to exit: \n")
        
    

def main():
    player_1_bank = 0
    player_2_bank = 0
    player1_pits = [3, 3, 3, 3, 3]
    player2_pits = [3, 3, 3, 3, 3]
    gui = graphics(700, 300, 'MANCALA')
    gui.clear()
    mancala_banks(gui)
    mancala_pits(gui)
    print_title(gui)
    gameplay(gui, player2_pits, player1_pits, player_1_bank, player_2_bank)

main()