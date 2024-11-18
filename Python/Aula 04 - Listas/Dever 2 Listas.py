numeros = []

for i in range(4):
    num = float(input(f"Insira o {i + 1}º número: "))
    numeros.append(num)

maior_numero = max(numeros)
menor_numero = min(numeros)

print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")