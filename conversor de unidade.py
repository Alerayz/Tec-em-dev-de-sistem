def converter_comprimento(valor, unidade_origem, unidade_destino):
    # Conversões de comprimento
    unidades = {
        'metros': 1,
        'centimetros': 100,
        'milimetros': 1000,
        'quilometros': 0.001,
        'poles': 39.3701,
        'milhas': 0.000621371
    }
    
    valor_em_metros = valor / unidades[unidade_origem]
    return valor_em_metros * unidades[unidade_destino]

def converter_peso(valor, unidade_origem, unidade_destino):
    # Conversões de peso
    unidades = {
        'gramas': 1,
        'quilogramas': 0.001,
        'miligramas': 1000,
        'libras': 0.00220462,
        'oncas': 0.035274
    }
    
    valor_em_gramas = valor / unidades[unidade_origem]
    return valor_em_gramas * unidades[unidade_destino]

def converter_temperatura(valor, unidade_origem, unidade_destino):
    # Conversões de temperatura
    if unidade_origem == 'celsius':
        if unidade_destino == 'fahrenheit':
            return (valor * 9/5) + 32
        elif unidade_destino == 'kelvin':
            return valor + 273.15
    elif unidade_origem == 'fahrenheit':
        if unidade_destino == 'celsius':
            return (valor - 32) * 5/9
        elif unidade_destino == 'kelvin':
            return (valor - 32) * 5/9 + 273.15
    elif unidade_origem == 'kelvin':
        if unidade_destino == 'celsius':
            return valor - 273.15
        elif unidade_destino == 'fahrenheit':
            return (valor - 273.15) * 9/5 + 32

def main():
    print("Escolha o tipo de conversão:")
    print("1. Comprimento")
    print("2. Peso")
    print("3. Temperatura")
    
    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        valor = float(input("Digite o valor a ser convertido: "))
        unidade_origem = input("Digite a unidade de origem (metros, centimetros, milimetros, quilometros, poles, milhas): ").lower()
        unidade_destino = input("Digite a unidade de destino (metros, centimetros, milimetros, quilometros, poles, milhas): ").lower()
        resultado = converter_comprimento(valor, unidade_origem, unidade_destino)
        print(f"{valor} {unidade_origem} é igual a {resultado} {unidade_destino}")

    elif escolha == '2':
        valor = float(input("Digite o valor a ser convertido: "))
        unidade_origem = input("Digite a unidade de origem (gramas, quilogramas, miligramas, libras, oncas): ").lower()
        unidade_destino = input("Digite a unidade de destino (gramas, quilogramas, miligramas, libras, oncas): ").lower()
        resultado = converter_peso(valor, unidade_origem, unidade_destino)
        print(f"{valor} {unidade_origem} é igual a {resultado} {unidade_destino}")

    elif escolha == '3':
        valor = float(input("Digite o valor a ser convertido: "))
        unidade_origem = input("Digite a unidade de origem (celsius, fahrenheit, kelvin): ").lower()
        unidade_destino = input("Digite a unidade de destino (celsius, fahrenheit, kelvin): ").lower()
        resultado = converter_temperatura(valor, unidade_origem, unidade_destino)
        print(f"{valor} {unidade_origem} é igual a {resultado} {unidade_destino}")

    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()