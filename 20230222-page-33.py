"""
    FUNCTIOSN FOR TEXTS  (page 33)
    1.- Usando replace(), cambiar es texto para que sea correcto. Además, usar el nombre original de “Python” en lugar de Píton.

    2.- Usar swapcase, replace, upper, in, count, find, strip
"""
# IMPORT
import MyFunctions.Colors as Col

# first case 
# function -> replace()
texto = "Pitón es un lenguaje de programación. Pitón está usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón fue creado por Bill Gates en 1960. Pitón es difícil de usar."

texto=texto.replace('Pitón','Python')
texto=texto.replace('Bill Gates en 1960','Guido Van Rossum en 1989')
texto=texto.replace('es difícil','es fácil')

print(texto)

# second case
# functions -> swapcase, replace, upper, in, count, find, strip
texto = "    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. Cuando contratamos nuevos empleados. Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil        "

#Contar las veces que la palabra Python aparece en el texto...y si a veces aparece en el texto con mayusculas y minusculas - Python, python
print(Col.frGREEN(f"occurrences of the word 'Python': {texto.count('Python')}\n"))

#Encuentras la ubicación (numero de carácter) donde esta la primera ocurrencia de la palabra Python. ¿Y la segunda?
print(Col.frGREEN(f"First occurrence of python -> {texto.find('Python')}"))
print(Col.frGREEN(f"Second occurrence of python -> {texto.find('Python',texto.find('Python')+1)}\n"))

#La palabra 'código' esta en el texto? Usar if ... in ...:
if texto.find('codigo') > -1:
    print(Col.frGREEN(f"La palabra 'código' SI está en el texto,\n   y empieaza en la posición {texto.find('código')} 👌\n"))
else: 
    print(Col.frRED(f"La palabra 'código' NO está en el texto 😢\n"))

#Reemplazar Python por PYTHON
texto = texto.replace('Python','\033[92mPYTHON\033[00m')
print(texto + '\n')

#Quitar los espacios
texto = texto.strip()
print(texto + '\n')

#Cambiar la letra de todo el texto a "lO MÁS IMPORTANTE QUE NOS HA MANTENIDO EN pYTHON... "
texto = texto.swapcase()
print(texto + '\n')




