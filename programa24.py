print("Programa 24. \nIdentificador de un numero mayor")
n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
n3 = float(input("Ingrese el tercer numero: "))

if n1 > n2 and n1 > n3:
    print(f"El numero {n1} es el mayor ")
elif n2 > n1 and n2 > n3:
    print(f"El numero {n2} es el mayor ")
if n3 > n1 and n3 > n2:
    print(f"El numero {n3} es el mayor ")        

print("\nFin del programa")    