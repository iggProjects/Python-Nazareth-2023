# probando la sentencia "from file import function"


# colors for text in windows : https://www.codeproject.com/Tips/5255355/How-to-Put-Color-on-Windows-Console

def Purple(mens): print("\033[95m{}\033[00m\n" .format(mens)) 
def Yellow(mens): print("\033[93m{}\033[00m\n" .format(mens)) 

# https://www.geeksforgeeks.org/print-colors-python-terminal/
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


#from MyFunctions import mostrar
# import My_Functions
### FUNCTIONS

# Funcion para detallar objetos
def mostrar(obj):
		print("\tVariable: ", obj, "es", type(obj), "\n\tmemDir  : ", id(obj))
		attributes = [attr for attr in dir(obj) 
			if not attr.startswith('__')]
		print('\tProperties & Methods ->' ,attributes, '\n')
	
def ver_objetos(obj):
	enum=1
	si_color='\033[0;91m'
	no_color='\033[0m'
	print(si_color + 'TIPO:' + no_color, str(type(obj)) , '\n')
	for elemento in dir(obj):
		ver='obj.' + elemento
		print(str(si_color + 'Elemento: ' + str(enum) + ' ' + no_color + ver))
		if 'method' in str(eval(ver)):
			print('\tMetodo --> ', eval(ver))
		else:
			print('\tAtribu --> ', eval(ver))
			print('\tTipo --> ', type(eval(ver)), '\n')
		enum=enum+1
