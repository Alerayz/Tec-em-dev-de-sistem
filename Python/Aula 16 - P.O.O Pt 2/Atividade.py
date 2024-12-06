from os import system as sy
import time
sy('cls')

class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.porta_malas = []
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"O carro {self.modelo} acelerou para {self.velocidade} km/h.")

    def adicionar_ao_porta_malas(self, item):
        self.porta_malas.append(item)
        print(f"{item} adicionado ao porta-malas do carro {self.modelo}.")

    def mostrar_porta_malas(self):
        if self.porta_malas:
            print(f"Conteúdo do porta-malas do carro {self.modelo}: {', '.join(self.porta_malas)}")
        else:
            print(f"O porta-malas do carro {self.modelo} está vazio.")


class Motorista:
    def __init__(self, nome):
        self.nome = nome
        self.carro = None

    def associar_carro(self, carro):
        self.carro = carro
        print(f"{self.nome} agora está dirigindo o carro {carro.modelo}.")

    def acelerar_carro(self, incremento):
        if self.carro:
            self.carro.acelerar(incremento)
        else:
            print(f"{self.nome} não tem um carro associado.")

    def adicionar_item_porta_malas(self, item):
        if self.carro:
            self.carro.adicionar_ao_porta_malas(item)
        else:
            print(f"{self.nome} não tem um carro associado.")


carro1 = Carro("Mercedes AMG", "azul")
motorista1 = Motorista("Alexandre")

motorista1.associar_carro(carro1)
motorista1.acelerar_carro(110)
motorista1.adicionar_item_porta_malas("Cooler de Bebidas")
motorista1.adicionar_item_porta_malas("Bola de Alta")
carro1.mostrar_porta_malas()