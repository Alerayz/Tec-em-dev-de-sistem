NOME_USUARIO = 'Victor'
SENHA_USUARIO = '1234'

nome = input('Digite o seu nome')
senha = input('Digite a sua senha')

# AND , TRUE TRUE
# OR , BASTA UM TRUE
# NOT , EXCLUSAO
if NOME_USUARIO == nome and SENHA_USUARIO == senha:
    print("VOCE ENTROU NA PLATAFORMA")
else:
    print("USUARIO OU SENHA INCORRETA")
