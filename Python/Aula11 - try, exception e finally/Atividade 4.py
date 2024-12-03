from os import system as sy
import time
sy('cls')

def main():
    saldo = 999.999,99 
    while True:
        try:
            valor_saque = float(input("Digite o valor a ser sacado: R$ "))

            if valor_saque <= 0:
                print("O valor do saque deve ser maior que zero. Tente novamente.")
                continue

            if valor_saque > saldo:
                print("Saldo insuficiente. Tente um valor menor.")
                continue

            saldo -= valor_saque
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um valor numérico.")

    print(f"Saldo atualizado: R$ {saldo:.2f}")

if __name__ == "__main__":
    main()