from os import system as sy
import time
sy('cls')

import random

lista_alunos = ['Paloma','Victor','Alessandra','João','Geraldo']

sorteado = random.choice(lista_alunos)

print(sorteado)