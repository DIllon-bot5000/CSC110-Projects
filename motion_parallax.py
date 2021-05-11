#
# Author: Dillon Barr
# Course: CSC 110
# Description: This program prints a scene and attempts to 
#              simulate motion parallax.






import sys
import os 
import random
cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, cwd)
from graphics import graphics

def print_land(graphic):
    '''
    This function prints the sky and sun in the image.
    Graphic is just the gui variable being passed to print
    an image.
    '''
    x_coordinate = (graphic.mouse_x / 150)
    y_coordinate = (graphic.mouse_y / 150)
    graphic.rectangle(x_coordinate, y_coordinate, 1000, 1000, 'light blue')
    graphic.ellipse(x_coordinate + 400, y_coordinate + 100, 100, 100, 'yellow')
    
def print_mountains(graphic, color_string1, color_string2, color_string3):
    '''
    This function prints the mountains in the image.
    Graphic is just the gui variable being passed to print
    an image.
    The color_string variables are random color strings.
    '''
    x_coordinate = (graphic.mouse_x / 100)
    y_coordinate = (graphic.mouse_y / 100)
    x_coordinate_two = (graphic.mouse_x / 38)
    y_coordinate_two = (graphic.mouse_y / 38) + 20
    graphic.triangle(x_coordinate + 300, y_coordinate + 180, 150, 500, 450, 500, color_string1)
    graphic.triangle(x_coordinate_two + 150, y_coordinate_two + 205, -100, 500, 350, 500, color_string2)
    graphic.triangle(x_coordinate_two + 480, y_coordinate_two + 205, 260, 500, 725, 500, color_string3)
    
def print_foreground(graphic):
    '''
    This function prints the grass, tree and field in the image.
    Graphic is just the gui variable being passed to print
    an image.
    '''
    i = 0
    x_coordinate = (graphic.mouse_x / 20) - 30
    y_coordinate = (graphic.mouse_y / 20) - 30
    graphic.rectangle(x_coordinate, y_coordinate + 500, 1000, 1000, 'green')
    while i < 800:
        graphic.line(x_coordinate + i, y_coordinate + 475, x_coordinate + i, y_coordinate + 500, 'green', 3)
        i += 5
    graphic.rectangle(x_coordinate + 450, y_coordinate + 480, 25, 50, 'brown')
    graphic.ellipse(x_coordinate + 463, y_coordinate + 440, 75, 115, 'dark green')
    
def print_birds(graphic, color_string1, color_string2, color_string3):
    '''
    This function draws the lines for the birds and has them loop.
    It then redraws the image after to continue the image.
    Graphic is just the gui variable being passed to print
    an image.
    The color_string variables are random color strings. 
    '''
    j = -20
    while True:
        graphic.line(j-320, 145, j-300, 155, 'black', 3)
        graphic.line(j-300, 155, j-280, 145, 'black', 3)
        graphic.line(j-240, 165, j-220, 175, 'black', 3)
        graphic.line(j-220, 175, j-200, 165, 'black', 3)
        graphic.line(j-160, 185, j-140, 195, 'black', 3)
        graphic.line(j-140, 195, j-120, 185, 'black', 3)
        graphic.line(j-80, 205, j-60, 215, 'black', 3)
        graphic.line(j-60, 215, j-40, 205, 'black', 3)
        graphic.line(j, 235, j+20, 245, 'black', 3)
        graphic.line(j+20, 245, j+40, 235, 'black', 3)
        graphic.update_frame(30)
        j += 10
        if j > 1000:
            j = -20
        graphic.clear()
        print_land(graphic)
        print_mountains(graphic, color_string1, color_string2, color_string3)
        print_foreground(graphic)

def main():
    gui = graphics(600, 600, 'motion parallax')
    color_r1 = random.randrange(0, 255)
    color_g1 = random.randrange(0, 255)
    color_b1 = random.randrange(0, 255)
    color_r2 = random.randrange(0, 255)
    color_g2 = random.randrange(0, 255)
    color_b2 = random.randrange(0, 255)
    color_r3 = random.randrange(0, 255)
    color_g3 = random.randrange(0, 255)
    color_b3 = random.randrange(0, 255)
    color_string1 = gui.get_color_string(color_r1, color_g1, color_b1)
    color_string2 = gui.get_color_string(color_r2, color_g2, color_b2)
    color_string3 = gui.get_color_string(color_r3, color_g3, color_b3)
    while True:
        gui.clear()
        print_land(gui)
        print_mountains(gui, color_string1, color_string2, color_string3)
        print_foreground(gui)
        print_birds(gui, color_string1, color_string2, color_string3)
        
    
main()