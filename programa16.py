print("programa 16. \nNota final de Juan en la materia ")
evaluacion1 = float(input("Ingrese el valor de la primera evaluacion "))
evaluacion2 = float(input("Ingrese el valor de la segunda evaluacion "))
evaluacion3 = float(input("Ingrese el valor de la tercera evaluacion "))
evaluacion4 = float(input("Ingrese el valor de la cuarta evaluacion "))
evaluacion5 = float(input("Ingrese el valor de la quinta evaluacion "))

p1 = evaluacion1 * 0.2
p2 = evaluacion2 * 0.15
p3 = evaluacion3 * 0.25
p4 = evaluacion4 * 0.1
p5 = evaluacion5 * 0.3
nota = p1 + p2 + p3 + p4 + p5

print(f"La nota final de Juan es {nota} ")