numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("El número ingresado no es positivo.")
else:
    factorial = 1
    contador = 1
    
    while contador <= numero:
        factorial *= contador
        contador += 1
    
    print(f"El factorial de {numero} es: {factorial}")