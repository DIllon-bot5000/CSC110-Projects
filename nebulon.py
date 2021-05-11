#
# Author: Dillon Barr
# Description: This program takes user input and builds
#              a neubulon ship to the desired length and layers.

largeLayers = int(input("Large Layers on bottom: \n"))
mediumLayers = int(input("Medium Layers on bottom: \n"))
smallLayers = int(input("Small Layers on bottom: \n"))
frontLength = int(input("Front length: \n"))
middleLength = int(input("Middle length: \n"))
backLength = int(input("Back length: \n"))

mediumWhiteSpaces = ' ' * ((frontLength - 3 + 5) - ((frontLength // 2) + 2))
smallWhiteSpaces = ' ' * ((frontLength - 3 + 5) - ((frontLength // 3) + 3))
largeLayer = ("   /" + "-" * (frontLength - 3) + "|" + "\n   \\" 
              + "=" * (frontLength - 3) + "|\n")
mediumLayer = (mediumWhiteSpaces + "/" + "+" * (frontLength // 2) 
               + "|" + "\n" + mediumWhiteSpaces + "\\" + "-" 
               * ((frontLength // 2)) + "|\n")
bottomLayer = (smallWhiteSpaces + "\\" + "<" * (frontLength // 3) 
               + "|" + "\n " + smallWhiteSpaces 
               + "<" * (frontLength // 3) + "|\n")

print("\n  /=" + "-" * frontLength + "\\" + " " * (middleLength + 9)
      + "/" + "-" * backLength + "|")

print(" /==" + "/" * frontLength + "==\\\\\\" + " " * (middleLength + 4) 
      + "|=" + "=" * backLength + "|")

print("|==-" + "\\" * frontLength + "=" * 6 + "\\--" + ("=" * middleLength) 
      + "==" + "=" * backLength + "|")

print(" \\" + "=" * frontLength + "====-------" + ("-" * middleLength) 
      + "--" + "-" * backLength + "|")

print("  \\=" + "-" * frontLength + "=///" + " " * (middleLength + 5) 
      + "\\" + "=" * backLength + "=/")

print(largeLayer * int(largeLayers), end='')
print(mediumLayer * int(mediumLayers), end='')
print(bottomLayer * int(smallLayers), end='')