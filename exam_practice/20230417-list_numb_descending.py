#
# Crear un programa para mostrar los números de 100 hasta 0 en bloques de 10. 
# Por ejemplo, 100, 90, 80, 70 ….10, 0.
#


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
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")

def printMsg(msg):
    print(f"{FR_GREEN}{msg}{NO_COLOR}")

def print_BN(msg):
    print(f"{msg}")       

def th_2_dec(num):
    return "{0:,.2f}".format(num)

if __name__ == "__main__":
  
    system('cls')
    print(F"\n\t{COL['yel']}=== mostrar la secuencia descendente de  10 en 10, empezando con 100 ==={COL['b_n']}\n")

    for n in range(100,1,-10):
        print_BN(f"\t{str(n).rjust(3)}")

    print(F"\n\t{COL['gr']}=== That's all for today ==={COL['b_n']}\n")