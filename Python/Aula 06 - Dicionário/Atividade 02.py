from os import system as sy
import time
sy('cls')

def limit_to_11_digits(value):
    str_value = ''.join(filter(str.isdigit, str(value)))
    limited_value = str_value[:11]
    
    return limited_value

def limit_to_11_digits(value):
    str_value = ''.join(filter(str.isdigit, str(value)))
    limited_value = str_value[:11]
    return limited_value

def main():
    contatos = {}

    while True:
        nome = input("Digite o nome do contato (ou '0' para encerrar): ")

        if nome.lower() == "0":
            break
        
        numero = input("Digite o número de telefone: ")
        numero_limitado = limit_to_11_digits(numero)
        contatos[nome] = numero_limitado
    print("\nContatos cadastrados:")
    for nome, numero in contatos.items():
        print(f"{nome}: {numero}")

if __name__ == "__main__":
    main()