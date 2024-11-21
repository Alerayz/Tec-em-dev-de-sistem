from os import system as sy
import time
sy('cls')

def armazenar_contatos():
    contatos = {}

    while True:
        nome = input("Digite o nome do contato (ou 'finalizar' para encerrar): ")
        
        if nome.lower() == "finalizar":
            break
        
        numero = input("Digite o número de telefone: ")
        
        contatos[nome] = numero
        print(f"Contato '{nome}' adicionado com sucesso!")

    return contatos

def exibir_contatos(contatos):
    print("\nContatos cadastrados:")
    for nome, numero in contatos.items():
        print(f"{nome}: {numero}")

if __name__ == "__main__":
    contatos = armazenar_contatos()
    exibir_contatos(contatos)