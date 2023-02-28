# probando la sentencia "from file import function"
#
# https://www.geeksforgeeks.org/python-import-module-from-different-directory/
# https://es.stackoverflow.com/questions/401804/python-importerror-attempted-relative-import-with-no-known-parent-package
# https://problemsolvingwithpython.com/07-Functions-and-Modules/07.05-Calling-Functions-from-Other-Files/#:~:text=To%20use%20the%20functions%20written,of%20the%20filename%20during%20import.
# https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
# https://stackoverflow.com/questions/24622041/python-importing-a-module-from-a-parallel-directory
# https://www.reddit.com/r/learnpython/comments/50795d/how_to_load_module_from_parallel_directory/
# https://dkhambu.medium.com/importing-files-in-python-repository-28ab49fade37
#

## If zFunctions is in the directory
#from zFunctions import mostrar, ver_objetos
##

## calling zFunctions from its folder
## Create file __init__.py empty in that folder - is for read dir

import sys
init_path = sys.path
for fold in init_path:
    print(f"{fold}")
print()    

#print(f"\norig path -->  {init_path}\n")

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'c:\\Users\\alu01\\Documents\\igg-Python\\Python-Nazareth-2023\\MyFunctions')
new_path = sys.path
for fold in new_path:
    print(f"{fold}")
print()

from Colors_out import *
from MyFunc import *

#print(f"\nnew path -->  {new_path}\n")
pause()

prYellow('Original path')
for fold in init_path:
    prBlue(fold)


prPurple('path actualizado\n')
for fold in new_path:
    prBlue(fold)

