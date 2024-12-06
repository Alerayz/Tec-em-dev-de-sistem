from os import system as sy
import time
sy('cls')

from datetime import datetime, timedelta

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def data_nascimento(self):
        ano_atual = datetime.now().year
        ano_nascimento = ano_atual - self.idade
        return f"{ano_nascimento}-01-24"

pessoa = Pessoa("Alexandre", 19)
print(f"Nome: {pessoa.nome}")
print(f"Idade: {pessoa.idade}")
print(f"Data de Nascimento: {pessoa.data_nascimento()}")