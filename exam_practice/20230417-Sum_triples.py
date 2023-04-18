"""
    Crear la función para sumar 3 números
    total = sumar(6, 7, 7)
"""

# CONSTANTS
COL = {'b_n':'\033[00m','red':'\033[91m','gr':'\033[92m','yel':'\033[93m'} 

from os import system
system('cls')

# pause function
def pause():  
  userInput = input(f"{COL['red']}Press ENTER to continue, or CTRL-C to exit{COL['b_n']}\n")  

def sum(a,b,c):
   return a+b+c

def sum_lista(lista):
   suma=0
   for i in range(len(lista)+1):
      suma += i
   return suma


if __name__ == "__main__":
  
    system('cls')
    print(F"\n\t{COL['yel']}Script para calcular la suma de tres números dados,\n\to de una lista de números usando funciones{COL['b_n']}\n")

    a=1;b=2;c=3
    print(f"\tLa suma de {a}, {b} y {c} es: {COL['yel']}{sum(a,b,c)}{COL['b_n']}")

    lis_num = [1,2,3,4,5,6]
    print(f"\n\tLa suma de la lista de números {lis_num} es: {COL['yel']}{sum_lista(lis_num)}{COL['b_n']}")

    print(F"\n\t{COL['gr']}=== That's all for today ==={COL['b_n']}\n")