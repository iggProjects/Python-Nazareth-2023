"""
Imprimir los valores impares, empezando desde 1 hasta 20. 

código

Sin embargo, este código no te funciona. Modificarlo para que funcione.
"""

# CONSTANTS
# Col_dict
COL = {'b_n':'\033[00m','red':'\033[91m','gr':'\033[92m','yel':'\033[93m'} 

# FR Colors
NO_COLOR = "\033[00m"
FR_GREEN = "\033[92m"
FR_RED   = "\033[91m"
FR_BLUE  = "\033[94m"
FR_YELL  = "\033[93m"

from os import system
import random

# pause function
def pause():  
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")

def printMsg(msg):
    print(f"{FR_GREEN}{msg}{NO_COLOR}")    

def print_BN(msg):
    print(f"{msg}")          
   

if __name__ == "__main__":
  
    system('cls')
    print(F"\n\t{COL['yel']}=== TITLE ==={COL['b_n']}\n")

    for p in range(1,21):
       printMsg(f' El numeral natural {str(p).rjust(2)}')
       if p % 2 == 0:
          print_BN('\tes par')
       else:
          print_BN('\tes impar')   

    print(F"\n\t{COL['gr']}=== That's all for today ==={COL['b_n']}\n")