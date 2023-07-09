print("programa 12. \nInteres a pagar por un prestamo ")
monto = float(input("Ingrese el monto "))
tasa = float(input("Ingrese la tasa "))
plazo = float(input("Ingrese el plazo a pagar "))
tasa_Porcentaje = tasa * 100
tasa_Mensual = tasa / 12
cuota = monto * (tasa_Mensual / (1 -(1 + tasa_Mensual)**(- plazo)))
interes_Mensual = monto * tasa_Mensual
capital_Mensual = cuota - interes_Mensual

print(f"La cuota es de {round(cuota,2)} \nEl interes mensual es de {round(interes_Mensual,2)} \nLa capital mensual es de {round(capital_Mensual,2)} ")
