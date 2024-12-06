from os import system as sy
import time
sy('cls')


num = int(input("Digite um número entre 1 e 10: "))

if 1 <= num <= 10:
    print(f"Tabuada do {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
else:
    print("Número inválido. Por favor, insira um número entre 1 e 10.")