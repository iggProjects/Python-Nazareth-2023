#!/usr/bin/python3

import csv
import mis_cosas as mc
import sys

# mc.ver_elementos(csv)

nombre_archivo=sys.argv[1]
nombre_pais=sys.argv[2]
lineas_pagina=30

def pausar():
	userInput = input('Presiona ENTER para continuar CTRL-C para salir. ')

campos = []
filas = []
filas_filtradas = []

with open(nombre_archivo, 'r') as archivo_csv:
	# Creo Objeto csv reader
	lector_csv = csv.reader(archivo_csv)

	campos = next(lector_csv)

	for fila in lector_csv:
		if nombre_pais in fila:
			filas.append(fila)

	print(f'Total Filas: {lector_csv.line_num}')


print(f'Numero de filas filtradas {len(filas)}')

# Escribo lista filtrada en un CSV nuevo
nombre_destino = nombre_pais + '.csv'

with open(nombre_destino, 'w') as destino_csv:
	escritor_csv = csv.writer(destino_csv)

	escritor_csv.writerow(campos)
	for fila in filas:
		escritor_csv.writerow(fila)


