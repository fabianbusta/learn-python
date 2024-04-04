numero = int(input("Ingresa un número entero positivo: "))

if numero > 1:
    divisor = 2
    es_primo = True
    
    while divisor < numero:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1
    
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
else:
    print("Por favor, introduce un número entero positivo")