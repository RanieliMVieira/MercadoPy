from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main():
    menu()

def menu():
    print('=================================')
    print('========== Bem-vindo(a) =========')
    print('=========== Geek Shop ===========')
    print('=================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto')
    print('2 - Listar produto')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')
    print('\n')

    opcao = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao ==2:
        listar_produtos()
    elif opcao == 3:
        comprar_produtos()
    elif opcao == 4:
        visualizar_produtos()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(1)
        menu()

def cadastrar_produto():
    print('Cadastro de Produto')
    print('===================')

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: '))

    prod = Produto(nome, preco)

    produtos.append(prod)

    print(f'O produto {prod.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()

def listar_produtos():
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('--------------------')
        for produto in produtos:
            print(produto)
            print('----------')
            sleep(1)
    else:
        print('Aionda não existem produtos cadastrados.')
    sleep(2)
    menu()

def comprar_produtos():
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        print('--------------------------------------------------------------')
        print('=================== Produtos Disponíveis =====================')
        for prod in produtos:
            print(prod)
            print('--------------------------------------------------------')
            sleep(1)
        codigo = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)
        if produto:
            if len(carrinho) > 0:
                tem_no_carinho = False
                for item in carrinho:
                    quant= item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidade no carrinho.')
                        tem_no_carinho = True
                        sleep(2)
                        menu()
                if not tem_no_carinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado no carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com o código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos para vender.')
        sleep(2)
        menu()

def visualizar_produtos():
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho.')
        sleep(2)
        menu()

def fechar_pedido():
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do Carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total = valor_total + dados[0].preco * dados[1]
                print('-----------------------')
                sleep(2)
        print(f'O total é : {formata_float_str_moeda(valor_total)}')
        print('Volte sempre')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho.')
        sleep(2)
        menu()

def pega_produto_por_codigo(codigo) -> Produto:
    p: Produto = None

    for prod in produtos:
        if prod.codigo == codigo:
            p = prod
    return p

if __name__ == '__main__':
    main()
