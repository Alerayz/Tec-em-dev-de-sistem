# AULA 1 - INTRODUÇÃO E VARIAVEIS

# COMENTÁRIO

"""
DOCTRING - ANOTAÇÕES
"""

# PRINT - ESCREVER
print("BOM DIA !!!")
print("Victor Santos Rohod")
# CRLF - caracteres que representam 
# a quebra de linha do sistema
# \r return
# \n line feed

# end (end - fim do print)
print('Uma informação ',' importante',end=' \n')
# sep (sep - separador do print)
print('Uma informação ',' importante',sep='----')
print(123)

# type
print(type(11)) # int (numero inteiro) ex 1, 0
print(type(1.5)) # float (numero flutuante, real) ex 1.5,-1.4
print(type('oi')) # str (string, caractere) ex 'oi', "opa"
print(type(True)) # bool (boolean , logico) ex True, False

# variavel
# 1 - caracteres especiais 
# 2 - espaços vazios 
# camelCase = umExemplo
# snakeCase = um_exemplo
# 3 - evite numeros solos, ou começo de variavel
# *4 - evite nomes pouco descritivos

# variaveis maiusculo são contantes
# constante não ter seu valor mudado
TESTE = 1
teste = "teste1"
teste_legal = 'TESTE'
print(teste,teste,teste)