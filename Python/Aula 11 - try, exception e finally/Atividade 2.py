from os import system as sy
import time
sy('cls')

aluno = {
    "nome": "Alexandre",
    "idade": 20,
    "notas": {
        "matematica": 8.5,
        "portugues": 9.0,
        "historia": 7.5
    },
    "turma": "3B",
    "ano": 2023
}
chave = input("Digite a chave que deseja acessar (nome, idade, notas, turma, ano): ")
try:
    valor = aluno[chave]
    print(f"O valor da chave '{chave}' é: {valor}")
except KeyError:
    print(f"A chave '{chave}' não existe. As chaves disponíveis são: {', '.join(aluno.keys())}")