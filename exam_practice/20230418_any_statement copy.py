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
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")

def printMsg(msg):
    print(f"{FR_GREEN}{msg}{NO_COLOR}")

def print_BN(msg):
    print(f"{msg}")       

def th_2_dec(num):
    return "{0:,.2f}".format(num)
    

if __name__ == "__main__":
  
    system('cls')
    print(F"\n\t{COL['yel']}\t=== ANY STATEMENT ==={COL['b_n']}\n")

    lista_notas=[1,2,3,4,5]

    Event = any(nota <3 for nota in lista_notas)
    print(f"\tEvent: {Event}")

    print(F"\n\t{FR_YELL}=== That's all for today ==={NO_COLOR}\n")

    jon_results = (0,0,0,0,0)
    maria_results= (1,1,1,1,1)

    
    Event_jon = all(result == 0 for result in jon_results)
    Event_maria = all(result == 1 for result in maria_results)
    print(f"\nJon - > {Event_jon} | maria -> {Event_maria}\n")
    
    # with ALL is not necesary to put need conditions
    Event_jon = all(jon_results)
    Event_maria = all(maria_results)
    print(f"\nJon - > {Event_jon} | maria -> {Event_maria}\n")