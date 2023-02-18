# function numbers -- page 16

# IMPORT  (searching in "sub folder" MyFunctions)
from MyFunctions.MyFunc import *
from MyFunctions.Colors import *

def numbers():
  return 10,20,30,40,50

print(f"numbers values: {numbers()}, and 'numbers' type is: {type(numbers())}\n") 
print(f"numbers at: {numbers}") 
print(f"numbers is located in: {id(numbers())}")
print(f"attributes & methods for numbers() type of data:\n\t{dir(numbers())}")  
print(f"first value of numbers(): {numbers()[0]} \n") 
print("---------------------------------------------------------------")

# variable a
a = numbers();
print(f"values of variable 'a': {a} ") 
print(f"first value of a(): {a[0]} ") 
print(f"second value of a(): {a[1]} ") 
print(f"length of a(): {len(a)} ") 
print("---------------------------------------------------------------")

# map of 'a' with functions
# squares
squares_a = [ i*i for i in a ]
print(f"squares of 'a': { squares_a }")
# cubics of even numbers in a
print(f"cubics of 'a' for multiples of 3: { [ i*i*i for i in a if i%3==0 ] }")
 
# a, b
# a, b = numbers();  does not works

c = [1,2,3,4,5]
# 
cubics_c = ( i*i*i for i in c if i%2==0 )
print(f"\ncubics of c for even values: { cubics_c },\nand type of cubics_c is: {type(cubics_c)}")
for x in cubics_c:
  print(x) 
print("---------------------------------------------------------------")
cubics_even_c = [ i*i*i for i in c if i%2==0 ]
print(f"cubics of c for even values: { cubics_even_c },\nand type of cubics_c is: {type(cubics_even_c)} ")

# link to other NB


#
# HELP FUNCTION
#
print("\n------------------------HELP FOR 'numbers'-----------------------------------")
#print(f"{help(numbers)}\n\n")
print("\n------------------------HELP FOR 'a'-----------------------------------")
#print(f"{help(a)}")