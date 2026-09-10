from estruturas.no import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def enfileirar(self, dado):
        novo = No(dado)

        if self.fim is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

        self.tamanho += 1

    def desenfileirar(self):
        if self.inicio is None:
            return None

        dado = self.inicio.dado
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        self.tamanho -= 1
        return dado

    def primeiro(self):
        if self.inicio:
            return self.inicio.dado

        return None

    def esta_vazia(self):
        return self.inicio is None

    def __len__(self):
        return self.tamanho