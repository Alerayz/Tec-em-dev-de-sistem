def dia_da_semana(numero):
    dias = {
        1: "segunda-feira",
        2: "terça-feira",
        3: "quarta-feira",
        4: "quinta-feira",
        5: "sexta-feira",
        6: "sábado",
        7: "domingo"
    }
    return dias.get(numero, "Número inválido! Por favor, digite um número de 1 a 7.")

try:
    numero_usuario = int(input("Digite um número de 1 a 7: "))
    resultado = dia_da_semana(numero_usuario)
    print(resultado)
except ValueError:
    print("Por favor, digite um número válido.")