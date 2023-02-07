#!/usr/bin/python3

import csv
import sys
import sqlite3

# Archivo con la DB
arch_db = 'CoronaVirus.db'


#
# Conectandome a SQlite3
#
try:
	# Conexion a la DB pasandole el nombre del archivo
	conexion = sqlite3.connect(arch_db)
	
	# Objeto para interactuar con la DB
	cursor = conexion.cursor()
	
	# Consulta
	consulta = """select * from pais where id_cont = ?"""
	
	# Ejecuto la consulta
	cursor.execute(consulta, (2,) )
	
	# Obtengo los resultados
	resultados = cursor.fetchall()

except sqlite3.Error as error:
	print("Consulta Fallida: ", error)	
except Exception as error:
	print("Error General: ", error)	
finally:
	# Cierro la conexion a la DB si existe
	if (conexion):
		conexion.close()


#
# Manejo el resultado
#

# Presento los resultados
for fila in resultados:
	print(fila)
