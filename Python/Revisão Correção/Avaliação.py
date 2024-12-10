# 1) Crie uma função chamada classificar_idade que recebe a idade de uma pessoa e retorna:
# "Criança" se a idade for menor que 12 anos.
# "Adolescente" se a idade estiver entre 12 e 17 anos.
# "Adulto" se a idade for maior ou igual a 18 anos.
# Em seguida, escreva um código que:  Peça ao usuário que insira sua idade e use a função classificar_idade para exibir a classificação.

def classificar_idade(idade):
    if idade < 12:
        return "Criança"
    elif 12 <= idade <= 17:
        return "Adolescente"
    else:
        return "Adulto"

try:
    idade_usuario = int(input("Por favor, insira sua idade: "))
    classificacao = classificar_idade(idade_usuario)
    print(f"A classificação da sua idade é: {classificacao}")
except ValueError:
    print("Por favor, insira um número válido para a idade.")


#2)Escreva um programa para um sistema de controle de estoque de uma loja. 
# O programa deve:Usar um para armazenar os itens no estoque, onde as chaves são os nomes dos produtos
#  e os valores são as quantidades disponíveis.Permitir que o usuário escolha uma das opções:
# Adicionar um novo produto ao estoque.
# Atualizar a quantidade de um produto existente.
# Verificar se um produto está disponível (quantidade maior que 0).
# Continuar exibindo o menu até que o usuário escolha sair.

estoque =()

def exibir_menu():
    print("\nSistema de Controle de Estoque")
    print("1 - Adicionar produto ao estoque")
    print("2 - Verificar disponibilidade do produto")
    print("3 - Sair")
    return input("Escolha uma opção:")

def gerenciar_produto(estoque):
    produto = input("Digite o nome do Produto:")
    try:
        quantidade = int(input("Digite a quantidade:"))
        if quantidade < 0:
            print("A quantidade ão pode ser negativa")
        else:
            estoque[produto] = quantidade
            print(f"Produto '{produto}' atualizado com sucesso! Quantidade: {produto}.")
    except ValueError:
        print("Por Favor, insira um número válido para a Qauntidade!")

def verificar_produto(produto):
    produto = input("Digite o nome do produto a ser verificado: ")
    if estoque.get(produto, 0) > 0:
        print(f"O produto '{produto}' está disponível com quantidade {estoque[produto]}. ")
    else:
        print(f"O produto '{produto}' não está dosponível ou está fora de estoque.")

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            gerenciar_produto(estoque)
        elif opcao == "2":
            verificar_produto(estoque)
        elif opcao == "3":
            print("Saindo do Sistema. Até Logo!")
            break
        else:
            print("Opção Inválida, Por favor escolha uma opção válida!")

# 3)Crie um jogo simples em Python:Um número secreto entre 1 e 100 é gerado aleatoriamente.O jogador tem 5 tentativas para adivinhar o número.Após cada tentativa, o programa deve informar:
# "Muito alto!" se o palpite for maior que o número.
# "Muito baixo!" se o palpite for menor que o número.
# "Parabéns, você acertou!" se o palpite for igual ao número.
# Caso o jogador não acerte após 5 tentativas, exiba "Game Over! O número era X".
# Utilize a biblioteca random para gerar o número secreto.
import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 5

    print("Bem-vindo ao jogo de adivinhação!")
    print("Você tem 5 tentativas para adivinhar o número secreto entre 1 e 100.")

    for tentativa in range(1, tentativas + 1):
        palpite = int(input(f"Tentativa {tentativa}: Qual é o seu palpite? "))

        if palpite > numero_secreto:
            print("Muito alto!")
        elif palpite < numero_secreto:
            print("Muito baixo!")
        else:
            print("Parabéns, você acertou!")
            break
    else:
        print(f"Game Over! O número era {numero_secreto}.")

if __name__ == "__main__":
    jogo_adivinhacao()

# 4)Crie duas classes:
# 1 Autor, com os atributos:  Nome, nacionalidade e livros
# 2 Livro, com os atributos: titulo, ano e autor
# Depois, escreva um programa que:Crie um autor e dois livros associados a ele.
# Imprima o nome do autor e a lista dos seus livros.

class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def __str__(self):
        return f"Autor: {self.nome}, Nacionalidade: {self.nacionalidade}"


class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor

    def __str__(self):
        return f"Título: {self.titulo}, Ano: {self.ano}, Autor: {self.autor.nome}"


if __name__ == "__main__":
    autor = Autor("Robert Greene", "Estadunidense")

    livro1 = Livro("48 Leis do Poder", 1998, autor)
    livro2 = Livro("33 Estratégias de Guerra", 2006, autor)

    autor.adicionar_livro(livro1)
    autor.adicionar_livro(livro2)

    print(autor)
    print("Livros:")
    for livro in autor.livros:
        print(livro)


# 5) Implemente uma função chamada calculadora que:Receba dois números e uma operação 
# (adição, subtração, multiplicação ou divisão).Retorne o resultado da operação.
# Trate divisões por zero e exiba uma mensagem apropriada.Salve o histórico dela em um json

import json
import os

def calculadora(num1, num2, operacao):
    resultado = None
    mensagem = ""

    if operacao == "adição":
        resultado = num1 + num2
    elif operacao == "subtração":
        resultado = num1 - num2
    elif operacao == "multiplicação":
        resultado = num1 * num2
    elif operacao == "divisão":
        if num2 == 0:
            mensagem = "Erro: Divisão por zero não é permitida."
            resultado = None
        else:
            resultado = num1 / num2
    else:
        mensagem = "Erro: Operação inválida."

    salvar_historico(num1, num2, operacao, resultado, mensagem)

    return resultado, mensagem

def salvar_historico(num1, num2, operacao, resultado, mensagem):
    if os.path.exists("historico_calculadora.json"):
        with open("historico_calculadora.json", "r") as file:
            historico = json.load(file)
    else:
        historico = []

    operacao_info = {
        "num1": num1,
        "num2": num2,
        "operacao": operacao,
        "resultado": resultado,
        "mensagem": mensagem
    }
    historico.append(operacao_info)

    with open("historico_calculadora.json", "w") as file:
        json.dump(historico, file, indent=4)

if __name__ == "__main__":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (adição, subtração, multiplicação, divisão): ")

    resultado, mensagem = calculadora(num1, num2, operacao)

    if mensagem:
        print(mensagem)
    else:
        print(f"O resultado da {operacao} é: {resultado}")