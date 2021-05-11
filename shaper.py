#
# Author: Dillon Barr
# Course: CSC 110
# Description: This program takes three inputs from a user and displays
#             one of three shapes built to their specifications.
#

def user_input_shape():
    '''
    This function gets the user's input for the shape to be displayed.
    '''
    user_shape = input("Enter shape to display: \n")
    user_shape = user_shape.lower()
    return user_shape
    
def user_input_character():    
    '''
    This function gets the user's input for the character
    used to build the parts of the shape not involving rows.
    '''
    user_character = input("Enter arrow character: \n")
    return user_character
    
def user_input_rows():    
    '''
    This function gets the user's input for the number of rows
    desired in their output.
    '''
    user_rows = input("Enter row-area height: \n")
    return user_rows

def upwards_facing_arrow(user_character):
    '''
    This function generates an arrow shape pointing up, built with the
    soecial character the user inputted.
    user_character should be a single character string.
    '''
    index = 1
    while index <= 6:
        print(' ' * (6-index) + user_character * (2*index-1))
        index += 1
    
def downwards_facing_arrow(user_character):
    '''
    This function generates an arrow shape pointing down, built with the
    soecial character the user inputted.
    user_character should be a single character string.
    '''
    index = 6
    while index >= 1:
        print(' ' * (6-index) + user_character * (2*index-1))
        index -= 1
    
def row_generator(user_rows):
    '''
    This function generates the row shape used in the shape
    chosen and replicates it as determined by the user's input.
    user_rows should be a numeric string then converted to an int.
    '''
    index = 1
    number_of_rows = int(user_rows)
    while index <= number_of_rows:
        print("|---------|")
        index += 1

def shape_print(user_shape, user_character, user_rows):
    '''
    This function compares the user_shape to the allowed shapes
    and generates one built to their specifications.
    user_shape is a case insensitive string.
    user_character is a single character string.
    user_rows is a numeric string
    '''
    print()
    if user_shape == 'hourglass':
        row_generator(user_rows)
        downwards_facing_arrow(user_character)
        upwards_facing_arrow(user_character)
        row_generator(user_rows)
    elif user_shape == 'plumbbob':
        upwards_facing_arrow(user_character)
        row_generator(user_rows)
        downwards_facing_arrow(user_character)
    elif user_shape == 'house':
        upwards_facing_arrow(user_character)
        row_generator(user_rows)
        
def main():
    '''
    This function dicates the order that the functions exectute while
    also handling the validation of the user's shape to make sure that it is supported.
    '''
    user_shape = user_input_shape()
    user_character = user_input_character()
    user_rows = user_input_rows()
    while user_shape != 'hourglass' and user_shape != 'plumbbob' and user_shape != 'house':
        print("!!! Enter a different shape !!!")
        user_shape = user_input_shape()
        user_character = user_input_character()
        user_rows = user_input_rows()
    shape_print(user_shape, user_character, user_rows)

main()

    