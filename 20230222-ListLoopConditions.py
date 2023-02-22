"""
    examples
"""

from MyFunctions.MyFunc import *
from MyFunctions.Colors import *

numbers=[1,2,5,-6,0]

pos_numbers = [i for i in numbers if i >= 0 ]

print(f"Positive numbers in list --> {pos_numbers}")

print(f"{numbers[3]}")

mostrar(numbers)
