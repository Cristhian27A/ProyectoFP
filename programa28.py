print("Programa 28. \nEvaluacion de una calificacion ")

calificacion = float(input("Ingrese la calificacion: "))

if calificacion >= 90 and calificacion <= 100:
    print("Su calificacion es A")
elif calificacion >= 80 and calificacion < 90:
    print("Su calificacion es B")
elif calificacion >= 70 and calificacion < 80:
    print("Su calificacion es C")
elif calificacion >= 60 and calificacion < 70:
    print("Su calificacion es D")    
else:
    print("F") 

print("\nFin del programa")            