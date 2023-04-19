"""
page 8 - img
Diccionarios
Añadir un nuevo clave y valor al diccionario coche (descapotable, False). 
Imprimir todos sus claves y valores, excepto los con valores tipo int.
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
    

if __name__ == "__main__":
  
    system('cls')
    print(F"\n\t{COL['yel']}=== ADD NEW KEY-VALUE TO A DICT ==={COL['b_n']}")

    coche = {'brand':'Ford','modelo':'mustang','año':194}
    print(f"\n\t{FR_YELL}coche dict:{NO_COLOR}\n\t{coche}")

    # add new key,value in 'coche'
    coche['descapotable'] = False
    print(f"\n\t{FR_YELL}coche dict with new key-val:{NO_COLOR}\n\t{coche}")

    # print not integer values of dict
    print(f"\n\t{FR_YELL}printing not integer values of dict:{NO_COLOR}\n")
    for k,v in coche.items():
        if 'int' not in str(type(v)):
            print(f"\t\t{k} : {v}")

    print(F"\n\t{FR_YELL}=== That's all for today ==={NO_COLOR}\n")