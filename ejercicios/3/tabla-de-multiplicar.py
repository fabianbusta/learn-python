numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("El número ingresado no es positivo.")
else:
    contador = 1

    print(f"Tabla de multiplicar de {numero}")
    while contador <= 10:
        print(f"{numero} x {contador} = {numero*contador}")
        contador += 1