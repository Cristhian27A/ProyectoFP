calificaciones = int(input("Ingrese el numero de calificaciones a evaluar: "))

for i in range(calificaciones):
    calificacion = float(input("Ingrese la calificacion: "))

    if calificacion >= 90 and calificacion <= 100:
        letra = 'Su evaluacion es A'
    elif calificacion >= 80 and calificacion <= 89:
        letra = 'Su evaluacion es B'
    elif calificacion >= 70 and calificacion <= 79:
        letra = 'Su evaluacion es C'
    elif calificacion >= 60 and calificacion <= 69: 
        letra = 'Su evaluacion es D'
    else:
        letra = 'Su evaluacion es F' 

    print(f"La calificacion es {letra}")           