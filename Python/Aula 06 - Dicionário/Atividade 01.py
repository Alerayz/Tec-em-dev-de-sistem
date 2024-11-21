from os import system as sy
import time
sy('cls')

# Função para armazenar informações do produto
def armazenar_informacoes_produto():
    # Criando um dicionário para armazenar as informações do produto
    produto = {}

    # Solicitando informações do usuário
    produto['nome'] = input("Digite o nome do produto: ")
    produto['preco'] = float(input("Digite o preço do produto: "))
    produto['quantidade'] = int(input("Digite a quantidade em estoque: "))

    return produto

# Função para exibir as informações do produto
def exibir_informacoes_produto(produto):
    print("\nInformações do Produto:")
    print(f"Nome: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Quantidade em Estoque: {produto['quantidade']}")

# Programa principal
if __name__ == "__main__":
    produto = armazenar_informacoes_produto()
    exibir_informacoes_produto(produto)