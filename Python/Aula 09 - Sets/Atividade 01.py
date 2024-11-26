matematica = {"Alice", "Bob", "Carlos", "Diana", "Eva", "Felipe", "Alexandre"}
portugues = {"Alice", "Eva", "Gustavo", "Fiona", "Bob", "Carlos", "Lucas", "Daniel"}

alunos_so_matematica = matematica - portugues

alunos_so_portugues = portugues - matematica

alunos_ambas = matematica & portugues
 
print("Alunos de Matemática:")
print(matematica)

print("\nAlunos de Português:")
print(portugues)

print("\nAlunos que cursam ambas as disciplinas (Matemática e Português):")
print(alunos_ambas)

print("\nAlunos que cursam apenas Matemática:")
print(alunos_so_matematica)

print("\nAlunos que cursam apenas Português:")
print(alunos_so_portugues)