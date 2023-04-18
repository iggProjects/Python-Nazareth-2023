"""
Teniendo esta lista de compra:
lista_compra = [“manzanas”, “leche”, “papel de cocina”]
Crear un programa para preguntar al usuario si quiere añadir una nueva objeto a su lista, 
o mostrar todo lo que hay en la lista de compra.
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
    print(F"\n\t{COL['yel']}=== Script para agregar items a lista o visualizar su contenido ==={COL['b_n']}\n")

    lista_compra = ['manzanas', 'leche', 'papel de cocina']

    repeat = True
    # loop until a number is captured
    while repeat:   
        # input tiempo
        try:

            accion = str(input("\nAgregar frutas, o imprimir listado frutas ('A','L') -> "))

            if accion == 'A':
                printMsg('\tAgregando')

                seguir = str(input("\nContinuar ('S') ? caso positivo responda con la letra S -> "))
                if seguir == 'S':
                    pass
                else:
                    print_BN(f"\n\trpta usuario:'{seguir}'")
                    printMsg("\t=== Saliendo del Proceso ===") 
                    repeat = False

            elif accion == 'L':
                printMsg('\tImprimiendo listado frutas')   

                seguir = str(input("\nContinuar ('S') caso positivo responda con la letra S -> "))
                if seguir == 'S':
                    pass
                else: 
                    print_BN(f"n\trpta usuario:'{seguir}'")
                    printMsg("\t=== Saliendo del Proceso ===") 
                    repeat = False
    
            else:        
                pass
            
        except ValueError: 
            printMsg('\tDebe responder con una letra !!!')         

    print(F"\n\t{FR_YELL}=== That's all for today ==={COL['b_n']}\n")