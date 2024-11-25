"""
4)Implemente uma lojinha virtual simples! Onde possamos
ter um catálogo com 5 produtos e nesse podemos adicionar
ao carrinho ou visualizar-lo.Até chegarmos na finalização 
do qual mostrará o valor total

entrada - lista de produtos
processo - somar valores
saída - mostrar o valor total

"""
escolha = None
carrinho = []
valorTotal = 0

def carregarCatalogo():
    print('1 - R$ 4.000 Celular')
    print('2 - R$ 8.000 Notebook')
    print('3 - R$ 7.000 Tablet')
    print('4 - R$ 3.000 Smartwatch')
    print('5 - R$ 2.000 Fone de ouvido')
    print('6 - MOSTRAR CARRINHO')
    print('7 - FINALIZAR COMPRA')

    global escolha
    escolha = input('Digite a opção desejada: ')

def adicionarAoCarrinho():
    carrinho.append('Celular')
    valorTotal += 4000
    print('Celular adicionado ao carrinho')

# while True:
#     carregarCatalogo()
    
#     if escolha == '1':
    
#     elif escolha == '7':
#         break