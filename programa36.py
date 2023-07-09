print("Programa 36. \nLista de numeros ")

numeros = list(range(1,11))

for numero in numeros:
    if numero > 5:
        print(f"El numero {numero} es mayor ")
    elif numero <= 0:
        print(f"El numero {numero} es menor o igual a cero")
    else:
        print(f"El numero {numero} es menor")

    if numero == 9:
        break    

print("\nFin del programa")