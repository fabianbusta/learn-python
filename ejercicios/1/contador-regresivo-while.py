contador = int(input("Introduce un número entero positivo: "))

if contador < 0:
    print("Por favor, introduce un número entero positivo.")
else:
    print(f"Contador regresivo desde {contador} hasta 0:")
    while contador >= 0:
        print(contador)
        contador -= 1