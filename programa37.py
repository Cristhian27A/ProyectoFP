print("Programa 37. \nCaptura de 5 articulos con el 7 porciento ")

total = 0 
articulos = 0

while articulos < 5:
    articulos += 1
    precio = float(input("Ingrese el precio del articulo: "))
    impuesto = precio * 0.07
    compra = articulos + impuesto
    total += compra

print(f"La compra total de los 5 articulos es de {round(total,2)} Balboas")

print("\nFIN DEL PROGRAMA")