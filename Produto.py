class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_produtos(self):
        print("Nome:", self.nome)
        print("Preço:", self.preco)
        print("Quantidade:", self.quantidade)
