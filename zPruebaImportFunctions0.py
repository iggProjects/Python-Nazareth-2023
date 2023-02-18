
# probando la sentencia "from file import function"
#
# https://sweetcode.io/python-file-importation-multi-level-directory-modules-packages/
# https://www.geeksforgeeks.org/python-import-module-from-different-directory/
# https://es.stackoverflow.com/questions/401804/python-importerror-attempted-relative-import-with-no-known-parent-package
# https://problemsolvingwithpython.com/07-Functions-and-Modules/07.05-Calling-Functions-from-Other-Files/#:~:text=To%20use%20the%20functions%20written,of%20the%20filename%20during%20import.
# https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
#

# calling zFunctions from its folder
# Create file __init__.py empty in that folder - is for read dir

# import sys
# caution: path[0] is reserved for script path (or '' in REPL)
# sys.path.insert(0, '../MyFunctions/')
# sys.path.insert(0, 'C:\ML_Project\NazarethCourse2023\Python-Nazareth-2023\MyFunctions')

# searching in "sub folder" MyFunctions
from MyFunctions.MyFunc import *
from MyFunctions.Colors import *

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