from os import system as sy
import time
sy('cls')

import json
import os

def carregar_usuarios():
    if os.path.exists('usuarios.json'):
        with open('usuarios.json', 'r') as file:
            return json.load(file)
    return {}
def salvar_usuarios(usuarios):
    with open('usuarios.json', 'w') as file:
        json.dump(usuarios, file, indent=4)

def cadastrar_usuario(usuarios):
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario in usuarios:
        print("Usuário já existe. Tente novamente.")
    else:
        usuarios[usuario] = senha
        salvar_usuarios(usuarios)
        print("Usuário cadastrado com sucesso!")

def fazer_login(usuarios):
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")

def main():
    usuarios = carregar_usuarios()

    while True:
        print("\nEscolha uma opção:")
        print("1. Cadastrar")
        print("2. Login")
        print("3. Sair")
        opcao = input("Digite o número da opção: ")

        if opcao == '1':
            cadastrar_usuario(usuarios)
        elif opcao == '2':
            fazer_login(usuarios)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()