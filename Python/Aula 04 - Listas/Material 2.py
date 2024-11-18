alunosPt1 = ['Carlos' , 'Ryan' , 'Geraldo']
alunospt2 = ['João' , 'Maria' , 'Pedro']

alunosPt3 = alunosPt1 + alunospt2
print(alunosPt3)

alunosPt1.extend(alunospt2)
print(alunosPt1)

# for + array
print(len(alunosPt1))

# for i in range(len(alunosPt1)):
#     print(alunosPt1[i])

# for i in alunosPt1:
#     print(i)

alunosPt1.append('Alexandre')

for nome in alunosPt1:
    print(f'- {nome} \n ###')