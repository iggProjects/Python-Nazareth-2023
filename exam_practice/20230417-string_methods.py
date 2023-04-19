"""
Texto
texto = "Pitón es un lenguaje de programación. Pitón está usado para la automación, 
análisis de datos e incluso la creación de páginas webs. Pitón es fácil de usar."
Usando los comandos de string, llevar a cabo lo siguiente:
    Reemplazar “Python” por “Piton”
    Imprimir el texto en mayúsculas
Conseguir imprimir la primera letra de cada palabra. Por ejemplo, P e u l d p …..
Imprimir todas las palabras en órden alfabético (página 35 de las notas de clase)
"""
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

if __name__ == "__main__":
  
    system('cls')
    print(F"\n\t{COL['yel']}=== String methods to change texts ==={COL['b_n']}\n")

    texto = "Pitón es un lenguaje de programación. Pitón está usado para la automación,\n análisis de datos e incluso la creación de páginas webs. Pitón es fácil de usar."

    print(f"{FR_YELL}Change Pitón with Python in this Text:{NO_COLOR}\n'{texto}'")
    new_texto=texto.replace('Pitón','Python')
    print(f"{FR_GREEN}New Text:{NO_COLOR}\n'{new_texto}'\n")

    new_texto_may = new_texto.upper()
    print(f"{FR_GREEN}New Text in mayúsculas:{NO_COLOR}\n'{new_texto_may}'\n")

    new_texto_list = new_texto.split()
    new_texto_1Mayusc_str = "" 
    """    
    for w in new_texto_list:
       new_texto_1Mayusc += w.capitalize() + ' '
    """
    new_texto_1Mayusc_list = [  w.capitalize() + ' ' for w in new_texto_list ]
    new_texto_1Mayusc_str = ''.join(w for w in new_texto_1Mayusc_list)
    
    print(f"{FR_GREEN}Primera letra de cada palabra en mayúsculas:{NO_COLOR}\n'{new_texto_1Mayusc_str}'\n")

    new_texto_minusc = new_texto.lower()
    new_texto_min_list = new_texto_minusc.split()
    print(f"{FR_GREEN}Lista palabras en orden alfabético:{NO_COLOR}\n'{sorted(new_texto_min_list)}'\n")

    print(F"\n\t{COL['gr']}=== That's all for today ==={COL['b_n']}\n")