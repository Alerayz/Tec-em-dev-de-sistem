numeros = [5, 8, 2, 9, 1]

#a)
# 1 metodo
numeros.sort()
print(numeros)  # [1, 2, 5, 8, 9]
numeros.sort(reverse=True)
print(numeros)  # [9, 8, 5, 2, 1]

# 2 metodo
# for numero in numeros:
#     if numero > maior:
#         maior = numero

# c)
numeros.append(7)
numeros.insert(2 , 3)
print(numeros)

# d)
# 1 metodo
# del numeros[1]
# numeros.insert(10 , 1)

# 2 metodo
numeros[1] = 10
print(numeros)

# e)
del numeros[2]
del numeros[3]
del numeros[4]
print(numeros)