"""
Usando la fórmula, (5 puntos)
Escribir un programa para calcular velocidad, distancia o tiempo (uno de los 3).
Preguntar al usuario por los datos necesarios e imprimir el resultado correctamente formateado. 
Incluir comentarios
No hace falta importar ninguna biblioteca.
: = división, . = multiplicación

¿Cómo podrías mejorar este programa para que sea más fácil de mantener en el futuro? 
Escribir el código para mostrar cómo lo harías 
(no tienes que hacer de todo, solo una muestra).

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
    print(F"\n\t{COL['yel']}=== Simulando una calculadora de velocidad, dada la distancia recorrida y el tiempo empleado ==={COL['b_n']}\n")

    
    repeat = True
    # loop until a number is captured
    while repeat:   
        # input distancia
        try:
            dist = float(input("\ndistancia recorrida: "))
            if dist < 0:
                printMsg('\tIndique un número >=0 !!!') 
            else:        
                print(f"\n\tDistancia recorrida (mts)'{dist}'")
                printMsg('\tFin de loop distancia\n')
                repeat = False
            
        except ValueError: 
            printMsg('\tIndique un número >=0 !!!')     

    repeat = True
    # loop until a number is captured
    while repeat:   
        # input tiempo
        try:
            time_ = float(input("\nTiempo Empleado (seg): "))
            if time_ < 0:
                printMsg('\tIndique un tiempo >=0 !!!') 
            else:        
                print(f"\n\tTiempo empleado '{time_}'")
                printMsg('\tFin de loop tiempo\n')
                repeat = False
            
        except ValueError: 
            printMsg('\tIndique un tiempo positvo > 0 !!!')            

    printMsg(f"\n{FR_YELL}=== La velocidad del objeto es: {th_2_dec(dist/time_)} mts/seg ===")
    print(F"\n\t{COL['gr']}=== That's all for today ==={COL['b_n']}\n")