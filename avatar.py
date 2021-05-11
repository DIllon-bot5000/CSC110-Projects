def print_adam():
    '''
    This function prints the premade avatar Adam
    '''
    print()
    print_hat('right')
    print_face('False', '*')
    print("      |-X-|")
    print_arms('T')
    print_torso(3)
    print_legs(3, '<|||>')

def print_chris():
    '''
    This function generates the premade avatar Chris.
    '''
    print()
    print_hat('else')
    print_face('True', 'U')
    print("      |-X-|")
    print_arms('W')
    print_torso(1)
    print_legs(4, '<>-<>')
    
def print_jeff():
    '''
    This function generates the premade avatar Jeff.
    '''
    print()
    print_hat('both')
    print_face('True', '0')
    print_arms('=')
    print_torso(2)
    print_legs(2, '#HHH#')

def print_custom(hat_style, eye_character, hair_style, arm_style, torso_length, leg_length, shoe_style):
    '''
    This function generate a custom, user designed avatar to their specifications.
    hat_style is a string saying left, right, both, or front.
    eye_character is a single character to use for the avatar's eyes.
    hair_style is either a True or False statement.
    arm_style is a single character used to create the arms.
    torso_length is an integer used specify the torso's length.
    leg_length is an integer 1-4 used to specify the leg length.
    shoe_style is a 5 character string used to print out the avatar's shoes.
    '''
    print_hat(hat_style)
    print_face(hair_style, eye_character)
    print_arms(arm_style)
    print_torso(torso_length)
    print_legs(leg_length, shoe_style)
    
def print_hat(style):
    '''
    This function prints out a hat matching the user's input.
    style is a string matching either front, right, both or defaults to front.
    '''
    if style == 'left':
        print("       ~-~       ")
        print("     /-~-~-\\     ")
        print(" ___/_______\\    ")
    elif style == 'right':
        print("       ~-~       ")
        print("     /-~-~-\\     ")
        print("    /_______\\___    ")
    elif style == 'both':
        print("       ~-~       ")
        print("     /-~-~-\\     ")
        print(" ___/_______\\___    ")
    else:
        print("       ~-~       ")
        print("     /-~-~-\\     ")
        print("    /_______\\    ")

def print_face(boolean, eyes):
    '''
    This function prints the avatar's face to the user's specifications.
    boolean is a True or False statement to determine hair thickness.
    eyes is a single character used for the avatar's eyes.
    '''
    if boolean == 'True':
        print('    |"""""""|    ')
    else:
        print("    |'''''''|    ")
    print("    | " + eyes + "   " + eyes + " |    ")
    print("    |   V   |    ")
    print("    |  ~~~  |    ")
    print("     \\_____/     ")

def print_arms(arms):
    '''
    This function prints the avatar's arms to the user's input.
    arms is a single character used to build the avatar's arms.
    '''
    index = 4
    print(" 0", end='')
    while index > 0:
        print(arms, end='')
        index -= 1
    print("|---|", end='')
    counter = 4
    while counter > 0:
        print(arms, end='')
        counter -= 1
    print("0")
    
    
def print_torso(torso):
    '''
    This function prints the avatar's torso to the user's input.
    torso is a single integer used to determine the avatar's torso height.
    '''
    index = 0
    while index < torso:
        print("      |-X-|")
        index += 1
    print("      HHHHH")
    
def print_legs(legs, shoes):
    '''
    This function prints the avatar's legs and shoes to the user's input.
    legs is a single integer 1-4 to build the avatar's leg height.
    shoes is a 5 character string used to print the shoe style.
    '''
    outer_spaces="     "
    inner_spaces=" "
    index = 0
    while index < legs:
        if index == 0:
            outer_spaces = "     "
        if index == 1:
            outer_spaces = "    "
        if index == 2:
            outer_spaces = "   "
        if index == 3:
            outer_spaces = "  "
        print(outer_spaces + "///" + inner_spaces + "\\\\\\")
        inner_spaces += '  '
        index += 1
    print(shoes + "       " + shoes)
def print_shoes(shoes):
    print(shoes + "       " + shoes)
    
def main():
    print("----- AVATAR -----")
    user_avatar = input("Select an Avatar or create your own: \n")
    user_avatar = user_avatar.lower()
    while user_avatar != 'jeff' and user_avatar != 'adam' and user_avatar != 'chris' \
    and user_avatar != 'custom' and user_avatar != 'exit':
        user_avatar = input("Select an Avatar or create your own: \n")
        user_avatar.lower()
    if user_avatar == 'jeff':
        print_jeff()
    elif user_avatar == "adam":
        print_adam()
    elif user_avatar == 'chris':
        print_chris()
    elif user_avatar == 'custom':
        print('Answer the following questions to create a custom avatar')
        hat_style = input('Hat style ? \n')
        eye_character = input('Character for eyes ? \n')
        hair_style = input('Shaggy hair (True/False) ? \n')
        arm_style = input('Arm style ? \n')
        torso_length = int(input('Torso length ? \n'))
        leg_length = int(input('Leg length (1-4) ? \n'))
        shoe_style = input('Shoe look ? \n')
        print()
        print_custom(hat_style, eye_character, hair_style, arm_style, torso_length, leg_length, shoe_style)
main()