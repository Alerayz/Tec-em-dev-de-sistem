usuario_correto = "ADM"
senha_correta = "ADM"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login realizado com sucesso!")
else:
    print("Falha no login. Usuário ou senha incorretos.")