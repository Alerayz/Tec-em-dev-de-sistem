# Catálogo de produtos
produtos = {
    'a': ('PAMONHA', 7.00),
    'b': ('CALDO', 4.00),
    'c': ('PASTEL', 6.99),
    'd': ('CAFÉ', 3.00),
}

print('----CATALOGO----')
for chave, (nome, preco) in produtos.items():
    print(f"{chave.upper()}) {nome} - R$ {preco:.2f}")
print('E) CANCELAR')
print('F) FINALIZAR')

# Inicializa o valor total como 0.0
valorTotal = 0.0  

while True:
    # Converte a opção para minúscula
    opcao = input('Qual opção desejada: ').lower()  

    if opcao in produtos:
        nome, preco = produtos[opcao]
        print(f"Você escolheu {nome}.")
        valorTotal += preco  # Adiciona o valor ao total
    elif opcao == 'e':
        print("Pedido cancelado!")
        break
    elif opcao == 'f':
        print("Total do pedido: R$", valorTotal)
        break
    else:
        print("Opção inválida! Tente novamente.")  
    
    adicionar = input('Deseja adicionar mais itens? (sim/não): ').lower()
    if adicionar != 'sim':
        break

print('Valor total do pedido: R$', valorTotal)  
print('Seu pedido está sendo processado!')
print('Obrigado!')