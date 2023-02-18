#!/usr/bin/python3

def Purple(mens): print("\033[95m{}\033[00m\n" .format(mens))
def Yellow(mens): print("\033[93m{}\033[00m" .format(mens))

# Funcion para detallar objetos
def mostrar(obj):

		Yellow('\nVARIABLE')
		print("   -- La variable ", obj, "es", type(obj), "y su dir mem: ", id(obj))

		# crear variable texro que recoja los valores de arriba, y luego presentarlos con Purple 
		# Purple(texto_variable))
		
		attributes = [
			attr for attr in dir(obj) if not attr.startswith('__')
		]
		
		Purple('\nProperties & Methods, dir() with filter __ ')
		print(attributes)
		print('')


# Variables algebraicas
print('\nVariables type algebraicas\n')
# Entero
variable=1
mostrar(variable)

# Punto Flotante
variable=23/2
mostrar(variable)

# Imaginarios / Complejos
variable=1+2j
mostrar(variable)

print('Variable type string\n')
# Cadena
variable='Hola Inaki'
mostrar(variable)
variable="Epale Gainzarain, que estas haciendo?"
mostrar(variable[3:15])
mostrar( len(variable))
mostrar(variable[-3])

print('Variable type tupla\n')
# Tuplas
variable=(1,4,'Hola', 2.4, 2-7j,[1,2,3,4,5,6,7,8,9])
mostrar(variable)
mostrar(variable[5][3])

variable[5][0]=3.5
#variable[5]=[3,67]
mostrar(variable[5])
mostrar(variable)

variable1=(2,5,'ziggy',3.4,2+7j)
variable3=variable+variable1
mostrar(variable3)


print('Variable type list\n')
# Lista
variable=[1,4,'Hola', 2.4, 2-7j]
mostrar(variable)
mostrar(variable[3])
variable[3]=3.5
mostrar(variable[3])
mostrar(variable)
variable1=[2,5,'ziggy',3.4,2+7j]
variable3=variable[4]-variable1[4]
mostrar(variable[-5])


print('Variable type boolean\n')
# Booleanos
variable=True
mostrar(variable)

# Diccionarios
variable={'uno':'UNO','dos':2+6j}
mostrar(variable)
mostrar(variable['dos'])
variable['dos']=5
mostrar(variable)

# Faltan los SETS
