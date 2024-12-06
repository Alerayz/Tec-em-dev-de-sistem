from os import system as sy
import time
sy('cls')

class ItemPedido:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome}: R${self.preco:.2f}"


class Cardapio:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def mostrar_cardapio(self):
        print("Cardápio:")
        for item in self.itens:
            print(item)


class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def calcular_total(self):
        return sum(item.preco for item in self.itens)

    def mostrar_pedido(self):
        print("Pedido:")
        for item in self.itens:
            print(item)
        print(f"Total: R${self.calcular_total():.2f}")

cardapio = Cardapio()
cardapio.adicionar_item(ItemPedido("Pizza", 30.00))
cardapio.adicionar_item(ItemPedido("Refrigerante", 5.00))
cardapio.mostrar_cardapio()

pedido = Pedido()
pedido.adicionar_item(cardapio.itens[0])
pedido.adicionar_item(cardapio.itens[1])
pedido.mostrar_pedido()