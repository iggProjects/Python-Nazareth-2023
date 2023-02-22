"""
    examples
"""

import MyFunc
import Colors

numbers=[1,2,5,-6,0]

pos_numbers = [i for i in numbers if i >= 0 ]

print(f"Positive numbers in list --> {pos_numbers}")

print(f"{numbers[3]}")

#MyFunc.mostrar(numbers)
MyFunc.desc_obj_method((numbers))

