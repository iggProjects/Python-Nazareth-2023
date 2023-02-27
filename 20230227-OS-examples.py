"""
OS examples
"""
# IMPORT LIBRARIES
import os
import platform

# IMPORT SECTION
import MyFunctions.MyFunc as MyFunc
import MyFunctions.Colors_out as Col

# CONSTANT SECTION
NO_COLOR = "\033[00m"
FR_GREEN = "\033[92m"

#
#  IMPORT MyFunctions
#

# IMPORT CONSTANTS

print(f"\f{FR_GREEN}platform.name --> {NO_COLOR}´{platform.uname()}\n")
print(f"\f{FR_GREEN}platform._Processor --> {NO_COLOR}´{platform._Processor()}\n")

# print(f"\fdir(os) --> {dir(os)}\n")

# print(f"\f{FR_GREEN}dir(platform) --> {NO_COLOR} {dir(platform)}\n")

# loop to present all methods-attributes of each
OS = dir(os)
MyFunc.matrix_view(OS,3)

PLATFORM = dir(platform)
MyFunc.matrix_view(PLATFORM,3)

