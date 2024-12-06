from os import system as sy
import time
import json
import os
sy('cls')

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def foi_aprovado(self):
        return self.calcular_media() >= 7

    def to_dict(self):
        return {
            'nome': self.nome,
            'notas': self.notas,
            'media': self.calcular_media(),
            'aprovado': self.foi_aprovado()
        }

def adicionar_aluno_a_json(aluno, arquivo='alunos.json'):
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            alunos = json.load(f)
    else:
        alunos = []

    alunos.append(aluno.to_dict())

    with open(arquivo, 'w') as f:
        json.dump(alunos, f, indent=4)

if __name__ == "__main__":
    aluno1 = Aluno("Alexandre", [7.0, 7.5, 6.5])
    adicionar_aluno_a_json(aluno1)

    aluno2 = Aluno("Mateus", [9.0, 8.5, 7.0])
    adicionar_aluno_a_json(aluno2)

    aluno3 = Aluno("João", [5.0, 4.5, 3.0])
    adicionar_aluno_a_json(aluno3)

    with open('alunos.json', 'r') as f:
        print(json.load(f))