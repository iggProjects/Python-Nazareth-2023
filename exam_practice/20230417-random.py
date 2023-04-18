"""
Page 8
Crear un programa para 
imprimir valores aleatorios entre 0 y 10
Si el valor es mayor a 50, imprimir MAYOR. Si no, imprimir MENOR. Continuar hasta que el 
usuario diga “para!”.
imprimir valores aleatorios entre 0 y 1
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

def th_2_dec(num):
    return "{0:,.2f}".format(num)


if __name__ == "__main__":
  
   system('cls')
   print(F"\n\t{COL['yel']}=== RANDOM NUMBERS ==={COL['b_n']}\n")

   """
   numb = random.random()
   printMsg(' Probando números aleatorios entre 0 y 1')
   print(f'\t{numb}')

   numb = random.randint(1,100)
   printMsg(' Probando números enteros aleatorios entre 1 y 10')
   print(f'\t{numb}')
   """
   printMsg(" Loop números aleatorios, mientras user diga 'Y'\n")
   moreData = True
   # loop until stop is "Y"
   while moreData:    
      numb = random.randint(1,100)
      #print(f"\tnumber: {numb}")
      if numb > 50:
         print(f"\tel número '{numb}' es mayor de 50\n")  
      else:
         print(f"\tel número '{numb}' es menor o igual de 50\n")
      # si la rpta es cualquier valor distinto de 'Y', se finaliza el loop   
      ans=str(input("\nDo you want to continue? (Y): ")) 
      if ans == 'Y':
         pass
      else:
         print(f"\n\tUser respondió '{ans}'")
         printMsg('\tFin de loop')
         moreData = False

   print(F"\n\t{COL['gr']}=== That's all for today ==={COL['b_n']}\n")


