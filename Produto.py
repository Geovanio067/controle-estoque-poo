class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_produtos(self):
        print("Nome:", self.nome)
        print("Preço:", self.preco)
        print("Quantidade:", self.quantidade)

    def repor_estoque(self, qtd):
        self.quantidade += qtd
        print(f'Estoque de {self.nome} atualizado para {self.quantidade}')

    def vender_produto(self, qtd):
        if self.quantidade >= qtd:
            self.quantidade -= qtd
            print(f'{qtd} unidades de {self.nome} vendidas.')
        else:
            print(f'Estoque insuficiente para vender {qtd} unidades de {self.nome}')