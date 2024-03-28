numero = int(input("Ingresa un número entero positivo: "))

suma = 0
contador = 1

while contador <= numero:
    if contador % 2 == 0:
        suma += contador
    contador += 1
    
print(f"La suma de todos los números pares hasta {numero} es: {suma}")