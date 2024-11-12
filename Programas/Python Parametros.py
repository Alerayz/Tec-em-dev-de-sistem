def calcular_soma(a, b):
    return a + b

def calcular_subtracao(a, b):
    return a - b

def calcular_multiplicacao(a, b):
    return a * b

def calcular_divisao(a, b):
    if b == 0:
        return 'Indefinido (divisão por zero)'
    return a / b

def main():
    # Solicita os números e a operação ao usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    operacao = input("Digite o número da operação (1/2/3/4): ")

    if operacao == '1':
        resultado = calcular_soma(num1, num2)
        print(f'Resultado da soma: {resultado}')
    elif operacao == '2':
        resultado = calcular_subtracao(num1, num2)
        print(f'Resultado da subtração: {resultado}')
    elif operacao == '3':
        resultado = calcular_multiplicacao(num1, num2)
        print(f'Resultado da multiplicação: {resultado}')
    elif operacao == '4':
        resultado = calcular_divisao(num1, num2)
        print(f'Resultado da divisão: {resultado}')
    else:
        print("Operação inválida!")

if __name__ == '__main__':
    main()