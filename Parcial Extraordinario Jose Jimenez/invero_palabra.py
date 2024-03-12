def invertir_palabras(palabras: list) -> list:
    palabras_invertidas = []
    for palabra in palabras:
        palabras_invertidas.append(palabra[::-1])
    return palabras_invertidas

frase = ["Hola", "Mundo"]
frase_invertida = invertir_palabras(frase)
print(frase_invertida)
