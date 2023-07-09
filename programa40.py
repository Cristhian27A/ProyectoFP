def hallar_el_perimetro_de_un_rectangulo(AB, BC, CD, DA):
    P = AB + BC + CD + DA
    return P
    
AB=  float(input("Ingrese el valor de AB: "))
BC=  float(input("Ingrese el valor de BC: "))
CD=  float(input("Ingrese el valor de CD: "))
DA=  float(input("Ingrese el valor de DA: "))

P = hallar_el_perimetro_de_un_rectangulo(AB, BC, CD, DA)
print(f"el perimetro del rectangulo es de {P} ")

print("\nFin del programa 40")