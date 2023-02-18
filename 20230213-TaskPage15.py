#
# page 15
#

# IMPORT  (searching in "sub folder" MyFunctions)
from MyFunctions.MyFunc import *
from MyFunctions.Colors import *

#
# First point
#
# Preguntar al usuario por su salario. Multiplicar el salario que introduce el usuario por 10, 
# explicándole que podría ganar tanta cantidad si fuera experto en Python
salary = float(input('Cuál es tu salario? '))
print(f"Si trabajaras programando en Python ganarías { salary*10 }, es decir,\ndiez veces tu sueldo actual !\n")
print("\n-------------------------------------\n")

#
# Second point
#
# Preguntar al usuario por 2 números. Sumarlos y mostrar el resultado.
n1 = float(input('Dime un número? '))
n2 = float(input('Dime un segundo número? '))
print(f"el resultado de la suma de los números {n1}, {n2} es: {n1+n2}")
print("\n-------------------------------------\n")


#
# Third point
#
# La acción de SANTANDER va cambiando de 3.1453, 2.987 y 3.5. Una aplicación de mainframe 
# con la que compartes datos solo quiere saber el número entero, por ejemplo, 3, 2, 3. 

# integer part of a number
import math  # for math.floor function
numbers = [3.1453, 2.987, 3.5]
numbers_int_part = []
for number in numbers:
  print(f"x value is: {number} and the integer part is: {math.floor(number)}")

for number in numbers:
  numbers_int_part.append(math.floor(number))
print(f"\numbers_int_part: {numbers_int_part}")  
print("\n-------------------------------------\n")


#
# Fourth point
#
# Crear un programa para calcular lo que cada uno tiene que pagar para la cena de una sociedad. 
# Preguntar cuántas personas hay y el precio total de la compra. Por tanto, cada uno tiene que pagar X.
#
cantidad_personas = int(input('Cuántas personas participaron en la comida? '))
costo_total_comida = float(input('Cuál fue el costo total de la comida?'))
print(f"El costo a pagar por cada comensal es: {costo_total_comida/cantidad_personas}")
print("\n-------------------------------------\n")


#
# Fifth point
#
# Crear un programa para convertir tu peso en kilos o en libras. Ya que sabemos usar 
# un comando if, preguntar primero qué acción quiere llevar a cabo 
#(“Teclear “k” si quieres convertir kilos en libras o teclear “l” si quieres convertir libras en kilos”).



#
# Sixth point:

#
# Has visto este código en una página web. 
# Adivinar el tipo de dato que hay un la variable a.
# En otra página, ejecutan la función de esta forma.
# a, b, c = numbers()
# ¿Qué tipo de datos son a, b y c?  
def numbers():
  return 10,20,30
a = numbers()
print(f"function 'numbers' is: {numbers}")  

#a = numbers();
print(f"variable 'a' is: {numbers}") 
print(f"el primer valor de numbers() es: {numbers()[0]} ") 
print(f"el primer valor de a() es: {a[0]} ") 
print(f"el tercer valor de a() es: {a[2]} ") 

# LINK other NB
# https://colab.research.google.com/drive/1GQpgR3_hRVnqp4RvlmHVRxHuYctFDTMC#scrollTo=MirIqfeMqfe5&line=41&uniqifier=1


