from PIL import Image
import pywt
import numpy as np

import matplotlib.pyplot as plt
import os

def filtroGrisesPromedio(imagen):
	x, y = imagen.size
	px = imagen.load()
	imagenGrises = Image.new('RGB',(x,y))
	for i in range(x):
		for j in range(y):
			pixeles = px[i,j]
			prom = sum(pixeles) / 3
			imagenGrises.putpixel((i,j),(prom,prom,prom))
	return imagenGrises

def generarMatriz(imagen):
	x,y = imagen.size
	p = imagen.load()
	matriz = list()
	for j in range(y):
		fila = list()
		for i in range(x):
			fila.append(p[i,j][0])
		matriz.append(fila)
	n_array = np.array(matriz)
	return n_array

def wavelet(array, umbral):
	mu = -umbral
	#se crea el objeto de la funcion
	w = pywt.Wavelet('haar')
	#obtenemos los coheficientes al aplicar la transformada haar en el
	#array de valores de grises, nivel 2 para una capa
	coe = pywt.wavedec2(array, w, level=2)
	#se obtienen los coheficientes
	v1, v2, coheficientes = coe
	#print "VALOR 1 coe:",type(v1),v1
	#print "_______________________________________________________________________________________________________________________________"
	#print "VALOR 2 coe:",type(v2),v2
	#print "_______________________________________________________________________________________________________________________________"
	#print "VALOR 3 coe: ",type(coheficientes), coheficientes
	#print "_______________________________________________________________________________________________________________________________"
	#transformada inversa sobre los valores modificados
	listaNva=list()
	for m in coheficientes:
		#cada m es un arreglo de detalle

		#pintar los valores originales
		plt.plot(m)
		plt.show()
		#Para comprimir, se remplazan todos los valores que caen 
		#dentro de un umbral a cero
		#Se crea una lista mueva de coeheficientes, la modificacion en base a umbral se hace para la 
		#matriz de regresion (coheficientes)
		nva = np.where(((m<mu) | (m>umbral)), m, 0)

		#pintar los resultados
		plt.plot(nva)
		plt.show()
		#listaNva sera el remplazo del factor coheficientes
		listaNva.append(nva)
	fn = list()
	fn.append(v1)
	fn.append(v2)
	fn.append(tuple(listaNva))
	#fn es la lista de nuevos coheficientes
	#transformada inversa sobre los valores modificados
	t = pywt.waverec2(fn, 'haar')
	# A enteros
	b = t.astype(int)
	#regresamos la matriz
	return b

def generaImagen(a, size):
	ancho,largo = size
	t = list()
	for e in a:
		fila = list()
		for valor in e:
			fila.append((int(valor),int(valor),int(valor)))
		t.append(fila)

	nueva = Image.new('RGB',(ancho,largo))
	for j in range(largo):
		for i in range(ancho):
			nueva.putpixel((i,j),t[j][i])
	nueva.save("salida.png")
	return nueva

def evaluacion(umbral):
	print "RESULTADOS"
	print "Valor umbral utilizado: ", umbral
	t_original = int(os.stat("test.png").st_size)
	t_gris = int(os.stat("gris.png").st_size)
	t_final = int(os.stat("salida.png").st_size)
	print "Peso de la imagen original: ", t_original,"bytes."
	print "Peso de la imagen final:    ", t_final, "bytes."
	porcentaje = ( t_final * 100 ) / float(t_original)
	print "Imagen compresa en un ", 100 - porcentaje, "%."  
	print ""
	o = Image.open("salida.png")
	o.show()

def proceso(umbral):
	imagen = Image.open('test.png').convert('RGB')
	gris = filtroGrisesPromedio(imagen)
	gris.save("gris.png")
	array = generarMatriz(gris)
	inversa = wavelet(array, umbral)
	im = generaImagen(inversa, imagen.size)
	evaluacion(umbral)

def main():

	#ejecutando del proceso con diferentes umbrales
	proceso(10)
	proceso(50)
	proceso(100)
main()