"""
ENTRADA
*PESO

PROCESSAMENTO
 SE TEM MULTA (ACIMA DE 50)
   VER EXCESSO (4 POR QUILO)
   CALCULAR
 SENAO
   MOSTRAR QUE NÃO HA MULTA

SAIDA
    MOSTRAR O VALOR DA MULTA
"""

peso = float(input("Digite o peso :"))
peso_maximo = 50.00
multa = 4.00

if peso > peso_maximo:
    ex = peso - peso_maximo
    valor_total = ex * multa
    print(f'O valor total a ser pago é R$ {valor_total}')
else:
    print('Não há multa!')