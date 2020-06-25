#Genera una lista con las letras del diccionario por medio de ASCII
def generar_diccionario():

    diccionario=[]

    for i in range(97,123):

        diccionario.append(chr(i))

    return diccionario

#Funcion que recibe el diccionario  y  la cadena ingresada por consola
def contador_diccionario(cadena,diccionario):

    resultados_diccionario={}
    
    for letra_diccionario in diccionario:
        contador=0
        for letra_cadena in cadena:

            if letra_cadena==letra_diccionario:
                contador=contador+1

        resultados_diccionario[letra_diccionario]=contador

    print(resultados_diccionario)


#---------------------------------------EJECUCION DEL PROGRAMA-------------------------
cadena=input("Ingrese cadena de caracteres").lower()

diccionario=generar_diccionario()

contador_diccionario(cadena,diccionario)

