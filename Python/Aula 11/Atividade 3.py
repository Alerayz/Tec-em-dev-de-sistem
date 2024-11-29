from os import system as sy
import time
sy('cls')

def calcular_imc(peso, altura):
    try:
        imc = peso / (altura ** 2)
        return imc
    except ZeroDivisionError:
        return None

def main():
    while True:
        try:
            peso = float(input("Por favor, insira seu peso em kg: "))
            altura = float(input("Por favor, insira sua altura em metros: "))

            if altura <= 0:
                print("A altura deve ser maior que zero. Tente novamente.")
                continue

            imc = calcular_imc(peso, altura)
            if imc is not None:
                print(f"Seu IMC é: {imc:.2f}")
                if imc < 18.5:
                    print("Classificação: Abaixo do peso")
                elif 18.5 <= imc < 24.9:
                    print("Classificação: Peso normal")
                elif 25 <= imc < 29.9:
                    print("Classificação: Sobrepeso")
                else:
                    print("Classificação: Obesidade")
            else:
                print("Erro ao calcular o IMC. Verifique os valores inseridos.")
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")

    print("Processo finalizado.")

if __name__ == "__main__":
    main()