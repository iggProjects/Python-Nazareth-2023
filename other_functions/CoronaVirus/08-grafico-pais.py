#!/usr/bin/python3

import csv
import sys, traceback
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
	consulta = """ select 
								   c.id_pais, p.nombre_iso, p.alpha_3, date(c.fecha,'unixepoch'), 
									 c.nuevos, c.muertes, c.total_nuevos, c.total_muertes 
								 from casos as c, pais as p 
								 where c.id_pais = ? and c.id_pais = p.id """
	
	# Ejecuto la consulta
	cursor.execute(consulta, (100,) )
	
	# Obtengo los resultados
	resultados = cursor.fetchall()

except sqlite3.Error as error:
	print("Consulta Fallida: ", error)	
	traceback.print_exc()
except Exception as error:
	print("Error General: ", error)	
	traceback.print_exc()
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
