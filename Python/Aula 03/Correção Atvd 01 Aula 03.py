from tkinter import Place


maior = 0

for i in range(0,3,1):
    numero = float(input(f'Digite o {i + 1}º número'))

    if numero > maior:
        maior = numero

print(f'O maior número é o : {maior}')