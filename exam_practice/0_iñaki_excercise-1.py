"""
Un Animal

    Un Perro
        patas (por ejemplo, 4)
        nombre
        raza
        hacerRuido() # imprime Woof, woof
        correr() # imprime estoy corriendo
    Un Pajaro
        patas (por ejemplo, 2)
        nombre
        hacerRuido() # imprime Tweet, tweet
        volar() # todavia no tenemos detalles de este método

Acciones:

    Crear 3 objetos y sus atributos y métodos (6)
    Crear código para instanciar un Perro (1)
    Ejecutar el método hacerRuido() y correr() del Perro (1)

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
    print(F"\n{COL['yel']}SCRIPT QUE SIMULA ANIMALES COMO PÁJAROS Y PERROS{COL['b_n']}\n")
    print(f"\t{FR_GREEN}Acciones a incluir en el script:{NO_COLOR}\n\tCrear 3 objetos y sus atributos y métodos (6)\n\tCrear código para instanciar un Perro (1)\n\tEjecutar el método hacerRuido() y correr() del Perro (1)\n\n")

    # clase padre
    class Animal:
        # attributes
        def __init__(self,nombre,patas):
            self.nombre = nombre
            self.patas  = patas

    # clase hijo Pájaro
    class Pajaro(Animal):
        def __init__(self,nombre,patas):
            super().__init__(nombre,patas)
        # methods
        # ruido
        def hacer_ruido(self):
            #print(f"\t\ttuit tuit tuit") 
            # usando return para entregar 'string' para incluir en el print del MAIN
            return f"{FR_RED}tuit tuit tuit{NO_COLOR}" 

    # clase hijo "Perro", que agrega atributo adicional "raza" y un método adic: movimiento
    class Perro(Animal):
        def __init__(self,nombre,patas,raza):
            super().__init__(nombre,patas)
            self.raza = raza
        # methods
        # ruido
        def hacer_ruido(self):
            print(f"\t\tguao guao guao")                 
        # movimiento
        def correr(self):
            # usando print directamente, con lo que se salta una línea al invocarse
            print(f"\t\tcorriendo muy rápido !!!")                 
    


    paraulata = Pajaro('Paraulata',2)
    print(f"\tpájaro paraulata\n\t{vars(paraulata)}")
    print(f"\t{FR_GREEN}paraulata canta así: {paraulata.hacer_ruido()}{NO_COLOR}")
    paraulata.hacer_ruido()

    print()

    doggy = Perro('doggy',4,'buldog')       
    print(f"\tperro doggy\n\t{vars(doggy)}")
    print(f"\t{FR_GREEN}doggy ladra así:{NO_COLOR}")
    doggy.hacer_ruido()
    print(f"\t{FR_GREEN}y se mueve:{NO_COLOR}")
    doggy.correr()


    print(F"\n\t{FR_YELL}=== That's all for today ==={NO_COLOR}\n")