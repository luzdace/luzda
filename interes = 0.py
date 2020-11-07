interes = 0
monto_total_a_pagar = 0
monto = float(input("Ingrese el monto a prestar: "))
tiempo = int(input("Digite el tiempo del crédito: "))
opcionProducto = int(input("""Seleccionar el producto financiero a validar:
1. Crédito Hipotecario
2. Tarjeta Crédito
3. Crédito Libre Inversión
4. Compra de Cartera
\n\n
"""))

if opcionProducto == 1:
    interes = 0.4

elif opcionProducto == 2:
    interes = 2.16

elif opcionProducto == 3:
     interes = 1.5
     
elif opcionProducto == 4:
    interes = 0.8

else:
    print("Opción Invalida...")

monto_inicial = monto
monto_total_a_pagar = monto*((1+(interes/100))**tiempo)

for i in range(tiempo):
    ValorPorIntereses = monto * (interes/100)
    monto = monto + ValorPorIntereses

print("El Interes compuesto es: {0:.2f}".format(monto - monto_inicial), "y el el valor total a pagar es: {0:.2f}".format(monto))
print("El Interes compuesto es: {0:.2f}".format(monto_total_a_pagar - monto_inicial)," y el valor total a pagar es: ""{0:.2f}".format(monto_total_a_pagar))