"""
            😎  My colors for printing  😎
"""
# https://www.geeksforgeeks.org/print-colors-python-terminal/
# colored text and background 

# TEXT CONSTANTS


# BACKGROUND CONSTANTS
BG_BLACK  = 16
BG_BLUE   = 17
BG_RED    = 124
BG_ORANGE = 165



# foreground
def prRed(msg):         print("\033[91m{}\033[00m".format(msg)) 
def prGreen(msg):       print("\033[92m{}\033[00m".format(msg)) 
def prYellow(msg):      print("\033[93m{}\033[00m".format(msg)) 
def prLightPurple(msg): print("\033[94m{}\033[00m".format(msg)) 
def prPurple(msg):      print("\033[95m{}\033[00m".format(msg)) 
def prCyan(msg):        print("\033[96m{}\033[00m".format(msg)) 
def prLightGray(msg):   print("\033[97m{}\033[00m".format(msg)) 
def prBlue(msg):        print("\033[34m{}\033[00m".format(msg)) 
def prBlack(msg):       print("\033[98m{}\033[00m".format(msg)) 

# background
def prBG(msg,col):
    col1 = str(col)
    return print(("\033[48;5;" + col1 + "m " + msg + " \033[0;0m\n"))
    #return(f"\033[48;5;{col1}m {col1} \033[0;0m\n".format(msg))

def prOrangeBG(msg): 
    return print(("\033[48;2;255;165;0m {} \033[0;0m".format(msg)))

# fg
prRed('Zaspiki zara...') 
prGreen('Zaspiki zara...')
prYellow('Zaspiki zara...')
prLightPurple('Zaspiki zara...')
prPurple('Zaspiki zara...')
prCyan('Zaspiki zara...')
prLightGray('Zaspiki zara...')
prBlue('Zaspiki zara...')
prBlack('Zaspiki zara...')
print()

# bg
prBG('Zaspiki zara...',BG_BLACK)   # black
prBG('Zaspiki zara...',BG_BLACK)   # black
prBG('Zaspiki zara...',BG_BLUE)    # blue 
prBG('Zaspiki zara...',BG_RED)     # red
prBG('Zaspiki zara...',BG_ORANGE)  # orange

prOrangeBG('Zaspiki zara...')