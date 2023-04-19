"""
Crear un programa para:

    Imprimir los valores de esta lista, excluyendo los valores en negativo (2)
    Al imprimir, imprimes "Hola numero 6" si el valor es 6. (1)

    lista = [5, 3, 12, -6, -3, 1, 6, 8, -12]

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
    print(F"\n{COL['yel']}SCRIPT QUE IMPRIME NÚMEROS DE UNA LISTA EN BASE A CONDICIONES DADAS{COL['b_n']}\n")

    print(f"{FR_GREEN}Las condiciones son:{NO_COLOR}\n\tNo imprimir nros negativos\n\tY si el número es el 6 color un mens: Hola número 6 !")

    # lISTA ORIGINAL
    lista = [5, 3, 12, -6, -3, 1, 6, 8, -12]
    print(f"{FR_GREEN}\nLa lista es: {NO_COLOR} {lista}\n")

    print(f"{FR_GREEN}Ejecución de laimpresión{NO_COLOR}\n")
    for n in lista:
        if n < 0:
            pass
        elif n == 6:
            print(f"\t{FR_YELL}Hola número 6 !{NO_COLOR}")
        else:
            print(f"\t{FR_GREEN}{n}{NO_COLOR}")

    print(F"\n\t{FR_YELL}=== That's all for today ==={NO_COLOR}\n")