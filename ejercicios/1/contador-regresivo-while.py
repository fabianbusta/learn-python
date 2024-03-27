numero = int(input("Introduce un número entero positivo: "))

# Controlar error si número no es entero.
if numero < 0:
    print("Por favor, introduce un número entero positivo.")
else:
    print("Contador regresivo desde", numero, "hasta 0:")
    while numero >= 0:
        # Si la condición se cumple
        print(f"n: {numero}")
        
        # Restar número al contador
        numero -= 1