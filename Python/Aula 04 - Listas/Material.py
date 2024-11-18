"""
LISTAS
"""
# cliente1 = "Victor"
# cliente2 = "Maria"
# cliente3 = "João"

# CRUD - CREATE , READ , UPDATE , DELETE

clientes = ["Victor", "Maria", "João"]
teste = ['texto' ,123,True, []]
# clientsAlt = list()

print(type(clientes))
print(teste)

# metodos de uma lista
lista = ['Cod' , 'Ghost' , 'Rocket League' , 'Fortnite']
print(lista)

lista.append('Videogame') # adicionar no final(adicionar alguma coisa)
print(lista)

lista.pop() # remover o ultimo elemento
print(lista)

lista.insert(2 , 'Minecraft') # adicionar em uma posição específica (indice,dado)
print(lista)

del lista[1] # deletar um elemento
print(lista)

# indice 0 1 2 3 4 / -5 -4 -3 -2 -1
print(lista[1])

lista.clear()# limpar a lista
print(lista)

lista.remove('Fortnite') # remove o primeiro elemento que encontrar com o dado passado
print(lista) 

