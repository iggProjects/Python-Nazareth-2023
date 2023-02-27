"""
OS examples
"""
# IMPORT LIBRARIES
import os
import platform

# IMPORT MY FUNCTIONS
import MyFunctions.MyFunc as MyFunc
import MyFunctions.Colors_out as Col

# CONSTANT SECTION
NO_COLOR = "\033[00m"
FR_GREEN = "\033[92m"

# IMPORT CONSTANTS

# 
#from os import walk
import os

print(f"\n------------------------------------------------\n")
myPath = os.getcwd()
f = []
for (dirpath, dirnames, filenames) in os.walk(myPath):
    f.extend(filenames)
    break
MyFunc.matrix_view(f,3)
print(f"\n------------------------------------------------\n")

parent = os.chdir('../')
parentPath = os.getcwd()
print(f"mypath {parentPath}")
f = []
for (dirpath, dirnames, filenames) in os.walk(parentPath):
    f.extend(filenames)
    break
MyFunc.matrix_view(f,3)
print(f"\n------------------------------------------------\n")

"""for method in dir(os):
    OS_method  = 'OS'+'.'+method
    print(f"{FR_GREEN}OS.method --> {NO_COLOR}´{OS_method}")

MyFunc.pause()

for method in dir(platform):
    platform_method= 'platform'+'.'+method
    print(f"{FR_GREEN}platform.method --> {NO_COLOR}´{platform_method}")

"""
  

