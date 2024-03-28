suma = 0

print("Ingresa una serie de números enteros. Para detener la suma, ingresa 0.")
while True:
    num = int(input("Ingresa un número entero: "))
    
    if num < 0:
        print("Por favor, introduce un número entero positivo.")
    else:
        if num == 0:
            break
        
        suma += num
    
print(f"La suma de los números ingresados es: {suma}")