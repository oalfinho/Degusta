from estruturas.no import No

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def inserir(self, dado):
        novo = No(dado)
        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio

            while atual.proximo:
                atual = atual.proximo

            atual.proximo = novo
        self.tamanho += 1

    def remover(self, indice):
        if indice < 0 or indice >= self.tamanho:
            return None

        if indice == 0:
            removido = self.inicio
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
            return removido.dado

        atual = self.inicio

        for _ in range(indice - 1):
            atual = atual.proximo

        removido = atual.proximo
        atual.proximo = removido.proximo
        self.tamanho -= 1
        return removido.dado

    def buscar(self, indice):
        if indice < 0 or indice >= self.tamanho:
            return None

        atual = self.inicio

        for _ in range(indice):
            atual = atual.proximo
        return atual.dado

    def listar(self):
        atual = self.inicio

        while atual:
            yield atual.dado
            atual = atual.proximo

    def esta_vazia(self):
        return self.inicio is None

    def __len__(self):
        return self.tamanho