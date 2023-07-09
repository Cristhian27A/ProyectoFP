value = 0
while value <= 5:
    C = float(input("Ingrese la calificacion: "))
    if 90 <= C <= 100:
        print("La evaluacion es A")
    elif 80 <= C <= 89:
        print("La evaluacion es B")    
    elif 70 <= C <= 79:
        print("La evaluacion es C")
    elif 60 <= C <= 69:
        print("La evaluacion es D") 
    else:
        print("La evaluacion es F")   