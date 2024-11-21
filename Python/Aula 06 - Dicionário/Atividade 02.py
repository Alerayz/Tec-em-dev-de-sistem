from os import system as sy
import time
sy('cls')

# def armazenar_contatos():
#     contatos = {}

#     while True:
#         nome = input("Digite o nome do contato (ou '0' para encerrar): ")
        
#         if nome.lower() == "0":
#             break
        
#         numero = input("Digite o número de telefone: ")
        
#         contatos[nome] = numero
#         print(f"Contato '{nome}' adicionado com sucesso!")

#     return contatos

# def exibir_contatos(contatos):
#     print("\nContatos cadastrados:")
#     for nome, numero in contatos.items():
#         print(f"{nome}: {numero}")

# if __name__ == "__main__":
#     contatos = armazenar_contatos()
#     exibir_contatos(contatos)

    # def limit_number (value, min_value, max_value):
    #     return max(min(value, max_value), min_value)
    
    # limit_number = 11

    # print(limit_number(11))

    # def limit_number(
    # value: 11,
    # min_value: 11,
    # max_value: 11):
    #     return max(min(value, max_value), min_value)

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