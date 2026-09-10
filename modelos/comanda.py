from datetime import datetime
from estruturas.lista_encadeada import ListaEncadeada

# Classe Comanda representa uma comanda de um cliente, contendo informações sobre a data de abertura, as refeições e bebidas adicionadas, e o status da comanda (aberta ou fechada).

class Comanda:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.data_abertura = datetime.now()

        self.refeicoes = ListaEncadeada()
        self.bebidas = ListaEncadeada()

        self.fechada = False
        self.data_fechamento = None

    def adicionar_refeicao(self, item):
        if self.fechada:
            raise Exception("A comanda já está fechada.")

        self.refeicoes.inserir(item)

    def adicionar_bebida(self, item):
        if self.fechada:
            raise Exception("A comanda já está fechada.")

        self.bebidas.inserir(item)

    def remover_refeicao(self, indice):
        if self.fechada:
            raise Exception("A comanda já está fechada.")

        return self.refeicoes.remover(indice)

    def remover_bebida(self, indice):
        if self.fechada:
            raise Exception("A comanda já está fechada.")

        return self.bebidas.remover(indice)

    def calcular_total(self):
        total = 0

        for item in self.refeicoes.listar():
            total += item.subtotal()

        for item in self.bebidas.listar():
            total += item.subtotal()

        return total

    def fechar(self):
        if self.fechada:
            raise Exception("Comanda já fechada.")

        self.fechada = True
        self.data_fechamento = datetime.now()

    def __str__(self):
        status = "Fechada" if self.fechada else "Aberta"

        return (
            f"Comanda #{self.numero} | "
            f"{self.cliente} | "
            f"{status} | "
            f"R$ {self.calcular_total():.2f}"
        )