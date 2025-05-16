from Produto import Produto
from ProdutoAlimenticio import ProdutoAlimenticio

produtos = []

while True:
    print('\n1 - Produto comum')
    print('2 - Produto alimentício')
    print('3 - Ver produtos')
    print('4 - Repor')
    print('5 - Vender')
    print('0 - Sair')

    opcao = input('opção: ')

    if opcao == '1':
        nome = input('nome: ')
        preco = float(input('preço: '))
        qtd = int(input('quantidade: '))
        p = Produto(nome, preco, qtd)
        produtos.append(p)

    elif opcao == '2':
        nome = input('nome: ')
        preco = float(input('preço: '))
        qtd = int(input('quantidade: '))
        validade = input('validade: ')
        p = ProdutoAlimenticio(nome, preco, qtd, validade)
        produtos.append(p)

    elif opcao == '3':
        for p in produtos:
            p.exibir_produtos()

    elif opcao == '4':
        nome = input('nome do produto: ')
        qtd = int(input('quanto vai repor: '))
        for p in produtos:
            if p.nome == nome:
                p.repor_estoque(qtd)

    elif opcao == '5':
        nome = input('nome do produto: ')
        qtd = int(input('quanto vai vender: '))
        for p in produtos:
            if p.nome == nome:
                p.vender_produto(qtd)

    elif opcao == '0':
        break
