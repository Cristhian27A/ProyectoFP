print("programa 15. \nCompra de tres articulo ")
Articulo1 = float(input("Ingrese el precio del primer articulo "))
Articulo2 = float(input("Ingrese el precio del segundo articulo "))
Articulo3 = float(input("Ingrese el precio del tercer articulo "))
precio = Articulo1 + Articulo2 + Articulo3
impuesto = precio * 0.07
compra_total = precio + impuesto

print(f"La compra total es de {round(compra_total,2)} ")