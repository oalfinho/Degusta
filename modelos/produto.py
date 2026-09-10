# classe produto é o modelo de um produto, contendo informações sobre nome, preço de compra, preço de venda, data de compra, data de vencimento e quantidade em estoque.
class Produto:
    def __init__(
        self,
        nome,
        preco_compra,
        preco_venda,
        data_compra,
        data_vencimento,
        quantidade
    ):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade

    def adicionar_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero.") 

        self.quantidade += quantidade

    def remover_estoque(self, quantidade):
        if quantidade > self.quantidade:
            raise ValueError("Estoque insuficiente.")

        self.quantidade -= quantidade

    def __str__(self):
        return (
            f"{self.nome} | "
            f"Estoque: {self.quantidade} | "
            f"R$ {self.preco_venda:.2f}"
        )