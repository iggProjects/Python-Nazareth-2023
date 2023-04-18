"""
Page 8
Crear un programa para 
imprimir valores aleatorios entre 0 y 10
Si el valor es mayor a 50, imprimir MAYOR. Si no, imprimir MENOR. Continuar hasta que el 
usuario diga “para!”.
imprimir valores aleatorios entre 0 y 1
""" 

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

from os import system
system('cls')

# pause function
def pause():  
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")  

def printMsg(msg):
   print(f"{FR_GREEN}{msg}{NO_COLOR}")       


if __name__ == "__main__":
  
    system('cls')
    print(F"\n\t{COL['yel']}=== RANDOM NUMBERS ==={COL['b_n']}\n")

    numb = random.random()
    printMsg(' Probando números aleatorios entre 0 y 1')
    print(f'\t{numb}')

    numb = random.randint(1,10)
    printMsg(' Probando números enteros aleatorios entre 1 y 10')
    print(f'\t{numb}')

    printMsg(' Loop números aleatorios hasta que user diga salir')
    moreData = True
    # loop until stop is "Y"
    while moreData:    
        numb = random.randint(1,10)
        print(f"\tnumber: {numb}")    
        ans=str(input("\nDo you want to continue? (Y,N): ")) 
        if ans == 'Y':
           pass
        else:
           printMsg('Fin de loop')
           moreData = False




    print(F"\n\t{COL['gr']}=== That's all for today ==={COL['b_n']}\n")


