print("programa 13. \nCalcular salario neto de empleados  ")

salario_bruto = float(input("Ingrese el salario bruto "))
ssocial = salario_bruto * 0.05
seducativo = salario_bruto * 0.02
cprestamo = 50
salario_Neto = salario_bruto - ssocial - seducativo - cprestamo

print("El salario neto a pagar es de:",salario_Neto)