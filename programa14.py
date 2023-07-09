print("programa 14. \nCompra total de gasolina ")
precio_de_gasolina_de_95 = float(input("Ingrese el precio de la gasolina "))
cantidad_de_litros = float(input("Ingrese la cantidad de litros "))
costo_sin_impuestos = precio_de_gasolina_de_95 * cantidad_de_litros
costo_total = costo_sin_impuestos * 1.07

print(f"El costo total es de {round(costo_total,2)}")