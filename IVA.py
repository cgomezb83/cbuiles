def promedioLista(*lista):
	contador=0
	for i in lista:
		contador+=i

	return contador/len(lista)


lista=[2,2,2,2]

print(promedioLista(lista))

print(sum(lista))

