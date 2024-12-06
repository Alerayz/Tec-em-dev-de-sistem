from os import system as sy
import time
sy('cls')

import time
from time import sleep as timer

segundos = int(input('Quantos segundos tem o timer: '))

for i in range(segundos,0,-1):
    timer(1)
    print(f'{i} segundos')

print('TEMPO ESGOTADO!')