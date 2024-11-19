valorTotal = float(0)

# parametro - recebe o argumento
def somarValor():
    global valorTotal

    valorProduto = float(input('PREÇO DO PRODUTO'))
    valorTotal += valorProduto

somarValor()

print(f'Valor total do produto é R$: {valorTotal}')

