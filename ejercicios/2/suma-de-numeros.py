suma_total = 0

print("Ingresa una serie de números enteros. Para detener la suma, ingresa 0.")
while True:
    numero = int(input("Ingresa un número entero: "))
    
    if numero < 0:
        print("Por favor, introduce un número entero positivo.")
    else:
        if numero == 0:
            break
        
        suma_total += numero
    
print(f"La suma de los números ingresados es: {suma_total}")