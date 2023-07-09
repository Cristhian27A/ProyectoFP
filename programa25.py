print("Programa 25. \nCalculadora de descuento ")

producto = float(input("Ingrese el precio del producto: "))
d = float(input("Ingrese el descuento: "))
p = d / 100
descuento = producto * p
porciento = producto - descuento

if producto >= 50:
    print(f"El total de la compra con el descuento incluido es de {round(porciento,2)} Balboas ")
else:
    print("Oferta especial") 

print("\nFin del programa")