#!/usr/bin/python3
#
#  Class and objects examples
#			https://www.w3schools.com/python/python_classes.asp
#

# Funcion para detallar objetos
def mostrar(mens,obj):
	print(mens, obj, ' | tipo ', type(obj), ' | memDir es ', id(obj))

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

p1 = Person("John Gainzarain", 36)
p2 = Person("Ametza Browfield", 11)

print('Descripción variables'), print()

mostrar('Person es -> ',Person), print()
mostrar('Number of objects -> ',Person.num_of_obj), print()
mostrar('Age average -> ',Person.age_Sum/Person.num_of_obj), print()

#
# funciones vars(),dir() -> https://stackoverflow.com/questions/5969806/print-all-properties-of-a-python-class
#

mostrar('p1 es ',p1)
mostrar('Propiedades p1 ',vars(p1)), print()
mostrar('p2 es ',p2)
mostrar('Propiedades p2 ',vars(p2)), print()

# Filtrando atributos y métodos
attributes = [attr for attr in dir(p1)
              if not attr.startswith('__')]
print('Properties and Methods list using dir() with filter ->' ,attributes), print()

#
# https://github.com/symonsoft/ppretty
# print ppretty(p1(), seq_length=10), print()
#
#
# list of an atribute values of the objects in a class
#     https://stackoverflow.com/questions/3182183/creating-a-list-of-objects-in-python
# 
names_List=[]
age_List=[]
print('\nProperties of the objects')
for thisObj in Person.myInstances:
	names_List.append(thisObj.name)
	age_List.append(thisObj.age)
	print('object-> ',thisObj,' | properties ',vars(thisObj))
	  
print()
mostrar('Name list-> ',names_List)
mostrar('Age list -> ',age_List)
print()
#help(Person)
i=1
print('Method list\n')
# print('Methods List -> ',dir(Person))
for method in dir(Person):
	print('method {0:3d}-> | {1: <20} '.format(i,method))
	i+=1
# print('dir of Class -> ',dir(Person))
