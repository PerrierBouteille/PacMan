from tkinter import *
from turtle import color

class colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# N  |  -1   |  x
#E O | 1  -1 | z
# S  |   1   |

###############################################################################################
#                                               MAP                                           #
###############################################################################################

L = [["     ","     ","     ","     ","     ","     ","     ","     ","     ","     ","     "],
     ["     ","     ","  ___","_____","___  ","  ___","_____","___  ","     ","     ","     "],
     ["     ","     "," |  _","_   _","_  | "," |  _","_____","_  | ","     ","     ","     "],
     ["     ","     "," | | "," | | "," | | "," | | ","     "," | | ","     ","     ","     "],
     ["     ","     "," | |_","_| | "," | |_","_| |_","___  "," | | ","     ","     ","     "],
     ["     ","     "," |  _","_  | "," |  _","_____","_  | "," | | ","     ","     ","     "],
     ["     ","     "," | | "," | | "," | | ","     "," | |_","_| | ","     ","     ","     "],
     ["     ","     "," | | "," | |_","_| | ","     "," |___","_  | ","     ","     ","     "],
     ["     ","     "," | | "," |___","___| ","     ","     "," | | ","     ","     ","     "],
     ["     ","     "," | | ","     ","     ","     ","     "," | | ","     ","     ","     "],
     ["     ","     "," | |_","_____","_____","_____","_____","_| | ","     ","     ","     "],
     ["     ","     "," |___","_____","_____","_____","_____","___| ","     ","     ","     "],
     ["     ","     ","     ","     ","     ","     ","     ","     ","     ","     ","     "]] 

###############################################################################################
#                                            VARIABLES                                        #
###############################################################################################

x = 5
z = 3
barrier = ""

###############################################################################################
#                                             CODE                                            #
###############################################################################################

print(colors.BLUE + L[x-1][z-1] + L[x-1][z] + L[x-1][z+1])
print(colors.BLUE + L[x][z-1] + L[x][z] + L[x][z+1], end="\r")
print(colors.BLUE + L[x][z-1] + L[x][z][:2] + colors.WARNING + "•" + colors.BLUE)
print(colors.BLUE + L[x+1][z-1] + L[x+1][z] + L[x+1][z+1] + colors.END)
print()
print(colors.BOLD + "Coordinate: " + colors.RED + "(X):" + str(x) +"" + colors.GREEN + " (Z):" + str(z) + colors.END)


while True:
    print(colors.BOLD + "──────────────────────────────────────" + colors.END)
    print()
    mve = input("Where do you want to go ? N/E/S/O: ")
    print(),print(),print()
    if (mve.__len__() == 1):
        if (mve.lower() == 'n' or mve.lower() == 'z'):
            x -= 1
            barrier = "n"
        elif (mve.lower() == 'e' or mve.lower() == 'd'):
            z += 1
            barrier = "e"
        elif (mve.lower() == 's'):
            x += 1
            barrier = "s"
        elif (mve.lower() == 'o' or mve.lower() == 'q'):
            z -= 1
            barrier = "o"
        else:
            print(colors.RED + "Sorry but it's not a direction." + colors.END)


        if(barrier == "n"):
            if(L[x][z] == '_____' or L[x][z] == '     ' or L[x][z] == '  ___' or L[x][z] == '___  ' or L[x][z] == ' ___ '):
                x+=1
                print(colors.RED + "Sorry but you can't go here." + colors.END)
                print(), print()
            print()
            print(colors.BLUE + L[x-1][z-1] + L[x-1][z] + L[x-1][z+1])
            print(colors.BLUE + L[x][z-1] + L[x][z] + L[x][z+1], end="\r")
            print(colors.BLUE + L[x][z-1] + L[x][z][:2] + colors.WARNING + "•" + colors.BLUE)
            print(colors.BLUE + L[x+1][z-1] + L[x+1][z] + L[x+1][z+1] + colors.END)

        elif(barrier == "s"):
            if(L[x][z] == '     ' or L[x][z] == '  ___' or L[x][z] == '___  ' or L[x][z] == ' ___ '):
                x-=1
                print(colors.RED + "Sorry but you can't go here." + colors.END)
                print(), print()
            print()
            print(colors.BLUE + L[x-1][z-1] + L[x-1][z] + L[x-1][z+1])
            print(colors.BLUE + L[x][z-1] + L[x][z] + L[x][z+1], end="\r")
            print(colors.BLUE + L[x][z-1] + L[x][z][:2] + colors.WARNING + "•" + colors.BLUE)
            print(colors.BLUE + L[x+1][z-1] + L[x+1][z] + L[x+1][z+1] + colors.END)
        
        elif(barrier == "e"):
            if(L[x][z] == ' |  _' or L[x][z] == ' | | ' or L[x][z] == '_| |_' or L[x][z] == ' | |_' or L[x][z] == '_| | ' or L[x][z] == '     ' or L[x][z] == '  ___' or L[x][z] == '___  ' or L[x][z] == ' ___ '):
                z-=1
                print(colors.RED + "Sorry but you can't go here." + colors.END)
                print(), print()
            print()
            print(colors.BLUE + L[x-1][z-1] + L[x-1][z] + L[x-1][z+1])
            print(colors.BLUE + L[x][z-1] + L[x][z] + L[x][z+1], end="\r")
            print(colors.BLUE + L[x][z-1] + L[x][z][:2] + colors.WARNING + "•" + colors.BLUE)
            print(colors.BLUE + L[x+1][z-1] + L[x+1][z] + L[x+1][z+1] + colors.END)

        elif(barrier == "o"):
            if(L[x][z] == '_  | ' or L[x][z] == ' | | ' or L[x][z] == '_| |_' or L[x][z] == ' | |_' or L[x][z] == '_| | ' or L[x][z] == '     ' or L[x][z] == '  ___' or L[x][z] == '___  ' or L[x][z] == ' ___ '):
                z+=1
                print(colors.RED + "Sorry but you can't go here." + colors.END)
                print(), print()
            print()
            print(colors.BLUE + L[x-1][z-1] + L[x-1][z] + L[x-1][z+1])
            print(colors.BLUE + L[x][z-1] + L[x][z] + L[x][z+1], end="\r")
            print(colors.BLUE + L[x][z-1] + L[x][z][:2] + colors.WARNING + "•" + colors.BLUE)
            print(colors.BLUE + L[x+1][z-1] + L[x+1][z] + L[x+1][z+1] + colors.END)
        else:
            print(), print(), print()
            print(colors.BLUE + L[x-1][z-1] + L[x-1][z] + L[x-1][z+1])
            print(colors.BLUE + L[x][z-1] + L[x][z] + L[x][z+1], end="\r")
            print(colors.BLUE + L[x][z-1] + L[x][z][:2] + colors.WARNING + "•" + colors.BLUE)
            print(colors.BLUE + L[x+1][z-1] + L[x+1][z] + L[x+1][z+1] + colors.END)

        print()
        print(colors.BOLD + "Coordinate: " + colors.RED + "(X):" + str(x) +"" + colors.GREEN + " (Z):" + str(z) + colors.END)   
    else:
        print(colors.RED + "Sorry but you can't donate to direction at same time." + colors.END)
        print(), print(), print()
        print(colors.BLUE + L[x-1][z-1] + L[x-1][z] + L[x-1][z+1])
        print(colors.BLUE + L[x][z-1] + L[x][z] + L[x][z+1], end="\r")
        print(colors.BLUE + L[x][z-1] + L[x][z][:2] + colors.WARNING + "•" + colors.BLUE)
        print(colors.BLUE + L[x+1][z-1] + L[x+1][z] + L[x+1][z+1] + colors.END)
        print()
        print(colors.BOLD + "Coordinate: " + colors.RED + "(X):" + str(x) +"" + colors.GREEN + " (Z):" + str(z) + colors.END)