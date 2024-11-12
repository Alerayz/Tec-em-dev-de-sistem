import argparse

def calcular(op, num1, num2):
    if op == 'soma':
        return num1 + num2
    elif op == 'subtracao':
        return num1 - num2
    elif op == 'multiplicacao':
        return num1 * num2
    elif op == 'divisao':
        if num2 == 0:
            return 'Indefinido (divisão por zero)'
        return num1 / num2
    else:
        return 'Operação inválida!'

def main():
    # Criação do parser
    parser = argparse.ArgumentParser(description='Calculadora simples com argumentos.')

    # Adicionando argumentos
    parser.add_argument('operacao', type=str, help='Operação a ser realizada: soma, subtracao, multiplicacao, divisao')
    parser.add_argument('num1', type=float, help='Primeiro número')
    parser.add_argument('num2', type=float, help='Segundo número')

    # Parse dos argumentos
    args = parser.parse_args()

    # Calculando o resultado
    resultado = calcular(args.operacao, args.num1, args.num2)

    # Exibindo o resultado
    print(f'Resultado: {resultado}')

if __name__ == '__main__':
    main()