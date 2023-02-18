#!/usr/bin/python3

import csv
import mis_cosas as mc
import sys
import matplotlib as ml
import matplotlib.pyplot as plt


# mc.ver_elementos(csv)

nombre_archivo=sys.argv[1]
nombre_pais=sys.argv[2]
lineas_pagina=30

def pausar():
	userInput = input('Presiona ENTER para continuar CTRL-C para salir. ')

campos = []
filas = []
xData = []
yData = []

filas_filtradas = []

with open(nombre_archivo, 'r') as archivo_csv:
	# Creo Objeto csv reader
	lector_csv = csv.reader(archivo_csv)

	campos = next(lector_csv)

	for fila in lector_csv:
		if nombre_pais in fila:
			filas.append([fila[1], fila[4]])
			xData.append(fila[1])
			yData.append(fila[4])

	print(f'Total Filas: {lector_csv.line_num}')


print(f'Numero de filas filtradas {len(filas)}')
# print(f'{filas}')
print(f'{yData}')

# Generar Grafico
imagen_destino = nombre_pais + '.png'

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_title('graph')

# plot dates in x axis

#   https://kite.com/python/answers/how-to-plot-dates-on-the-x-axis-of-a-matplotlib-plot-in-python
#  https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/date.html
# x_values = [datetime.datetime.strptime(d,"%m/%d/%Y").date() for d in xData

#  https://stackoverflow.com/questions/9627686/plotting-dates-on-the-x-axis-with-pythons-matplotlib



ax.set_xlabel('Fecha',rotation=0)
ax.set_ylabel('N.Deaths')

# plt.grid(True)
plt.axis([0,200,0,1000])
plt.plot(yData,'k-',color='k')

# plt.savefig(imagen_destino)

plt.show()
