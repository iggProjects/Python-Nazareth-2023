"""
            😎  My colors for printing  😎
"""

# https://www.geeksforgeeks.org/print-colors-python-terminal/
# colored text and background 
# fore
def prRed(msg):         print("\033[91m{}\033[00m".format(msg)) 
def prGreen(msg):       print("\033[92m{}\033[00m".format(msg)) 
def prYellow(msg):      print("\033[93m{}\033[00m".format(msg)) 
def prLightPurple(msg): print("\033[94m{}\033[00m".format(msg)) 
def prPurple(msg):      print("\033[95m{}\033[00m".format(msg)) 
def prCyan(msg):        print("\033[96m{}\033[00m".format(msg)) 
def prLightGray(msg):   print("\033[97m{}\033[00m".format(msg)) 
def prBlack(msg):       print("\033[98m{}\033[00m".format(msg)) 

prCyan('HOLA')
print('HOLA')
prRed('HOLA')
prBlack('HOLA')