#!/usr/bin/python3

import csv
import mis_cosas as mc
import sys

# mc.ver_elementos(csv)

nombre_archivo=sys.argv[1]
lineas_pagina=30

def pausar():
	userInput = input('Presiona ENTER para continuar CTRL-C para salir. ')

campos = []
filas = []

with open(nombre_archivo, 'r') as archivo_csv:
	# Creo Objeto csv reader
	lector_csv = csv.reader(archivo_csv)

	campos = next(lector_csv)

	for fila in lector_csv:
		filas.append(fila)

	print(f'Total Filas: {lector_csv.line_num}')

linea_inicio=0
linea_fin=lineas_pagina

while linea_inicio <= len(filas):
	# Presento Titulo de Columnas
	for col in campos:
		print('%14s'%col, end="")
	print()
	
	for fila in filas[linea_inicio:(linea_inicio+lineas_pagina)]:
		for col in fila:
			print('%14s'%col[:5], end="")
		print()
	linea_inicio+=lineas_pagina
	pausar()
	print()
