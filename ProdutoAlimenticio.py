from Produto import Produto

class ProdutoAlimenticio(Produto):
    def __init__(self, nome, preco, quantidade, data_validade):
        super().__init__(nome, preco, quantidade)
        self.data_validade = data_validade

    def exibir_produtos(self):
        print(f'Nome: {self.nome}, Preço: {self.preco}, Quantidade: {self.quantidade}, Validade: {self.data_validade}')
