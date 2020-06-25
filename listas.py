facturas={}

accion=""

cobro=0
deuda=0
while accion!="3":
	accion=int(input("Que desear hacer con las facturas : \n1.Agregar\n2.Pagar\n3.Terminar\n"))

	if accion==1:

		n_factura=input("Ingrese el numero de factura: ")
		v_factura=input("Valor de la factura: ")
		facturas[n_factura]=v_factura
		print("Se ha agregado al diccionario")

	elif accion==2:

		n_pagar=input("Ingrese factura a pagar: ")

		cobro=cobro+int(facturas[n_pagar])
		facturas.pop(n_pagar)

		print("Ha sido borrado esta factura")

		
	elif accion==3:
		break

	else:

		print("Valor ingresado es incorrecto")

	for i in facturas:
		deuda=deuda+int(facturas[i])

	deuda=int(deuda)-int(cobro)

	print("Se cobro: $", cobro)
	print("Se debe : $",deuda)