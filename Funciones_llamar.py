def programa1():
    a = 7 
    b = 0 
    c = 0 
    b = a 
    c = b
    a = a 
    return a, b, c 

def programa2():
    a = 10
    b = 0
    aux = 0
    a = a 
    b = a
    aux = b 
    return a, b, aux

def programa3():
    a = float(input("Leer A: "))
    b = float(input("Leer B: "))
    c = float(input("Leer C: "))
    d = (a + b + c) / 3
    return round(d, 2)

def programa4():
    Base = 3
    Altura = 4
    Hipotenusa = 5
    Area = (Base * Altura) / 2 
    return Area

def programa5():
    AB=  float(input("Ingrese el valor de AB: "))
    BC=  float(input("Ingrese el valor de BC: "))
    CD=  float(input("Ingrese el valor de CD: "))
    DA=  float(input("Ingrese el valor de DA: "))
    P = AB + BC + CD + DA
    return P

def programa6():
    base_1 = float(input("Ingrese el valor de la primera base "))
    base_2 = float(input("Ingrese el valor de la segunda base "))
    Altura = float(input("Ingrese el valor de la altura "))
    Area = (base_1 + base_2) * Altura / 2
    return Area

def programa7():
    largo = float(input("Ingrese el valor del largo "))
    ancho = float(input("Ingrese el valor del ancho "))
    altura = float(input("Ingrese el valor de la altura "))
    Volumen = largo * ancho * altura
    return Volumen

def programa8():
    x = float(input("Ingrese el valor de x "))
    a = 20 - (7 * x)
    b = (-7 * x) + 2 - (10 * x) + 5
    c = (4 * x) + 4 + (9 * x) + 18
    d = (6 * x) - 5 - (8 * x) + 2
    e = ((5 * x) + 78) / 28
    f = (((6 * x) -7) /4) + (((3 * 7) -5) /7)
    return a, b, c, d, e, f 

def programa9():
    a = float(input("Escriba el valor de A "))
    b = float(input("Escriba el valor de B "))
    c = float(input("Escriba el valor de C "))
    c1 = (4 * a) + (3 * b)
    c2 = (21 * a) - 18 + (8 * b) - 5
    c3 = (4 * a) + (3 * b) + 7
    c4 = (2 * a) + (3 * b) - (c ** 5)
    c5 = (2 * a) + (3 * b) - (c ** 2)
    return c1, c2, c3, c4, c5

def programa10():
    metros = float(input("Escriba la cantidad de metros: "))
    pies = metros * 3.28
    pulgadas = metros / 39.37
    return pies, pulgadas

def programa11():
    A = float(input("Ingrese el primer valor "))
    B = float(input("Ingrese el segundo valor "))
    C = float(input("Ingrese el tercer valor "))
    D = (B * C) / A
    return D

def programa12():
    monto = float(input("Ingrese el monto: "))
    tasa = float(input("Ingrese la tasa: "))
    plazo = float(input("Ingrese el plazo a pagar: "))
    tasa_Porcentaje = tasa * 100
    tasa_Mensual = tasa / 12
    cuota = round(monto * (tasa_Mensual / (1 - (1 + tasa_Mensual) ** (-plazo))), 2)
    interes_Mensual = round(monto * tasa_Mensual, 2)
    capital_Mensual = round(cuota - interes_Mensual, 2)
    return cuota, interes_Mensual, capital_Mensual

def programa13():
    salario_bruto = float(input("Ingrese el salario bruto "))
    ssocial = salario_bruto * 0.05
    seducativo = salario_bruto * 0.02
    cprestamo = 50
    salario_Neto = salario_bruto - ssocial - seducativo - cprestamo
    return salario_Neto

def programa14():
    precio_de_gasolina_de_95 = float(input("Ingrese el precio de la gasolina "))
    cantidad_de_litros = float(input("Ingrese la cantidad de litros "))
    costo_sin_impuestos = precio_de_gasolina_de_95 * cantidad_de_litros
    costo_total = costo_sin_impuestos * 1.07
    return costo_total

def programa15():
    Articulo1 = float(input("Ingrese el precio del primer articulo "))
    Articulo2 = float(input("Ingrese el precio del segundo articulo "))
    Articulo3 = float(input("Ingrese el precio del tercer articulo "))
    precio = Articulo1 + Articulo2 + Articulo3
    impuesto = precio * 0.07
    compra_total = precio + impuesto
    return compra_total

def programa16():
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
    nota = round(p1 + p2 + p3 + p4 + p5, 2)
    return nota

def programa17():
    unidad = float(input("Ingrese la cantidad: "))
    gramos = round(unidad / 0.001, 2)
    kilogramos = round(unidad / 1000, 2)
    centimetros = round(unidad / 0.01, 2)
    metros = round(unidad / 100, 2)
    return gramos, kilogramos, centimetros, metros

def programa18():
    Ci = float(input("Ingrese la capital inicial: "))
    i = float(input("Ingrese la tasa de interés: "))
    n = float(input("Ingrese el período de ahorro: "))
    Cf = round(Ci * (1 + i) ** n, 2)
    return Cf

def programa19():
    art1 = float(input("Ingrese el precio del primer artículo: "))
    art2 = float(input("Ingrese el precio del segundo artículo: "))
    art3 = float(input("Ingrese el precio del tercer artículo: "))
    art4 = float(input("Ingrese el precio del cuarto artículo: "))
    art5 = float(input("Ingrese el precio del quinto artículo: "))

    sumaArticulo = art1 + art2 + art3 + art4 + art5
    impuesto = sumaArticulo * 0.07
    compra_sin_impuesto = round(sumaArticulo, 2)
    compra_con_impuesto = round(impuesto + sumaArticulo, 2)
    promedio_de_la_compra = round(sumaArticulo / 5, 2)

    return compra_sin_impuesto, compra_con_impuesto, promedio_de_la_compra

def programa20():
    Salario_bruto = float(input("Ingrese el salario bruto "))
    Seguro_social = Salario_bruto * 0.08
    Seguro_educativo = Salario_bruto * 0.02
    impuesto = Salario_bruto * 0.15
    prestamo = 100
    Salario_Neto = Salario_bruto - Seguro_social - Seguro_educativo - impuesto - prestamo
    return Salario_Neto

def programa21():
    salario = float(input("Ingrese el salario: "))
    if salario > 3000:
        impuesto = salario * 0.07
        return "Debe pagar impuestos: " + str(impuesto)
    else:
        return "No debe pagar impuestos"     
    
def programa22():
    temperatura = float(input("Digite la temperatura: "))
    if temperatura < 20:
        if temperatura < 10:
            return "Nivel Azul" 
        else: 
            return "Nivel Verde"
    else:
        if temperatura < 30:
         return "Nivel Naranja"
        else:
         return "Nivel Rojo" 

def programa23():
    edad = float(input("Ingrese la edad: "))
    if edad <= 18:
        return "Es un adolecente - cierto "
    else:
        return "Es un adulto - falso "           

def programa24():
    n1 = float(input("Ingrese el primer numero: "))
    n2 = float(input("Ingrese el segundo numero: "))
    n3 = float(input("Ingrese el tercer numero: "))

    if n1 > n2 and n1 > n3:
        return (f"El numero {n1} es el mayor ")
    elif n2 > n1 and n2 > n3:
        return (f"El numero {n2} es el mayor ")
    if n3 > n1 and n3 > n2:
        return (f"El numero {n3} es el mayor ")       
    
def programa25():
    producto = float(input("Ingrese el precio del producto: "))
    d = float(input("Ingrese el descuento: "))
    p = d / 100
    descuento = producto * p
    porciento = producto - descuento
    if producto >= 50:
        return(f"El total de la compra con el descuento incluido es de {round(porciento,2)} Balboas ")
    else:
        return "Oferta especial"    
    
def programa26():
    lado1 = float(input("Ingrese el primer lado: "))
    lado2 = float(input("Ingrese el segundo lado: "))
    lado3 = float(input("Ingrese el tercer lado: "))

    if lado1 == lado2 and lado2 == lado3:
        return "Es un triangulo equilatero"
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        return "Es un triangulo isoceles"
    else:
        return "Es un triangulo escaleno"   
    
def programa27():
    numero = float(input("Ingrese un numero: "))

    if numero > 0:
        return "El numero es positivo"
    elif numero == 0:
        return "El numero es cero"
    else:
        return "El numero es negativo"    
    
def programa28():
    calificacion = float(input("Ingrese la calificacion: "))
    if calificacion >= 90 and calificacion <= 100:
        return("Su calificacion es A")
    elif calificacion >= 80 and calificacion < 90:
        return("Su calificacion es B")
    elif calificacion >= 70 and calificacion < 80:
        return("Su calificacion es C")
    elif calificacion >= 60 and calificacion < 70:
        return("Su calificacion es D")    
    else:
        return("F")     
    
def programa29():
    value = 0
    while value <= 5:
        C = float(input("Ingrese la calificacion: "))
        if 90 <= C <= 100:
           return 'La evaluacion es A'
        elif 80 <= C <= 89:
            return 'La evaluacion es B'   
        elif 70 <= C <= 79:
            return 'La evaluacion es C'
        elif 60 <= C <= 69:
            return 'La evaluacion es D' 
        else:
            return 'La evaluacion es F'       

def programa30():
    valor = 1

    while valor <= 3:
        numero = int(input("ingrese un numero: "))
        if numero > 0:
            return 'El numero es positivo'
        elif numero == 0:
            return 'El numero es cero' 
        else:
            return 'El numero es negativo'

def programa31():
    valor = 1
    while valor <= 10:
        print(valor)
        if valor == 7:
            break
        valor += 1

def programa32():
    calificaciones = int(input("Ingrese el número de calificaciones a evaluar: "))

    for i in range(calificaciones):
        calificacion = float(input("Ingrese la calificación: "))

        if calificacion >= 90 and calificacion <= 100:
            letra = 'A'
        elif calificacion >= 80 and calificacion <= 89:
            letra = 'B'
        elif calificacion >= 70 and calificacion <= 79:
            letra = 'C'
        elif calificacion >= 60 and calificacion <= 69:
            letra = 'D'
        else:
            letra = 'F'

        print(f"La calificación es {letra}")

    return None      

def programa33():
    for i in range(1,13):
        print("Tabla de multiplicar del",i)
        print("------------------------")
        for j in range(1,13):
            resultado = i * j 
            print(i, "x", j, "=", resultado)
            print()      
                   
    return None
        
def programa34():
    numero = 1

    while numero <= 15:
        print(numero)
        if numero %2 == 0:
            print("El numero es par")
        else:
            print("El numero es impar")
    
        numero += 1    
    return None    

def programa35():
    numero = 0
    while numero <= 15:
      if numero %2 == 0:
          print(f"El numero {numero} es un numero par")
      else:
          print(f"El numero {numero} es un numero impar")
      numero += 1   

    return None           

def programa36():
    numeros = list(range(1,11))
    for numero in numeros:
        if numero > 5:
            print(f"El numero {numero} es mayor ")
        elif numero <= 0:
            print(f"El numero {numero} es menor o igual a cero")
        else:
            print(f"El numero {numero} es menor")

        if numero == 9:
            break    

    return None      
        
def programa37():
    total = 0
    articulos = 0

    while articulos < 5:
        precio = float(input("Ingrese el precio del artículo: "))
        impuesto = precio * 0.07
        compra = precio + impuesto
        total += compra
        articulos += 1

    return total

def programa38():
    suma = 0
    for numero in range(2, 21, 2):
        suma += numero
    return suma

def programa39():
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    area = (base * altura) / 2
    return area

def programa40():
    AB = float(input("Ingrese el valor de AB: "))
    BC = float(input("Ingrese el valor de BC: "))
    CD = float(input("Ingrese el valor de CD: "))
    DA = float(input("Ingrese el valor de DA: "))

    P = AB + BC + CD + DA
    return P
