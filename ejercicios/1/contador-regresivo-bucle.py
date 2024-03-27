numero = int(input("Introduce un número entero positivo: "))

if numero < 0:
    print("Por favor, introduce un número entero positivo.")
else:
    print("Contador regresivo desde", numero, "hasta 0:")
    for i in range(numero, -1, -1):
        print(i)