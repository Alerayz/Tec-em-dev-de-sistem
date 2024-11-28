from os import system as sy
import time
sy('cls')

def calcular():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
            resultado = num1 / num2
        else:
            raise ValueError("Erro: Operação inválida. Use +, -, * ou /.")

        print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")

    except ValueError as ve:
        print(ve)
    except ZeroDivisionError as zde:
        print(zde)
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    calcular()