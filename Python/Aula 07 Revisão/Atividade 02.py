from os import system as sy
import time
sy('cls')

def converter_moeda():
    valor_reais = float(input("Digite o valor em Reais: "))
    print("Escolha a moeda para a qual deseja converter:")
    print("1 - Dólares")
    print("2 - Ienes")
    print("3 - Euros")
    
    opcao = int(input("Digite o número da opção desejada: "))
    
    if opcao == 1:
        taxa_dolar = 5.82 
        valor_convertido = valor_reais / taxa_dolar
        print(f"{valor_reais} Reais equivalem a {valor_convertido:.2f} Dólares.")
    elif opcao == 2:
        taxa_iene = 0.038  
        valor_convertido = valor_reais / taxa_iene
        print(f"{valor_reais} Reais equivalem a {valor_convertido:.2f} Ienes.")
    elif opcao == 3:
        taxa_euro = 6.06
        valor_convertido = valor_reais / taxa_euro
        print(f"{valor_reais} Reais equivalem a {valor_convertido:.2f} Euros.")
    else:
        print("Opção inválida.")

converter_moeda()