print("Programa 20. \nCalculo del salario neto de empleados ")

Salario_bruto = float(input("Ingrese el salario bruto "))
Seguro_social = Salario_bruto * 0.08
Seguro_educativo = Salario_bruto * 0.02
impuesto = Salario_bruto * 0.15
prestamo = 100
Salario_Neto = Salario_bruto - Seguro_social - Seguro_educativo - impuesto - prestamo

print(f"El salario neto a pagar es de {round(Salario_Neto,2)} Balboas")