print("Programa 18. \nCalculo del interes compuesto ")

Ci = float(input("Ingrese la capital inicial "))
i = float(input("Ingrese la tasa de interes "))
n = float(input("Ingrese el periodo de ahorro "))

Cf = Ci * (1 + i) ** n

print(f"La capital final es de {round(Cf,2)} ")