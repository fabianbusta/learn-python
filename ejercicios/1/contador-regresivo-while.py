numero = int(input("Introduce un número entero positivo: "))

if numero < 0:
    print("Por favor, introduce un número entero positivo.")
else:
    print(f"Contador regresivo desde {numero} hasta 0:")
    while numero >= 0:
        print(numero)
        numero -= 1