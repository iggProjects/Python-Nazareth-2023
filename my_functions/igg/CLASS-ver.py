#!/usr/bin/python3

# colors
def Purple(mens): print("\033[95m{}\033[00m" .format(mens),end='')
def Yellow(mens,variable): print("\033[93m{}\033[00m" .format(mens),variable,end='')

# function
def mostrar(obj):
	enum=1
	print('TIPO:', type(obj), '\n')
	for elemento in dir(obj):
		ver='obj.' + elemento
		Yellow('Elemento ',enum)
		print(': ', ver)
		# print('Elemento ',enum, ': ', ver)
		if 'method' in str(eval(ver)):
			print('\tMetodo --> ', eval(ver))
		else:
			print('\tAtribu --> ', eval(ver))
		print('\tTipo --> ', type(eval(ver)), '\n')
		enum=enum+1

#########################################################################3

class Persona:
	''' 
		Clase que define a una Persona.

		Atributos:
			nombre ->
			apellido ->
	'''
	def __init__(self, nombre=None, apellido=None, edad=0):
		self.nombre=nombre
		self.apellido=apellido
		# Nombre
		if 'str' not in str(type(nombre)):
			raise Exception('Tipo de dato: NOMBRE')	
		else:
			self.nombre=nombre
		# Apellido
		if 'str' not in str(type(apellido)):
			raise Exception('Tipo de dato: APELLIDO')	
		else:
			self.apellido=apellido
		# Edad
		if 'int' not in str(type(edad)):
			raise Exception('Tipo de dato: EDAD')	
		else:
			self.edad=edad
	def nombreCompleto(self):
		print(self.nombre, self.apellido, '(', self.edad, ')')


try:
	persona=Persona('Iñaki','Gainza',16)
	persona.nombreCompleto()
except Exception as err:
	print('Hubo un error', err)
	print(err.__traceback__)
	print(str(err.__traceback__))
	mostrar(err.__traceback__)
#	mostrar(err.__traceback__.tb_frame)


# mostrar(Exception())

# EJEMPLOS DE OBJETOS
# a=1
# mostrar(a)
