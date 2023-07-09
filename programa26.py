print("Programa 26. \nClasificacion de triangulos ")
lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

if lado1 == lado2 and lado2 == lado3:
    print("Es un triangulo equilatero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Es un triangulo isoceles")
else:
    print("Es un triangulo escaleno")    

print("\nFin del programa")        