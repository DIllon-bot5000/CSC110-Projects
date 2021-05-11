#
#Author: Dillon Barr
#Description: Program takes user input for height and length and then generates an AT-AT
#

neckLength = int(input("Neck Length: \n"))
bodyHeight = int(input("Body Height: \n"))
legHeight = int(input("Leg Height: \n"))

print("\n     _,.-Y  |  |  Y-._")
print(' .-~"   ||  |  |  |   "-.' + "\n |______________________|" * bodyHeight)
print(" |______________________|" + " " * neckLength + "    _____")
print(' L______________________[---' + "-" * neckLength + 'I" .-{"-.')
print("I____________________ [__L]" + "_" * neckLength + "[I_/r(=}=-P")
print("L________________________j~ " + " " * neckLength + "'-=c_]/=-^")
print("\\________________________]")
print("  [___________________]")
print('     I--I"~~"""~~"I--I''' + "\n     |\\n|         |\\n|" * legHeight)
print("     ([])         ([])")
print("    /|..|\\       /|..|\\")
print("   |=}--{=|     |=}--{=|")
print("  .-^--e-^-.   .-^--e-^-.")