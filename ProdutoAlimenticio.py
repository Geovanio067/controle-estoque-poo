from Produto import Produto

class ProdutoAlimenticio(Produto):
    def __init__(self, nome, preco, quantidade, validade):
        Produto.__init__(self, nome, preco, quantidade)
        self.validade = validade

    def exibir_produtos(self):
        Produto.exibir_produtos(self)
        print("Validade:", self.validade)
