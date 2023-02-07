#!/usr/bin/python3

import sys, traceback
import sqlite3
import matplotlib.pyplot as plt

# Archivo con la DB
arch_db = 'CoronaVirus.db'

#
# Listas para graficos
#
pais = ''
alpha_3 = ''
x_fecha = []
y_nuevos = []
y_muertes = []
y_total = []
y_total_muertes = []

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
	for resultado in cursor.execute(consulta, (200,) ):
		if not alpha_3:
			alpha_3 = resultado[2]
		if not pais:
			pais = resultado[1].replace(' ', '_')
			print(pais)
		x_fecha.append(resultado[3])
		y_nuevos.append(resultado[4])
		y_muertes.append(resultado[5])
		y_total.append(resultado[6])
		y_total_muertes.append(resultado[7])
	
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


# Graficos
archivo = alpha_3+'_'+pais+'_casos.png'
archivo_total = alpha_3+'_'+pais+'_casos_total.png'

# Graficos Nuevos
fig, grafico = plt.subplots()
grafico.plot(x_fecha, y_nuevos, label='Casos')
grafico.plot(x_fecha, y_muertes, label='Muertes')
plt.xlabel('Fechas')
plt.ylabel('Casos')
plt.title(pais+' -> '+alpha_3+' -> Nuevos')
grafico.legend()
plt.savefig(archivo, dpi=150)

# Graficos Totales
fig, grafico = plt.subplots()
grafico.plot(x_fecha, y_total, label='Casos')
grafico.plot(x_fecha, y_total_muertes, label='Muertes')
plt.xlabel('Fechas')
plt.ylabel('Casos')
plt.title(pais+' -> '+alpha_3+' -> Totales')
grafico.legend()
plt.savefig(archivo_total, dpi=150)
