from os import system as sy
import time
sy('cls')

class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome}, Quantidade: {self.quantidade}, Preço: R${self.preco:.2f}"


class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto):
        if produto.nome in self.produtos:
            self.produtos[produto.nome].quantidade += produto.quantidade
        else:
            self.produtos[produto.nome] = produto
        print(f"Produto '{produto.nome}' adicionado ao estoque.")

    def remover_produto(self, nome, quantidade):
        if nome in self.produtos:
            if self.produtos[nome].quantidade >= quantidade:
                self.produtos[nome].quantidade -= quantidade
                print(f"Removido {quantidade} do produto '{nome}'.")
                if self.produtos[nome].quantidade == 0:
                    del self.produtos[nome]
                    print(f"Produto '{nome}' removido do estoque.")
            else:
                print(f"Quantidade insuficiente para remover. Estoque atual: {self.produtos[nome].quantidade}.")
        else:
            print(f"Produto '{nome}' não encontrado no estoque.")

    def verificar_produto(self, nome):
        if nome in self.produtos:
            print(self.produtos[nome])
        else:
            print(f"Produto '{nome}' não encontrado no estoque.")

    def listar_produtos(self):
        if not self.produtos:
            print("Estoque vazio.")
        else:
            print("Produtos no estoque:")
            for produto in self.produtos.values():
                print(produto)

if __name__ == "__main__":
    estoque = Estoque()

    produto1 = Produto("Nocta x Nike Hot Step 2", 100, 1800.90)
    produto2 = Produto("Air Max Dn Light Bone and Light Taupe", 500, 1500.90)
    estoque.adicionar_produto(produto1)
    estoque.adicionar_produto(produto2)

    estoque.listar_produtos()

    estoque.verificar_produto("Nocta x Nike Hot Step 2")

    estoque.remover_produto("Nocta x Nike Hot Step 2", 3)
    estoque.verificar_produto("Nocta x Nike Hot Step 2")

    estoque.remover_produto("Nocta x Nike Hot Step 2", 7)

    estoque.listar_produtos()