"""
4)Implemente uma lojinha virtual simples! Onde possamos
ter um catálogo com 5 produtos e nesse podemos adicionar
ao carrinho ou visualizar-lo.Até chegarmos na finalização 
do qual mostrará o valor total

entrada - lista de produtos
processo - somar valores
saída - mostrar o valor total

"""
# escolha = None
# carrinho = []
# valorTotal = 0

# def carregarCatalogo():
#     print('1 - R$ 4.000 Iphone')
#     print('2 - R$ 8.000 Macbook')
#     print('3 - R$ 7.000 Ipad')
#     print('4 - R$ 3.000 Appplewatch')
#     print('5 - R$ 2.000 Airpods')
#     print('6 - MOSTRAR CARRINHO')
#     print('7 - FINALIZAR COMPRA')

#     global escolha
#     escolha = input('Digite a opção desejada: ')

# def adicionarCarrinho(nome,valor):
#     carrinho.append(nome)
#     global valorTotal
#     valorTotal += valor
#     print(f'{nome} adicionado efetuado com sucesso!')

# while True:
#     carregarCatalogo()

#     if escolha == '1':
#         adicionarCarrinho('Iphone',4.000)
#     elif escolha == '2':
#         adicionarCarrinho('Macbook',8.000)
#     elif escolha == '3':
#         adicionarCarrinho('Ipad',7.000)
#     elif escolha == '4':
#         adicionarCarrinho('AppleWatch',3.000)
#     elif escolha == '5':
#         adicionarCarrinho('Airpods',10.00)
#     elif escolha == '6':
#         print(carrinho)
#     elif escolha == '7':
#         break
#     else:
#         print('Opção inválida! Tente novamente!')

# print(f'Valor total da compra é de : {valorTotal}')


"""
4)Implemente uma lojinha virtual simples! Onde possamos 
ter um catálogo com 5 produtos e nesse podemos adicionar 
ao carrinho ou visualizar-lo. Até chegarmos na finalização 
do qual mostrará o valor total

entrada - lista de produtos
processo - somar valores
saida - mostrar o valor total

"""
escolha = None
carrinho = []
valorTotal = 0

def carregarCatalogo():
    print('1 - R$ 14.00 Shampo')
    print('2 - R$ 20.00  Pasta de dentes')
    print('3 - R$ 4.00 Sabonete')
    print('4 - R$ 25.00 Fio dental')
    print('5 - R$ 10.00 Condicionador')
    print('6 - MOSTRAR CARRINHO')
    print('7 - FINALIZAR')

    global escolha
    escolha = input('Digite a opção desejada: ')

def adicionarCarrinho(nome,valor):
    carrinho.append(nome)
    global valorTotal
    valorTotal += valor 
    print(f'{nome} adicionado efetuado com sucesso!')

while True:
    carregarCatalogo()

    if escolha == '1':
        adicionarCarrinho('Shampo',14.00)
    elif escolha == '2':
        adicionarCarrinho('Pasta de dentes',20.00)
    elif escolha == '3':
        adicionarCarrinho('Sabonete',4.00)
    elif escolha == '4':
        adicionarCarrinho('Fio dental',25.00)
    elif escolha == '5':
        adicionarCarrinho('Condicionador',10.00)
    elif escolha == '6':
        print(carrinho)
    elif escolha == '7':
        break
    else:
        print('Opção inválida! Tente novamente!')

print(f'Valor total da compra é de : {valorTotal}')
