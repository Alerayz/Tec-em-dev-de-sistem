def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

try:
    idade_usuario = int(input("Digite a sua idade: "))
    resultado = verificar_idade(idade_usuario)
    print(resultado)
except ValueError:
    print("Por favor, digite um número válido.")