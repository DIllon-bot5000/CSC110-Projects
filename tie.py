###
###Author: Dillon Barr
###Description: This program accepts user input for widt
###             and prints a corresponding TIE Fighter.
###

tieWidth = int(input('Enter TIE width: \n'))
middle = "|== X ==|"
print('\n|[' + " " * ((tieWidth * 2) + int(9)) + ']|')
print('|[' + " " * ((tieWidth * 2) + int(9)) + ']|')
print('|[' + " " * ((tieWidth * 2) + int(9)) + ']|')
print('|[' + " " * tieWidth + " /=---=\ " + " " * tieWidth + ']|')
print('|[' + " " * tieWidth + "/==---==\\" + " " * tieWidth + ']|')
print('|[' + "/" * tieWidth + "|== X ==|" + '\\' * tieWidth + ']|')
print('|[' + " " * tieWidth + "\==---==/" + " " * tieWidth + ']|')
print('|[' + " " * tieWidth + " \=---=/ " + " " * tieWidth + ']|')
print('|[' + " " * ((tieWidth * 2) + int(9)) + ']|')
print('|[' + " " * ((tieWidth * 2) + int(9)) + ']|')
print('|[' + " " * ((tieWidth * 2) + int(9)) + ']|')