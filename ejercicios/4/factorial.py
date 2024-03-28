numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("El número ingresado no es positivo")
else:
    factorial = 1
    i = 1
    
    while i <= numero:
        factorial *= i
        i += 1
    
    print("El factorial de", numero, "es: ", factorial)