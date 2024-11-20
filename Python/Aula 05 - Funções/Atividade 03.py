from os import system as sy
import time
sy('cls')

def calcular_media_ponderada(nota1, nota2, nota3):
    peso1, peso2, peso3 = 2, 3, 5
    
    media = round((nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3), 2)
    
    return media
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media_final = calcular_media_ponderada(nota1, nota2, nota3)

media_final_arredondada = round(media_final, 2)

response = media_final_arredondada
print(f'A média do aluno é: {response:.2f}' , end=' ')
print(f'A média final do aluno é: {round(media_final_arredondada, 2)}')
print('\033[32mAPROVADO!\033[m' if response >= 7 else '\033[31mREPROVADO!\033[m')
