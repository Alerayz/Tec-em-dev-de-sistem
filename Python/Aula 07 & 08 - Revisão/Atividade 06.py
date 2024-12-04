from os import system as sy
import time
sy('cls')

valor = int(input("Digite um número: "))

antecessor = valor - 1
sucessor = valor + 1

print(f"O número escolhido é {valor}.")
print(f"O antecessor valor é {antecessor}, o valor é {valor} e o sucessor é {sucessor}.")