# page 9

# CONSTANTS
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
  userInput = input(f"{COL['red']}Press ENTER to continue, or CTRL-C to exit{COL['b_n']}\n")  

if __name__ == "__main__":

    system('cls')
    print(F"\n\t{COL['yel']}=== TITLE ==={COL['b_n']}\n")


    print(f"\n\t{COL['yel']}Script para imprimir las letras que están en mayúsculas{COL['b_n']}\n")

    texto = "This is a Long text and Only the letters with Capital letters will be Included"
    #texto2 = "This is a    Long     text    and Only the letters with Capital letters will be Included"
    print(f"\t{COL['gr']}first text{COL['b_n']}\n\t{texto}\n")
    #print(f"\t{COL['yel']}second text with multiple spaces between words\n\t{COL['b_n']}{texto2}\n")

    print(f"\t{FR_YELL}List of words in text:{NO_COLOR}\n")
    texto_list = texto.split(" ")  
    print(f"\t{texto_list}")
    print()
    print()

    upperLettersInText = []
    for w in texto_list:
      #print(w[0])
      if w[0].isupper():
        upperLettersInText.append(w[0])     
    print(f"\t{FR_GREEN}list of Upper Letters in list of words{NO_COLOR}\n\t{upperLettersInText}\n")

    words_lower = [w.lower() for w in texto_list]
    print(f"{FR_YELL}\tlist of words sorted ascending\n\t{NO_COLOR}{sorted(words_lower)}\n")    

    print(F"\t{COL['gr']}=== That's all for today ==={COL['b_n']}\n")

