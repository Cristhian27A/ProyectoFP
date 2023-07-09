# se importan las funciones desde el archivo "funciones.py"
import time
from Funciones_llamar import programa1, programa2, programa3, programa4, programa5, programa6, programa7, programa8, programa9, programa10, programa11, programa12,programa13,programa14,programa15, programa16, programa17, programa18,programa19, programa20, programa21, programa22, programa23, programa24, programa25, programa26, programa27, programa28, programa29, programa30, programa31, programa32, programa33, programa34, programa35, programa36, programa37, programa38, programa39, programa40

# Función para mostrar la animación de un perrito
def mostrar_animacion():
    print("           _ _")
    print("          /^ ^\\")
    print("         / 0 0 \\")
    print("         V\\ Y /V")
    print("          / - \\")
    print("         /    |")
    print("        V__) ||")
    print("     !HASTA PRONTO!  ")

# Mensaje de bienvenida
print("¡Hola, bienvenido! 😎\n")

# Menú de programas
print("Menú de programas:")
print("1. Programa 1: Sucesión de valores")
print("2. Programa 2: Sucesión de variables")
print("3. Programa 3: Promedio de tres números")
print("4. Programa 4: Cálculo del área de un triángulo")
print("5. Programa 5: Cálculo del perímetro de un rectángulo")
print("6. Programa 6: Cálculo del área de un trapecio")
print("7. Programa 7: Cálculo del volumen de un prisma")
print("8. Programa 8: Resolución de ecuaciones")
print("9. Programa 9: Resolución de ecuaciones")
print("10. Programa 10: Conversión de unidades")
print("11. Programa 11: Regla de tres simple")
print("12. Programa 12: Interes a pagar por un prestamo")
print("13. Programa 13: Calculo del salario Neto a empleados")
print("14. Programa 14: Compra total de gasolina")
print("15. Programa 15: Compra de tres articulos")
print("16. Programa 16: Nota final de Juan en la materia")
print("17. Programa 17: Conversion de unidades de medidas")
print("18. Programa 18: Calculo del interes compuesto")
print("19. Programa 19: Compra de 5 articulos")
print("20. Programa 20: Calculo del salario de empleados")
print("21. Programa 21: Calcular si una persona paga impuestos")
print("22. Programa 22: Calculo de temperatura")
print("23. Programa 23: Calcular la edad")
print("24. Programa 24: Identificador de un numero mayor")
print("25. Programa 25: Calculadora de descuento")
print("26. Programa 26: Clasificacion de triangulos")
print("27. Programa 27: Identificador de un numero")
print("28. Programa 28: Evaluacion de una clasificacion")
print("29. Programa 29: Identificacion de notas utilizando Bucles")
print("30. Programa 30: Identificador de un numero utilizando Bucles")
print("31. Programa 31: Aumento de numero hasta 10")
print("32. Programa 32: Determinacion de una nota usando for")
print("33. Programa 33: Tablas de multiplicacion")
print("34. Programa 34: Muestra de numeros pares e impares")
print("35. Programa 35: Numeros del 1 al 15")
print("36. Programa 36: Lista de numeros mayores, menores o menores o iguales a cero")
print("37. Programa 37: Compra de 5 articulos usando Bucles")
print("38. Programa 38: Funcion para sumar numeros pares hasta el 20")
print("39. Programa 39: Definido como funcion para hallar el area de un triangulo")
print("40. Programa 40: Programa a funcion")



# Bucle principal
while True:
    opcion = input("\nIngrese el número del programa que desea ejecutar (o 'salir' para terminar): ")

    if opcion == "salir":
        break
    elif opcion == "1":
        resultado = programa1()
        print(f"La sucesion de valores de a, b y c es:{resultado} ")
    elif opcion == "2":
        resultado = programa2()  
        print(f"Los valores de a, b y aux son: {resultado}")  
    elif opcion == "3":
        resultado = programa3()
        print(f"El resultado redondeado del programa 3 es: {resultado}")   
    elif opcion == "4":
        resultado = programa4()
        print(f"El area de un triangulo es de: {round(resultado,2)} cm") 
    elif opcion == "5":
        resultado = programa5()
        print(f"El perimetro del rectangulo es: {resultado}")       
    elif opcion == "6": 
        resultado = programa6()
        print(f"El Area del trapecio es: {round(resultado,2)}")    
    elif opcion == "7":
        resultado = programa7()
        print(f"El volumen del prisma es {round(resultado,2)}")    
    elif opcion == "8":
        a, b, c, d, e, f = programa8()   
        print(f"El resultado A es: {a}")
        print(f"El resultado B es: {b}")
        print(f"El resultado C es: {c}")
        print(f"El resultado D es: {d}")
        print(f"El resultado E es: {round(e,2)}")
        print(f"El resultado F es: {round(f,2)}")
    elif opcion == "9":
        c1, c2, c3, c4, c5 = programa9()
        print(f"El resultado de c1 es: {c1}")
        print(f"El resultado de c2 es: {c2}")
        print(f"El resultado de c3 es: {c3}")
        print(f"El resultado de c5 es: {c4}")
        print(f"El resultado de c6 es: {c5}")
    elif opcion == "10":
        pies, pulgadas = programa10()
        print(f"El resultado en pies es: {pies}")
        print(f"El resultado en pulgadas es: {round(pulgadas, 2)}")
    elif opcion == "11":
        resultado = programa11()      
        print(f"El resultado de la regla de tres simple es {round(resultado,2)} ")
    elif opcion == "12":
        cuota, interes_Mensual, capital_Mensual = programa12()
        print(f"La cuota mensual es: {cuota} Balboas")
        print(f"El interés mensual es: {interes_Mensual} Balboas")
        print(f"El capital mensual es: {capital_Mensual} Balboas")
    elif opcion == "13":
        resultado = programa13()      
        print(f"El Salario neto a pagar es de {round(resultado,2)} Balboas ")       
    elif opcion == "14":
        resultado = programa14()      
        print(f"El costo total es de  {round(resultado,2)} Balboas ")     
    elif opcion == "15":
        resultado = programa15()      
        print(f"El costo total de la compra de tres articulos es de  {round(resultado,2)} Balboas ")  
    elif opcion == "16":
        resultado = programa16()      
        print(f"La nota final de Juan es  {resultado} ")     
    elif opcion == "17":
        gramos, kilogramos, centimetros, metros = programa17()
        print(f"El resultado en gramos es: {gramos}")
        print(f"El resultado en kilogramos es: {kilogramos}")
        print(f"El resultado en centímetros es: {centimetros}")
        print(f"El resultado en metros es: {metros}")
    elif opcion == "18":
        resultado = programa18()
        resultado_redondeado = round(resultado,2)
        print(f"La capital final es de: {resultado_redondeado}")
    elif opcion == "19":
        compra_sin_impuesto, compra_con_impuesto, promedio_de_la_compra = programa19()
        print(f"El total de la compra sin impuesto es: {compra_sin_impuesto} Balboas")
        print(f"El total de la compra con impuesto es: {compra_con_impuesto} Balboas")
        print(f"El promedio de la compra es: {promedio_de_la_compra} Balboas")
    elif opcion == "20":
        resultado = programa20()      
        print(f"El salario neto a pagar es de {round(resultado,2)} Balboas")   
    elif opcion == "21":
        resultado = programa21()
        print(resultado)    
    elif opcion == "22":
        resultado = programa22()
        print(resultado)
    elif opcion == "23":
        resultado = programa23()
        print(resultado)
    elif opcion == "24":
        resultado = programa24()
        print(resultado)  
    elif opcion == "25":
        resultado = programa25()
        print(resultado)    
    elif opcion == "26":
        resultado = programa26()
        print(resultado)    
    elif opcion == "27":
        resultado = programa27()
        print(resultado)    
    elif opcion == "28":
        resultado = programa28()
        print(resultado)  
    elif opcion == "29":
        resultado = programa29()
        print(resultado) 
    elif opcion == "30":
        resultado = programa30()
        print(resultado)    
    elif opcion =="31":
        programa31()
    elif opcion == "32":
        programa32()
    elif opcion == "33":
        programa33()
    elif opcion == "34":
        programa34()
    elif opcion == "35":
        programa35()
    elif opcion == "36":
        programa36()
    elif opcion == "37":
        resultado = programa37()
        print(f"El total de la compra es:{resultado} Balboas")     
    elif opcion == "38":
        resultado = programa38()
        print(f"La suma de los numeros pares hasta 20 es: {resultado}")
    elif opcion == "39":
        resultado = programa39()
        print(resultado)   
    elif opcion == "40":
        resultado = programa40()
        print(f"El perímetro del rectángulo es de {resultado}") 
    else:
        print("Nombre de programa no valido")     
 
 # Mostrar animación de despedida
print("\n")
mostrar_animacion()
