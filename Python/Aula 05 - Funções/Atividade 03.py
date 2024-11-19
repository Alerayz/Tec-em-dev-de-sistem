# def calcular_media_ponderada(nota1, nota2, nota3):
#     peso1, peso2, peso3 = 2, 3, 5
    
#     media = round((nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3), 2)
    
#     return media

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))

# media_final = calcular_media_ponderada(nota1, nota2, nota3)

# media_final_arredondada = round(media_final, 2)

# print(f'A média final do aluno é: {round(media_final_arredondada, 2)}')

from os import system as sy
sy('cls')

def media():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    return(nota1 + nota2 + nota3) / (2 + 3 + 5)

response = media()
print(f'A média final do aluno é: {round(response, 2)}' , end=' ')
print('\033[32mAPROVADO!\033[m' if response >= 5 else '\033[31mREPROVADO!\033[m') 