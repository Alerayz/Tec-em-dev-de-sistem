# 1 metodo
# numero[1] = input

numeros = []

for i in range(4):
    numero = int(input(f'Digite o {i+1}º número: '))
    numeros.append(numero)

    #numero > maior

print(numeros)
print(max(numeros))
print(min(numeros))