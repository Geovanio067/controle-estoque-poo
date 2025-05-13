from Produto import Produto
from ProdutoAlimenticio import ProdutoAlimenticio

lista = []

while True:
    print('')
    print('1 - Cadastrar Produto')
    print('2 - Cadastrar Produto Alimentício')
    print('3 - Mostrar Produtos')
    print('0 - Sair')

    op = input('Escolha: ')

    if op == '1':
        nome = input('Nome: ')
        preco = float(input('Preço: '))
        qtd = int(input('Quantidade: '))
        p = Produto(nome, preco, qtd)
        lista.append(p)

    elif op == '2':
        nome = input('Nome: ')
        preco = float(input('Preço: '))
        qtd = int(input('Quantidade: '))
        validade = input('Validade: ')
        pa = ProdutoAlimenticio(nome, preco, qtd, validade)
        lista.append(pa)

    elif op == '3':
        for i in lista:
            print('')
            i.exibir_produtos()

    elif op == '0':
        break

    else:
        print('Opção inválida')
