from os import system as sy
import time
sy('cls')

import random

atividades = [
    "Estudar Python",
    "Fazer exercícios",
    "Ler um livro",
    "Assistir a um filme",
    "Cozinhar uma nova receita",
    "Fazer uma caminhada",
    "Praticar meditação",
    "Jogar um jogo de tabuleiro",
    "Visitar um amigo",
    "Trabalhar em um projeto pessoal"
]

dias_da_semana = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo"
]

agenda_semanal = {}

for dia in dias_da_semana:
    atividade = random.choice(atividades)
    agenda_semanal[dia] = atividade

print("Agenda Semanal:")
for dia, atividade in agenda_semanal.items():
    print(f"{dia}: {atividade}")