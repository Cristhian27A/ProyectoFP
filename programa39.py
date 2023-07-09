def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

area = calcular_area_triangulo(base, altura)
print(f"El area de un triangulo es de {area}")
