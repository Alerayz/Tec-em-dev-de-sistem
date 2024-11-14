print('----CATALOGO----')
print('A) PAMONHA - R$ 7,00')
print('B) CALDO - R$ 4,00')
print('C) PASTEL - R$ 6,99')
print('D) CAFÉ - R$ 3,00')
print('E) CANCELAR')
print('F) FINALIZAR')

adicionar = 'sim'
valor = 0.0

while adicionar .lower() == 'sim':

    opcao = input('Qual opcao desejada: ') .lower()
    valor = float

    match opcao:
        case 'a':
            print("Você escolheu pamonha")
            valor = 7.00
        case 'b':
            print("Você escolheu caldo")
            valor = 4.00
        case 'c':
            print("Você escolheu pastel")
            valor = 6.99
        case 'd':
            print("Você escolheu café")
            valor = 3.00
        case 'e':
            print("Pedido cancelado!")
        case 'f':
            print("Total do pedido: " ,valor)
            break
        case _:
            print("Opção inválida! Tente novamente.")

    adicionar = input('Deseja adicionar mais itens? (sim/não): ') .lower()
        
    #adicionar .reaplace('á' , 'a' )
    # if adicionar == 'não':
    #     break

print('Valor total do pedido: R$' , valor)
print ('Obrigado pelo seu pedido,ele está sendo processado')