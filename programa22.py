print("Programa 22. \nCalculo de temperatura ")

temperatura = float(input("Digite la temperatura: "))

if temperatura < 20:
    if temperatura < 10:
        print("Nivel Azul")
    else: 
        print("Nivel Verde")
else:
    if temperatura < 30:
     print("Nivel Naranja")
    else:
     print("Nivel Rojo")  

print("\nFin del programa")