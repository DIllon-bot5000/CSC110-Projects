###
### Author: Dillon Barr
### Course: CSC 110
### Description: This program displays a cricle, triange, and square all
###              moving equally across the screen before wrapping around infinitely.
###

import sys
import os 
import random
cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, cwd)
from graphics import graphics

def main():
    '''
    This function displays a 600x600 canvas and
    fills it with a circle, triangle and square.
    They then move uniformily across the screen horizontally
    and after wrapping across the screen have new positions on the y axis.
    '''
    gui = graphics(600, 600, 'three')
    x = 300
    y1 = random.randrange(0, 600)
    y2 = random.randrange(0, 600)
    y3 = random.randrange(0, 600)
    while True:
        gui.clear()
        gui.rectangle(x - 25, y1, 50, 50, 'red')
        gui.ellipse(x, y2, 50, 50, 'blue')
        gui.triangle(x, y3, x - 25, y3 + 50, x + 25, y3 +50, 'green') 
        gui.update_frame(30)
        x += 10
        if x > 600:
            x = -50
            y1 = random.randrange(25, 575)
            y2 = random.randrange(25, 575)
            y3 = random.randrange(25, 575)
    
main()