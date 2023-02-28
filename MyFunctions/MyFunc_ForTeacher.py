"""
 MY FUNCTIONS FOR:

   - see objects types, methods and attributes,
   - view objectS info in matrix form
   - time functions like pause, ......  
   - printing colors options
   - decisions functions
   - use HELP function
   - write in log files, like "comments log", "errors log"
   - OS most used functions
   - MODULES info

"""
#
# IMPORT LIBRERIES OR YOUR OWN FUNCTIONS 
#

#
# COLORS CONSTANTS
#

# FOREGORUND CONSTANTS AS TEXT
FG_WH_TXT = "\033[00m"
FR_GREEN = "\033[92m"
FR_RED   = "\033[91m"
NO_COLOR = "\033[00m"

#
# TIME FUNCTIONS
#

# pause function
def pause():  
  userInput = input(f"{FR_RED}Press ENTER to continue, or CTRL-C to exit{NO_COLOR}\n")  
        
#
# DECISIONS FUNCTIONS
#        

# Yes or No function
def Y_N(msg):  
    ans=str(input(msg))    
    if ans == 'N':                        
        return False
    elif ans == 'Y':                                
        return True
    else:
        Y_N(msg)
