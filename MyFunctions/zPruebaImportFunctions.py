# probando la sentencia "from file import function"
#
# https://www.geeksforgeeks.org/python-import-module-from-different-directory/
# https://es.stackoverflow.com/questions/401804/python-importerror-attempted-relative-import-with-no-known-parent-package
# https://problemsolvingwithpython.com/07-Functions-and-Modules/07.05-Calling-Functions-from-Other-Files/#:~:text=To%20use%20the%20functions%20written,of%20the%20filename%20during%20import.
# https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
#

## If zFunctions is in the directory
#from zFunctions import mostrar, ver_objetos
##

## calling zFunctions from its folder
## Create file __init__.py empty in that folder - is for read dir

import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(0, '\ML_Project\Python-igg\Modulo-2-Sgf\igg\MyFunctions')
from zFunctions import *
#from zFunctions import mostrar, ver_objetos

##

def Purple(mens): print("\033[95m{}\033[00m\n" .format(mens)) 
def Yellow(mens): print("\033[93m{}\033[00m\n" .format(mens)) 

# https://www.geeksforgeeks.org/print-colors-python-terminal/
# colored text and background 

def prRed(skk): print("\033[91m{}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m{}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m{}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m{}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m{}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m{}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m{}\033[00m" .format(skk)) 

# type Cadena
Purple('type string')
var1='Hola Inaki'
mostrar(var1)
variable="Epale Gainzarain, que estas haciendo?"
mostrar(var1[3:15])
mostrar( len(var1))
mostrar(var1[-3])

ver_objetos(var1)

## see how to do that
#zFunctions.ver_objetos(var1)