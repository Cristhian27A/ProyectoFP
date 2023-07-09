
def sumar_numeros_pares(numero):
    suma = 0
    for a in range(1, numero + 1):
        if a % 2 == 0:
         suma += a
    return suma

resultado = sumar_numeros_pares(20)
print(f"La suma de los numeros pares es de {resultado}")

print("\nFin del programa 38")