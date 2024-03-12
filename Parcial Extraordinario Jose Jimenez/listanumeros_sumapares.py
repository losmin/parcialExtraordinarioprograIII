def sumar_numeros_pares(numeros: list) -> int:
    suma_pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            suma_pares += numero
    return suma_pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_pares = sumar_numeros_pares(numeros)
print(suma_pares)
