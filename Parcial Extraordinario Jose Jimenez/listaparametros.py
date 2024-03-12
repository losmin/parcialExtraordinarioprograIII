class ListaParametro:
    def __init__(self, Lista):
        self.Lista = Lista

    def suma_de_elementos(self):
        return sum(self.Lista)

numeros = [1, 2, 3, 4, 5]
parametros = ListaParametro(numeros)

suma_de_numeros = parametros.suma_de_elementos()
print(suma_de_numeros)
