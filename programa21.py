print("Programa 21. \nCalcular si una persona paga impuestos ")
salario = float(input("Ingrese el salario: "))

if salario > 3000:
    impuesto = salario * 0.07
    print("Debe pagar impuestos",impuesto)
else:
    print("No debe pagar impuestos") 

print("\n Fin del programa")       