"""
Exam Prototype
"""

from os import system
import random

# CONSTANTS
# Col_dict
COL = {'b_n':'\033[00m','red':'\033[91m','gr':'\033[92m','yel':'\033[93m'} 

# FR Colors
NO_COLOR = "\033[00m"
FR_GREEN = "\033[92m"
FR_RED   = "\033[91m"
FR_BLUE  = "\033[94m"
FR_YELL  = "\033[93m"

# pause function
def pause():  
  userInput = input(f"\n{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")

def printMsg(msg):
    print(f"{FR_GREEN}{msg}{NO_COLOR}")

def print_BN(msg):
    print(f"{msg}")       

def th_2_dec(num):
    return "{0:,.2f}".format(num)
    
def repetirXveces(n):
    if n == 6:
        lista=[*range(0,6)]
        print(f"\tlista: {lista}")
    elif n == 10:
        lista=[*range(0,10)]
        lista.remove(5)
        lista.remove(6)
        print(f"\tlista: {lista}")
    else:
        pass

if __name__ == "__main__":
  
    system('cls')
    print(F"\n\t{COL['yel']}=== repetirXveces ==={COL['b_n']}\n")


    veces = int(input("\t¿Cuántas veces quiere repetir?: "))
    repetirXveces(veces)

    print(F"\n\t{FR_YELL}=== That's all for today ==={NO_COLOR}\n")