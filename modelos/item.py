class Item:
    def __init__(self, nome, valor, quantidade=1):
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade

    def subtotal(self):
        return self.valor * self.quantidade

    def __str__(self):
        return (
            f"{self.nome} | "
            f"{self.quantidade}x | "
            f"R$ {self.subtotal():.2f}"
        )