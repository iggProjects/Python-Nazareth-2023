"""
    Dict: days of weeks
"""
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

  days_week = {'1':'lunes','2':'martes','3':'miércoles','4':'jueves','5':'viernes','6':'sábado','7':'domingo',}

  print(f"\nLos días de la semana usando una variable tipo 'dict':\n")
  pause()

  for k,v in days_week.items():
      print(f"\t{COL['yel']}día {k}:{NO_COLOR} {v}")
  print(f"\n{COL['b_n']}===== That's all =====\n")    