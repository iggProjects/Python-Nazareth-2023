#!/usr/bin/python3

def Purple(mens): print("\033[95m{}\033[00m\n" .format(mens)) 
def Yellow(mens): print("\033[93m{}\033[00m\n" .format(mens)) 

# Funcion para detallar objetos
def mostrar(obj):
		print("\tVariable: ", obj, "es", type(obj), "\n\tmemDir  : ", id(obj))
		attributes = [attr for attr in dir(obj) 
			if not attr.startswith('__')]
		print('\tProperties & Methods ->' ,attributes, '\n')


# Variables algebraicas
Purple('\ntype algebraicas')

# Entero
variable=1
mostrar(variable)

# Punto Flotante
variable=23/2
mostrar(variable)

# Imaginarios / Complejos
variable=1+2j
mostrar(variable)

# Cadena
Purple('type string')
variable='Hola Inaki'
mostrar(variable)
variable="Epale Gainzarain, que estas haciendo?"
mostrar(variable[3:15])
mostrar( len(variable))
mostrar(variable[-3])

# Tuplas
Purple('type tuplas')
variable=(1,4,'Hola', 2.4, 2-7j,[1,2,3,4,5,6,7,8,9])
mostrar(variable)
mostrar(variable[5][3])

variable[5][0]=3.5
#variable[4]=[3,67]
mostrar(variable[5])
mostrar(variable)

variable1=(2,5,'ziggy',3.4,2+7j)
variable3=variable+variable1
mostrar(variable3)


# Lista
Purple('type list')
variable=[1,4,'Hola', 2.4, 2-7j]
mostrar(variable)
mostrar(variable[3])
variable[3]=3.5
mostrar(variable[3])
mostrar(variable)
variable1=[2,5,'ziggy',3.4,2+7j]
variable3=variable[4]-variable1[4]
mostrar(variable[-5])


# Booleanos
Purple('type boolean')
variable=True
mostrar(variable)

# Diccionarios
Purple('type dictionary')
variable={'uno':'UNO','dos':2+6j}
mostrar(variable)
mostrar(variable['dos'])
variable['dos']=5
mostrar(variable)

# SETS
Purple('type sets')




# CLASS
Purple('type CLASS')

class Person:
	num_of_obj=0
	myInstances=[]
	age_Sum=0
	def __init__(self, name, age):
		self.name = name
		self.age = age
		Person.num_of_obj += 1
		self.__class__.myInstances.append(self)
		Person.age_Sum += self.age

Yellow('\tClass Person') 
mostrar(Person)

p1 = Person("John Gainzarain", 36)
p2 = Person("Ametza Browfield", 11)

Yellow('\tObject 1')
mostrar(p1)
mostrar(vars(p1))
Yellow('\tObject 2')
mostrar(p2)
mostrar(vars(p2))

Yellow('\tNumber of objects')
mostrar(Person.num_of_obj)
Yellow('\tAge average objects')
mostrar(Person.age_Sum/Person.num_of_obj)

names_List=[]
age_List=[]
Yellow('\tProperties of the objects')
for thisObj in Person.myInstances:
  names_List.append(thisObj.name)
  age_List.append(thisObj.age)
print('\tobject-> ',thisObj,' | properties "vars function" ',vars(thisObj),'\n')

Yellow('\tList of names')
mostrar(names_List)
Yellow('\tList of ages')
mostrar(age_List)

i=1
Yellow('\tMethod list of Class Person')
# print('Methods List -> ',dir(Person))
for method in dir(Person):
  print('\tmethod {0:3d}:  {1: <20} '.format(i,method))
  i+=1
print()
Yellow('\tAttribute list of Class Person')
i=1
for attr in dir(Person):
	print('\tattribute {0:3d}: {1: <20} '.format(i,attr))
	i+=1

#
# https://www.geeksforgeeks.org/print-colors-python-terminal/
#
# Python program to print 
# colored text and background 
def prRed(skk): print("\033[91m{}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m{}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m{}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m{}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m{}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m{}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m{}\033[00m" .format(skk)) 

print('\nCOLORS') 
prCyan("\tHello World, ") 
prYellow("\tIt's") 
prGreen("\tGeeks") 
prRed("\tFor") 
prPurple("\tGeeks") 


