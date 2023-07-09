print("Programa 19. \nCompra de 5 articulos ")

art1 = float(input("Ingrese el precio del primer articulo "))
art2 = float(input("Ingrese el precio del segundo articulo "))
art3 = float(input("Ingrese el precio del tercer articulo "))
art4 = float(input("Ingrese el precio del cuarto articulo "))
art5 = float(input("Ingrese el precio del quinto articulo "))
compra_sin_impuesto = art1 + art2 + art3 + art4 + art5
impuesto = compra_sin_impuesto * 0.07
compra_con_impuesto = impuesto + compra_sin_impuesto
promedio = compra_sin_impuesto / 5

print(f"La compra sin impuestos es de {round(compra_sin_impuesto,2)} Balboas \nLa compra con impuesto es de {round(compra_con_impuesto,2)} Balboas \nEl promedio de la compra es {round(promedio,2)} Balboas ")